#!/usr/bin/env python3
"""Compare Phase A vs Phase B across existing run artifacts in `results/`.

Produces:
- results/pilot_A_vs_B_full_aggregation.csv
- results/pilot_comparative_report_A_vs_B_full.md
- results/pilot_A_vs_B_full_boxplot.png

Usage:
  conda activate eegrasp
  python Thesis-Copilot-Toolkit/scripts/compare_phaseA_vs_phaseB.py
"""
import os
import json
import glob
import math
import pandas as pd
import numpy as np

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

SCRIPT_DIR = os.path.dirname(__file__)
RESULTS_DIR = os.path.normpath(os.path.join(SCRIPT_DIR, '..', 'results'))
SCHEDULE_A = os.path.normpath(os.path.join(SCRIPT_DIR, '..', 'experiments', 'schedules', 'it01-it50_schedule_phaseA_real_varied.json'))
SCHEDULE_B = os.path.normpath(os.path.join(SCRIPT_DIR, '..', 'experiments', 'schedules', 'it01-it50_schedule_phaseB_real_mne_sample.json'))
OUT_CSV = os.path.join(RESULTS_DIR, 'pilot_A_vs_B_full_aggregation.csv')
OUT_MD = os.path.join(RESULTS_DIR, 'pilot_comparative_report_A_vs_B_full.md')
OUT_PLOT = os.path.join(RESULTS_DIR, 'pilot_A_vs_B_full_boxplot.png')


def find_all_run_metadata(results_dir):
    paths = glob.glob(os.path.join(results_dir, '**', '*run_metadata.json'), recursive=True)
    runs = []
    for p in paths:
        try:
            with open(p, 'r', encoding='utf-8') as f:
                md = json.load(f)
        except Exception:
            continue
        dirp = os.path.dirname(p)
        stats_candidates = glob.glob(os.path.join(dirp, '*_stats.csv'))
        stats_path = None
        tag = md.get('tag') or md.get('key')
        # prefer stats with tag in filename
        for sc in stats_candidates:
            if tag and os.path.basename(sc).startswith(tag):
                stats_path = sc
                break
        if stats_path is None and stats_candidates:
            stats_path = stats_candidates[0]
        # fallback: top-level results <tag>_stats.csv
        if stats_path is None and tag:
            top_candidate = os.path.join(results_dir, f"{tag}_stats.csv")
            if os.path.exists(top_candidate):
                stats_path = top_candidate
        runs.append({'meta_path': p, 'meta': md, 'stats_path': stats_path})
    return runs


def build_method_values(runs):
    mapping = {}
    for r in runs:
        md = r['meta']
        tag = md.get('tag') or md.get('key')
        datasets = md.get('datasets') or md.get('requested_datasets') or []
        dataset = datasets[0] if datasets else None
        stats_path = r.get('stats_path')
        method_medians = {}
        if stats_path and os.path.exists(stats_path):
            try:
                df = pd.read_csv(stats_path)
                if 'method' in df.columns and 'mae_median' in df.columns:
                    for _, row in df.iterrows():
                        method = str(row['method'])
                        try:
                            val = float(row['mae_median'])
                        except Exception:
                            val = float('nan')
                        method_medians[method] = val
            except Exception:
                pass
        mapping[(tag, dataset)] = {'meta_path': r['meta_path'], 'meta': md, 'method_medians': method_medians, 'stats_path': stats_path}
    return mapping


def load_schedule(schedule_path):
    with open(schedule_path, 'r', encoding='utf-8') as f:
        j = json.load(f)
    iterations = j.get('iterations', [])
    seq = []
    for it in iterations:
        tag = it.get('tag') or it.get('key')
        datasets = it.get('datasets') or []
        dataset = datasets[0] if datasets else None
        seq.append({'tag': tag, 'dataset': dataset})
    return seq


def collect_group_values(schedule_seq, mapping):
    methods_values = {}
    missing = []
    for entry in schedule_seq:
        tag = entry['tag']
        dataset = entry['dataset']
        key = (tag, dataset)
        entry_map = None
        if key in mapping:
            entry_map = mapping[key]
        else:
            # try looser match: same tag and dataset present in metadata lists
            for (t, d), v in mapping.items():
                if t == tag:
                    md = v.get('meta', {})
                    md_datasets = md.get('datasets') or md.get('requested_datasets') or []
                    if not dataset or (md_datasets and dataset in md_datasets) or d == dataset:
                        entry_map = v
                        break
        if entry_map is None:
            missing.append((tag, dataset))
            continue
        mm = entry_map.get('method_medians', {})
        if not mm:
            missing.append((tag, dataset))
            continue
        for m, val in mm.items():
            if isinstance(val, (int, float)) and (not math.isnan(val)):
                methods_values.setdefault(m, []).append(val)
    return methods_values, missing


