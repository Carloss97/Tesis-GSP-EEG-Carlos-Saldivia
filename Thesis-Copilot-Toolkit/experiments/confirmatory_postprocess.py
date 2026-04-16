"""
confirmatory_postprocess.py

Wait for a confirmatory results folder (`results_confirmatory_*`), run
`generate_b1_b4.py` over it, aggregate raw CSVs and perform paired
Wilcoxon tests with Benjamini-Hochberg correction. Produce summary CSVs
and a short Markdown report.

Usage (run in repo root):
  $env:PYTHONPATH='Thesis-Copilot-Toolkit'; & .venv\Scripts\python.exe Thesis-Copilot-Toolkit\experiments\confirmatory_postprocess.py

This script is conservative and robust to partial outputs: it waits until
the confirmatory folder exists and has at least one `_run_metadata.json`.
"""
from __future__ import annotations

import argparse
import subprocess
import sys
import time
from pathlib import Path
from typing import List, Optional, Tuple

import numpy as np
import pandas as pd
from scipy import stats

ROOT = Path(__file__).resolve().parents[1]


def find_latest_confirm_dir(root: Path) -> Optional[Path]:
    cand = sorted(root.glob('results_confirmatory_*'), key=lambda p: p.stat().st_mtime, reverse=True)
    return cand[0] if cand else None


def count_meta_files(results_dir: Path) -> int:
    return len(list(results_dir.glob('*_run_metadata.json')))


def run_generate_b1_b4(results_dir: Path) -> None:
    gen = ROOT / 'experiments' / 'generate_b1_b4.py'
    cmd = [sys.executable, str(gen), '--results', str(results_dir.name)]
    print('Running generator:', ' '.join(cmd))
    subprocess.run(cmd, check=False)


def benjamini_hochberg(pvals: List[float]) -> List[float]:
    """Return BH-adjusted p-values in the original order."""
    if not pvals:
        return []
    p = np.asarray(pvals)
    m = len(p)
    order = np.argsort(p)
    ranked = p[order]
    adjusted = np.minimum.accumulate((m / (np.arange(1, m + 1))) * ranked[::-1])[::-1]
    adjusted = np.clip(adjusted, 0, 1)
    p_adj = np.empty(m)
    p_adj[order] = adjusted
    return p_adj.tolist()


def aggregate_raw_csvs(results_dir: Path) -> pd.DataFrame:
    raws = sorted(results_dir.glob('*_raw.csv'))
    if not raws:
        raise FileNotFoundError('No *_raw.csv files found in ' + str(results_dir))
    dfs = []
    for f in raws:
        try:
            df = pd.read_csv(f)
            dfs.append(df)
        except Exception as exc:
            print('Warning: failed to read', f, exc)
    if not dfs:
        raise RuntimeError('No readable raw CSVs')
    all_df = pd.concat(dfs, ignore_index=True, sort=False)
    return all_df


def paired_wilcoxon_tests(df: pd.DataFrame, value_col: str = 'mae') -> pd.DataFrame:
    # determine grouping keys that help align paired observations
    candidate_keys = ['dataset', 'tag', 'seed', 'missing_ratio', 'case', 'case_id']
    group_keys = [k for k in candidate_keys if k in df.columns]
    if not group_keys:
        # fallback: try to align by index-like columns
        group_keys = [c for c in df.columns if c not in ['method', value_col]]

    pivot_index = group_keys
    print('Using pivot/group keys for pairing:', pivot_index)

    # pivot to have methods as columns and grouped index
    pivot = df.pivot_table(index=pivot_index, columns='method', values=value_col)
    methods = list(pivot.columns)
    results = []
    pvals = []
    pairs = []
    for i in range(len(methods)):
        for j in range(i + 1, len(methods)):
            m1 = methods[i]
            m2 = methods[j]
            sub = pivot[[m1, m2]].dropna()
            if sub.shape[0] < 1:
                stat = np.nan
                p = np.nan
            else:
                try:
                    stat, p = stats.wilcoxon(sub[m1], sub[m2])
                except Exception:
                    # fallback to paired t-test
                    try:
                        stat_t, p = stats.ttest_rel(sub[m1], sub[m2])
                        stat = stat_t
                    except Exception:
                        stat = np.nan
                        p = np.nan
            results.append({'method1': m1, 'method2': m2, 'n_pairs': int(sub.shape[0]), 'stat': float(stat) if not np.isnan(stat) else None, 'pval': float(p) if not np.isnan(p) else None})
            pvals.append(float(p) if (p is not None and not np.isnan(p)) else 1.0)
            pairs.append((m1, m2))

    adj = benjamini_hochberg(pvals)
    for idx, rec in enumerate(results):
        rec['pval_bh'] = adj[idx]
        rec['significant_bh'] = adj[idx] < 0.05

    return pd.DataFrame(results)


