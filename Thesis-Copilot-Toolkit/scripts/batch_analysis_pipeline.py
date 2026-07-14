#!/usr/bin/env python3
"""
Batch analysis pipeline

This script locates B1/B2/B3/B4 and all it*_raw CSVs under the results
folder, processes them in configurable batches, normalizes metrics and
produces per-batch consolidated CSVs, aggregated stats and simple
pairwise post-hoc results. Outputs go to `results/analysis/batches`.

Usage:
    python Thesis-Copilot-Toolkit/scripts/batch_analysis_pipeline.py --batch-size 10
"""
from pathlib import Path
import argparse
import json
import sys

import math
import re

try:
    import pandas as pd
    import numpy as np
    import scipy.stats as stats
except Exception as e:
    print("Missing python packages. Ensure pandas/numpy/scipy are installed.", file=sys.stderr)
    raise

def find_files(results_dir: Path):
    results_dir = Path(results_dir)
    files = []
    # Known B1/B2 filenames
    for name in ("opt_benchmark_b1_protocol_raw.csv", "opt_benchmark_b2_full_scale_raw.csv"):
        p = results_dir / name
        if p.exists():
            files.append(p)
    # B3/B4 summary CSVs (any file with b3 or b4 prefix)
    for p in sorted(results_dir.glob('b3*.csv')):
        files.append(p)
    for p in sorted(results_dir.glob('b4*.csv')):
        files.append(p)
    # All iteration raw files named like it*_raw.csv (covers it100_... etc.)
    for p in sorted(results_dir.glob('it*_raw.csv')):
        files.append(p)
    # Also include patterns like it*_*.csv where raw may be embedded differently
    # but avoid duplicates
    unique = []
    seen = set()
    for p in files:
        if str(p) not in seen:
            unique.append(p)
            seen.add(str(p))
    return unique

def read_and_normalize(path: Path, metrics=('mae','rmse','dtw','snr')):
    try:
        df = pd.read_csv(path)
    except Exception as e:
        print(f"Failed to read {path}: {e}")
        return None
    # normalize column names to lower
    df.columns = [c.lower() for c in df.columns]
    # Coerce numeric metrics
    for m in metrics:
        if m in df.columns:
            df[m] = pd.to_numeric(df[m], errors='coerce')
    # Create a block id to use as Friedman block if possible
    if 'mask_seed' in df.columns:
        df['block'] = df.apply(lambda r: f"{r.get('dataset','')}_{r.get('scenario','')}_{r.get('missing_ratio','')}_{r.get('mask_seed','')}", axis=1)
    elif 'run_id' in df.columns:
        df['block'] = df['run_id'].astype(str)
    else:
        # fallback to combination of dataset+scenario+missing_ratio+index
        if 'dataset' in df.columns or 'scenario' in df.columns or 'missing_ratio' in df.columns:
            df['block'] = df.apply(lambda r: f"{r.get('dataset','')}_{r.get('scenario','')}_{r.get('missing_ratio','')}_{r.name}", axis=1)
        else:
            df['block'] = df.index.astype(str)
    df['source_file'] = path.name
    # Keep a reduced set of columns if available
    keep = [c for c in ['dataset','scenario','method','family','graph','missing_ratio','mae','rmse','dtw','snr','block','source_file'] if c in df.columns]
    return df[keep]

def holm_correction(pvals):
    # simple Holm-Bonferroni correction for a list of p-values
    n = len(pvals)
    if n == 0:
        return []
    sorted_idx = sorted(range(n), key=lambda i: pvals[i])
    adj = [None]*n
    for rank, idx in enumerate(sorted_idx):
        adj[idx] = min(1.0, pvals[idx] * (n - rank))
    return adj