def mann_whitney_u_from_samples(x, y):
    n1 = len(x); n2 = len(y)
    if n1 == 0 or n2 == 0:
        return None, None
    try:
        from scipy.stats import mannwhitneyu
        res = mannwhitneyu(x, y, alternative='two-sided')
        return float(res.statistic), float(res.pvalue)
    except Exception:
        pass
    # fallback using rank normal approximation
    combined = np.concatenate([np.asarray(x), np.asarray(y)])
    ranks = pd.Series(combined).rank(method='average').to_numpy()
    R1 = ranks[:n1].sum()
    U1 = R1 - n1 * (n1 + 1) / 2.0
    U = float(U1)
    mu = n1 * n2 / 2.0
    sigma = math.sqrt(n1 * n2 * (n1 + n2 + 1) / 12.0)
    if sigma == 0:
        p = 1.0
    else:
        z = (U - mu) / sigma
        p = math.erfc(abs(z) / math.sqrt(2.0))
    return U, p


def main():
    runs = find_all_run_metadata(RESULTS_DIR)
    mapping = build_method_values(runs)
    scheduleA = load_schedule(SCHEDULE_A)
    scheduleB = load_schedule(SCHEDULE_B)
    A_vals, A_missing = collect_group_values(scheduleA, mapping)
    B_vals, B_missing = collect_group_values(scheduleB, mapping)
    methods = sorted(set(list(A_vals.keys()) + list(B_vals.keys())))
    rows = []
    for m in methods:
        a = A_vals.get(m, [])
        b = B_vals.get(m, [])
        median_a = float(np.median(a)) if len(a) > 0 else float('nan')
        median_b = float(np.median(b)) if len(b) > 0 else float('nan')
        n_a = len(a); n_b = len(b)
        U, p = mann_whitney_u_from_samples(a, b)
        significant = (p is not None and (not math.isnan(p)) and p < 0.05)
        rows.append({'method': m, 'median_A': median_a, 'median_B': median_b, 'n_A': n_a, 'n_B': n_b, 'U': U if U is not None else 'NA', 'p_value': p if p is not None else 'NA', 'significant': bool(significant)})
    df = pd.DataFrame(rows)
    df.to_csv(OUT_CSV, index=False)

    # write markdown summary
    with open(OUT_MD, 'w', encoding='utf-8') as f:
        f.write('# Full Phase A vs Phase B comparison\n\n')
        f.write('Generated automatically.\n\n')
        f.write(f'Missing A runs: {len(A_missing)}\n\n')
        if A_missing:
            f.write('Example missing A entries:\n')
            for t in A_missing[:10]:
                f.write(f'- {t}\n')
            f.write('\n')
        f.write(f'Missing B runs: {len(B_missing)}\n\n')
        if B_missing:
            f.write('Example missing B entries:\n')
            for t in B_missing[:10]:
                f.write(f'- {t}\n')
            f.write('\n')
        f.write('## Aggregated comparison table\n\n')
        f.write(df.to_markdown(index=False))
        f.write('\n')

    # boxplot
    plot_arrays = []
    labels = []
    for m in methods:
        plot_arrays.append(A_vals.get(m, []))
        labels.append(f"{m}_A")
        plot_arrays.append(B_vals.get(m, []))
        labels.append(f"{m}_B")
    plt.figure(figsize=(max(8, len(methods) * 1.2), 6))
    plt.boxplot(plot_arrays, showfliers=False)
    plt.xticks(range(1, len(labels) + 1), labels, rotation=90, fontsize=6)
    plt.ylabel('MAE median')
    plt.title('Phase A vs Phase B MAE per method')
    plt.tight_layout()
    plt.savefig(OUT_PLOT, dpi=150)
    print('Wrote', OUT_CSV, OUT_MD, OUT_PLOT)
    if A_missing:
        print('Missing A entries (sample):', A_missing[:10])
    if B_missing:
        print('Missing B entries (sample):', B_missing[:10])
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