def save_markdown_summary(summary_df: pd.DataFrame, out_md: Path, top_n: int = 10) -> None:
    lines = []
    lines.append('# Confirmatory Results Summary')
    lines.append('')
    lines.append('Top methods by mean MAE:')
    lines.append('')
    lines.append(summary_df.head(top_n).to_markdown(index=False))
    out_md.write_text('\n'.join(lines), encoding='utf-8')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--confirm-dir', type=str, default=None)
    parser.add_argument('--poll', type=int, default=300)
    parser.add_argument('--timeout', type=int, default=24 * 3600)
    parser.add_argument('--min-files', type=int, default=1)
    args = parser.parse_args()

    start = time.time()
    confirm_dir = Path(args.confirm_dir) if args.confirm_dir else None

    while True:
        if confirm_dir and confirm_dir.exists():
            done = count_meta_files(confirm_dir)
            print(f'Found confirm dir {confirm_dir} — metadata files: {done}')
        else:
            latest = find_latest_confirm_dir(ROOT)
            if latest:
                confirm_dir = latest
                done = count_meta_files(confirm_dir)
                print(f'Using latest confirm dir {confirm_dir} — metadata files: {done}')
            else:
                done = 0
                print('No confirmatory folder found yet')

        if done >= args.min_files:
            print('Confirmatory outputs detected — proceeding with postprocessing')
            break

        if time.time() - start > args.timeout:
            print('Timeout waiting for confirmatory results. Exiting.')
            return
        time.sleep(args.poll)

    assert confirm_dir is not None
    # generate B1–B4 for confirmatory folder
    try:
        run_generate_b1_b4(confirm_dir)
    except Exception as exc:
        print('generate_b1_b4 failed:', exc)

    try:
        all_df = aggregate_raw_csvs(confirm_dir)
    except Exception as exc:
        print('Aggregation failed:', exc)
        return

    # compute per-method summary
    if 'method' not in all_df.columns or 'mae' not in all_df.columns:
        print('Expected columns `method` and `mae` not found in aggregated raw CSVs')
        return

    summary = all_df.groupby('method', as_index=False)['mae'].agg(mae_mean='mean', mae_std='std', n='count').sort_values('mae_mean')
    summary_csv = confirm_dir / 'confirm_summary.csv'
    summary.to_csv(summary_csv, index=False)
    print('Wrote summary to', summary_csv)

    # pairwise tests
    pairwise = paired_wilcoxon_tests(all_df, value_col='mae')
    pairwise_csv = confirm_dir / 'confirm_pairwise_wilcoxon.csv'
    pairwise.to_csv(pairwise_csv, index=False)
    print('Wrote pairwise tests to', pairwise_csv)

    # markdown summary
    md = confirm_dir / 'confirm_summary.md'
    save_markdown_summary(summary, md)
    print('Wrote markdown summary to', md)

    print('Confirmatory postprocessing complete.')


if __name__ == '__main__':
    main()