def run_batch(batch_files, out_dir: Path, batch_idx:int, metric='mae'):
    dfs = []
    for p in batch_files:
        df = read_and_normalize(p)
        if df is None:
            continue
        if metric not in df.columns:
            # skip files without the requested metric
            continue
        dfs.append(df)
    if not dfs:
        print(f"Batch {batch_idx}: no data for metric {metric}")
        return None
    all_df = pd.concat(dfs, ignore_index=True)
    all_df = all_df.dropna(subset=[metric])
    out_dir.mkdir(parents=True, exist_ok=True)
    consolidated_path = out_dir / f"batch_{batch_idx:03d}_consolidated.csv"
    all_df.to_csv(consolidated_path, index=False)
    # Aggregate safely: 'scenario' may be missing in some files
    agg_path = out_dir / f"batch_{batch_idx:03d}_agg.csv"
    group_cols = [c for c in ['scenario', 'method'] if c in all_df.columns]
    if 'method' not in group_cols:
        # cannot aggregate without method
        print(f"Batch {batch_idx}: 'method' column missing; skipping aggregation")
        # write empty placeholder
        pd.DataFrame().to_csv(agg_path, index=False)
    else:
        agg = all_df.groupby(group_cols)[metric].agg(['count','mean','std']).reset_index()
        agg.to_csv(agg_path, index=False)
    # Statistical tests per scenario
    scenarios = all_df['scenario'].unique() if 'scenario' in all_df.columns else [None]
    stats_summary = {}
    for s in scenarios:
        sub = all_df[all_df['scenario']==s] if s is not None else all_df
        if 'block' not in sub.columns or 'method' not in sub.columns:
            continue
        pivot = sub.pivot_table(index='block', columns='method', values=metric, aggfunc='mean')
        pivot = pivot.dropna(axis=0, how='any')
        methods = list(pivot.columns)
        if len(methods) < 2 or pivot.shape[0] < 2:
            continue
        try:
            stat, pval = stats.friedmanchisquare(*[pivot[c].values for c in methods])
        except Exception as e:
            stat, pval = None, None
        stats_summary_key = str(s) if s is not None else 'global'
        stats_summary[stats_summary_key] = {'friedman_stat': stat, 'p_value': pval, 'n_blocks': int(pivot.shape[0]), 'methods': methods}
        # pairwise Wilcoxon (fallback post-hoc)
        pairs = []
        raw_pvals = []
        for i in range(len(methods)):
            for j in range(i+1, len(methods)):
                m1 = methods[i]; m2 = methods[j]
                x = pivot[m1].values; y = pivot[m2].values
                try:
                    w_stat, w_p = stats.wilcoxon(x, y)
                except Exception:
                    w_stat, w_p = None, None
                pairs.append((m1, m2, w_stat, w_p))
                raw_pvals.append(w_p if w_p is not None else 1.0)
        adj = holm_correction(raw_pvals)
        pairwise_results = []
        for k, pair in enumerate(pairs):
            m1, m2, w_stat, w_p = pair
            pairwise_results.append({'method1':m1, 'method2':m2, 'wilcoxon_stat': w_stat, 'p_value': w_p, 'adj_p_value': adj[k] if adj else None})
        stats_summary[stats_summary_key]['pairwise'] = pairwise_results
    json_path = out_dir / f"batch_{batch_idx:03d}_stats.json"
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(stats_summary, f, indent=2)
    # Simple boxplots per scenario saved as PNGs
    try:
        import matplotlib.pyplot as plt
        for s in scenarios:
            sub = all_df[all_df['scenario']==s] if s is not None else all_df
            if sub.empty:
                continue
            if 'method' not in sub.columns:
                continue
            methods = sub['method'].unique()
            data = [sub.loc[sub['method']==m, metric].dropna().values for m in methods]
            if not any(len(d)>0 for d in data):
                continue
            fig, ax = plt.subplots(figsize=(8,4))
            ax.boxplot(data, showfliers=False)
            ax.set_xticklabels(methods, rotation=45, ha='right')
            ax.set_title(f"Batch {batch_idx} - {metric} by method - scenario {s}")
            ax.set_ylabel(metric)
            plt.tight_layout()
            png = out_dir / f"batch_{batch_idx:03d}_box_{str(s).replace('/','_')}.png"
            fig.savefig(png)
            plt.close(fig)
    except Exception as e:
        print("Plotting failed:", e)
    return {'consolidated': str(consolidated_path), 'agg': str(agg_path), 'stats': str(json_path)}

def run_pipeline(results_dir, out_dir, batch_size=10, metric='mae'):
    results_dir = Path(results_dir)
    out_dir = Path(out_dir)
    files = find_files(results_dir)
    print(f"Discovered {len(files)} candidate files to process.")
    if len(files) == 0:
        return []
    # chunk into batches
    batches = [files[i:i+batch_size] for i in range(0, len(files), batch_size)]
    results = []
    for idx, batch in enumerate(batches, start=1):
        print(f"Processing batch {idx}/{len(batches)} ({len(batch)} files)")
        res = run_batch(batch, out_dir, idx, metric=metric)
        results.append(res)
    # aggregate consolidated CSVs
    consolidated_list = []
    for r in results:
        if not r:
            continue
        try:
            consolidated_list.append(pd.read_csv(r['consolidated']))
        except Exception:
            continue
    if consolidated_list:
        final = pd.concat(consolidated_list, ignore_index=True)
        final_path = out_dir / 'consolidated_all_batches.csv'
        final.to_csv(final_path, index=False)
        print(f"Wrote {final_path}")
    return results

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--results-dir', default='Thesis-Copilot-Toolkit/results')
    parser.add_argument('--out-dir', default='Thesis-Copilot-Toolkit/results/analysis/batches')
    parser.add_argument('--batch-size', type=int, default=10)
    parser.add_argument('--metric', default='mae')
    args = parser.parse_args()
    run_pipeline(args.results_dir, args.out_dir, batch_size=args.batch_size, metric=args.metric)

if __name__ == '__main__':
    main()
