#!/usr/bin/env python3
"""Compare Phase A vs Phase B using a whitelist of accepted NO-GO runs.

Reads `results/no_go_accepted_provisional.csv` and only uses those runs
to aggregate per-method `mae_median` values for Phase A and Phase B schedules.

Outputs (in `results/`):
- pilot_A_vs_B_full_aggregation_no_go_accepted.csv
- pilot_comparative_report_A_vs_B_no_go_accepted.md
- pilot_A_vs_B_full_boxplot_no_go_accepted.png

Usage:
  conda activate eegrasp
  python Thesis-Copilot-Toolkit/scripts/compare_phaseA_vs_phaseB_use_accepted.py
"""
import os
import csv
import json
import math
import glob
from pathlib import Path

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

SCRIPT_DIR = Path(__file__).resolve().parent
RESULTS_DIR = SCRIPT_DIR.parent / 'results'
SCHEDULE_A = SCRIPT_DIR.parent / 'experiments' / 'schedules' / 'it01-it50_schedule_phaseA_real_varied.json'
SCHEDULE_B = SCRIPT_DIR.parent / 'experiments' / 'schedules' / 'it01-it50_schedule_phaseB_real_mne_sample.json'
ACCEPTED_CSV = RESULTS_DIR / 'no_go_accepted_provisional.csv'

OUT_CSV = RESULTS_DIR / 'pilot_A_vs_B_full_aggregation_no_go_accepted.csv'
OUT_MD = RESULTS_DIR / 'pilot_comparative_report_A_vs_B_no_go_accepted.md'
OUT_PLOT = RESULTS_DIR / 'pilot_A_vs_B_full_boxplot_no_go_accepted.png'
OUT_TRACE = RESULTS_DIR / 'pilot_mapping_trace_no_go_accepted.csv'


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


def read_accepted(accepted_csv):
    mapping = {}
    if not accepted_csv.exists():
        return mapping
    df = pd.read_csv(accepted_csv, dtype=str).fillna("")
    for _, row in df.iterrows():
        tag = row.get('tag', '')
        dataset = row.get('dataset', '')
        stats_path = row.get('stats_path', '')
        if not stats_path:
            # try local stats file
            candidate = RESULTS_DIR / f"{tag}_stats.csv"
            if candidate.exists():
                stats_path = str(candidate)
        # normalize path
        stats_p = Path(stats_path) if stats_path else None
        if stats_p and not stats_p.is_absolute():
            stats_p = RESULTS_DIR / stats_p
        method_medians = {}
        if stats_p and stats_p.exists():
            try:
                sdf = pd.read_csv(stats_p)
                # prefer mae_median, fallback mae_mean
                if 'method' in sdf.columns and 'mae_median' in sdf.columns:
                    for _, r in sdf.iterrows():
                        try:
                            val = float(r['mae_median'])
                            method_medians[str(r['method'])] = val
                        except Exception:
                            continue
                elif 'method' in sdf.columns and 'mae_mean' in sdf.columns:
                    for _, r in sdf.iterrows():
                        try:
                            val = float(r['mae_mean'])
                            method_medians[str(r['method'])] = val
                        except Exception:
                            continue
            except Exception:
                pass
        mapping[(tag, dataset)] = {'method_medians': method_medians, 'stats_path': str(stats_p) if stats_p else ''}
    return mapping


def collect_group_values(schedule_seq, mapping, group_label=None):
    methods_values = {}
    missing = []
    trace_rows = []
    for entry in schedule_seq:
        tag = entry['tag']
        dataset = entry['dataset']
        key = (tag, dataset)
        entry_map = None
        match_type = 'none'
        if key in mapping and mapping[key].get('method_medians'):
            entry_map = mapping[key]
            match_type = 'exact'
        else:
            # try looser match: same tag
            for (t, d), v in mapping.items():
                if t == tag and v.get('method_medians'):
                    entry_map = v
                    match_type = 'tag_fallback'
                    break
        stats_path = ''
        mm = {}
        if entry_map is None:
            missing.append((tag, dataset))
        else:
            mm = entry_map.get('method_medians', {})
            stats_path = entry_map.get('stats_path', '')
            if not mm:
                missing.append((tag, dataset))
        trace_rows.append({'group': group_label or '', 'tag': tag, 'dataset': dataset, 'match_type': match_type, 'used_stats_path': stats_path, 'used_method_count': len(mm)})
        for m, val in mm.items():
            if isinstance(val, (int, float)) and (not math.isnan(val)):
                methods_values.setdefault(m, []).append(val)
    return methods_values, missing, trace_rows


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
    mapping = read_accepted(ACCEPTED_CSV)
    scheduleA = load_schedule(SCHEDULE_A)
    scheduleB = load_schedule(SCHEDULE_B)
    A_vals, A_missing, A_trace = collect_group_values(scheduleA, mapping, group_label='A')
    B_vals, B_missing, B_trace = collect_group_values(scheduleB, mapping, group_label='B')
    # write mapping trace for inspection
    trace_all = A_trace + B_trace
    try:
        tdf = pd.DataFrame(trace_all)
        tdf.to_csv(OUT_TRACE, index=False)
        unique_stats = sorted([p for p in set([r.get('used_stats_path', '') for r in trace_all]) if p])
        print(f'Wrote trace file: {OUT_TRACE} (unique stats files used: {len(unique_stats)})')
    except Exception as _:
        print('Could not write mapping trace file')
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

    with open(OUT_MD, 'w', encoding='utf-8') as f:
        f.write('# Phase A vs Phase B comparison (using provisional accepted NO-GO runs)\n\n')
        f.write('Generated automatically.\n\n')
        f.write(f'Accepted runs provided by: {ACCEPTED_CSV}\n\n')
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
    plt.title('Phase A vs Phase B MAE per method (accepted NO-GO)')
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
