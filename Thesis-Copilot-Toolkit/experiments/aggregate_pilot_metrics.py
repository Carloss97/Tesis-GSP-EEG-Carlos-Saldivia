#!/usr/bin/env python3
"""Aggregate pilot metrics for Phase A vs Phase B and compute Mann-Whitney U tests.

Writes:
- results/pilot_A_vs_B_aggregation.csv
- results/pilot_A_vs_B_boxplot.png
- appends summary to results/pilot_comparative_report_A_vs_B.md

Run: python experiments/aggregate_pilot_metrics.py
"""

import os
import sys
import math
import json
import argparse
import pandas as pd
import numpy as np
from scipy.stats import mannwhitneyu

try:
    import seaborn as sns
    import matplotlib.pyplot as plt
    matplotlib_available = True
except Exception:
    import matplotlib.pyplot as plt
    sns = None
    matplotlib_available = True


PHASE_A = ["it01", "it02", "it03", "it05", "it06", "it09", "it10"]
PHASE_B = ["it01", "it04", "it07", "it11", "it14", "it17"]

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
RESULTS = os.path.join(ROOT, 'results')

def find_stats_path(tag):
    # common pattern: results/itXX_stats.csv
    candidates = [
        os.path.join(RESULTS, f"{tag}_stats.csv"),
        os.path.join(RESULTS, f"{tag}_mne_sample_stats.csv"),
    ]
    for p in candidates:
        if os.path.exists(p):
            return p
    return None

def read_stats(tag):
    p = find_stats_path(tag)
    if p is None:
        print(f"[WARN] stats CSV not found for {tag}", file=sys.stderr)
        return None
    try:
        df = pd.read_csv(p)
        if 'method' in df.columns and 'mae_median' in df.columns:
            return df[['method','mae_median']]
        else:
            print(f"[WARN] unexpected columns in {p}: {df.columns.tolist()}", file=sys.stderr)
            return None
    except Exception as e:
        print(f"[ERROR] reading {p}: {e}", file=sys.stderr)
        return None

def collect(phase_tags, phase_label):
    rows = []
    for tag in phase_tags:
        df = read_stats(tag)
        if df is None:
            continue
        for _, r in df.iterrows():
            try:
                val = float(r['mae_median'])
            except Exception:
                val = math.nan
            rows.append({'method': r['method'], 'it': tag, 'phase': phase_label, 'mae_median': val})
    return pd.DataFrame(rows)

def main():
    parser = argparse.ArgumentParser(description="Aggregate pilot metrics for Phase A vs B")
    parser.add_argument("--phase-a-schedule", type=str, default=None, help="Path to Phase A schedule JSON (will extract iteration keys)")
    parser.add_argument("--phase-b-schedule", type=str, default=None, help="Path to Phase B schedule JSON (will extract iteration keys)")
    args = parser.parse_args()

    a_tags = PHASE_A
    b_tags = PHASE_B
    if args.phase_a_schedule and os.path.exists(args.phase_a_schedule):
        try:
            with open(args.phase_a_schedule, 'r', encoding='utf-8') as fh:
                sched = json.load(fh)
            a_tags = [it.get('key') for it in sched.get('iterations', []) if it.get('key')]
            print(f"Using Phase A tags from: {args.phase_a_schedule}")
        except Exception as e:
            print(f"[WARN] could not read Phase A schedule: {e}", file=sys.stderr)
    if args.phase_b_schedule and os.path.exists(args.phase_b_schedule):
        try:
            with open(args.phase_b_schedule, 'r', encoding='utf-8') as fh:
                sched = json.load(fh)
            b_tags = [it.get('key') for it in sched.get('iterations', []) if it.get('key')]
            print(f"Using Phase B tags from: {args.phase_b_schedule}")
        except Exception as e:
            print(f"[WARN] could not read Phase B schedule: {e}", file=sys.stderr)

    dfA = collect(a_tags, 'A')
    dfB = collect(b_tags, 'B')
    df = pd.concat([dfA, dfB], ignore_index=True)
    if df.empty:
        print("No data collected. Aborting.")
        return 1

    methods = sorted(df['method'].unique())
    out_rows = []
    for m in methods:
        a = df[(df.method==m)&(df.phase=='A')]['mae_median'].dropna().values
        b = df[(df.method==m)&(df.phase=='B')]['mae_median'].dropna().values
        medA = float(np.median(a)) if len(a)>0 else float('nan')
        medB = float(np.median(b)) if len(b)>0 else float('nan')
        nA = int(len(a))
        nB = int(len(b))
        if nA>=2 and nB>=2:
            try:
                U, p = mannwhitneyu(a, b, alternative='two-sided')
            except Exception as e:
                U, p = float('nan'), float('nan')
        else:
            U, p = float('nan'), float('nan')
        signif = (not math.isnan(p)) and (p < 0.05)
        out_rows.append({
            'method': m,
            'median_A': medA,
            'median_B': medB,
            'n_A': nA,
            'n_B': nB,
            'U': U,
            'p_value': p,
            'significant': signif,
        })

    out_df = pd.DataFrame(out_rows)
    csv_out = os.path.join(RESULTS, 'pilot_A_vs_B_aggregation.csv')
    out_df.to_csv(csv_out, index=False)
    print(f"Wrote aggregation CSV: {csv_out}")

    # boxplot
    try:
        plt.figure(figsize=(10,6))
        if sns is not None:
            sns.boxplot(data=df, x='method', y='mae_median', hue='phase')
        else:
            # fallback: plot separate boxplots
            methods_sorted = methods
            data_to_plot = []
            labels = []
            for m in methods_sorted:
                data_to_plot.append(df[(df.method==m)&(df.phase=='A')]['mae_median'].dropna().values)
                labels.append(f"{m}-A")
                data_to_plot.append(df[(df.method==m)&(df.phase=='B')]['mae_median'].dropna().values)
                labels.append(f"{m}-B")
            plt.boxplot(data_to_plot)
            plt.xticks(range(1, len(labels)+1), labels, rotation=45)
        plt.xticks(rotation=45)
        plt.tight_layout()
        fig_out = os.path.join(RESULTS, 'pilot_A_vs_B_boxplot.png')
        plt.savefig(fig_out, dpi=200)
        plt.close()
        print(f"Wrote boxplot: {fig_out}")
    except Exception as e:
        print(f"[WARN] could not create plot: {e}", file=sys.stderr)

    # append summary to markdown report
    md_path = os.path.join(RESULTS, 'pilot_comparative_report_A_vs_B.md')
    try:
        with open(md_path, 'a', encoding='utf-8') as f:
            f.write('\n## Aggregated statistics (automatically computed)\n\n')
            f.write('Method | median(A) | median(B) | n(A) | n(B) | U | p-value | significant\n')
            f.write('---|---:|---:|---:|---:|---:|---:|---\n')
            for r in out_rows:
                pval = r['p_value']
                pstr = f"{pval:.3e}" if (not math.isnan(pval)) else "NA"
                Ustr = f"{r['U']:.3f}" if (not math.isnan(r['U'])) else "NA"
                medA = f"{r['median_A']:.6e}" if (not math.isnan(r['median_A'])) else "NA"
                medB = f"{r['median_B']:.6e}" if (not math.isnan(r['median_B'])) else "NA"
                sig = 'YES' if r['significant'] else ''
                f.write(f"{r['method']} | {medA} | {medB} | {r['n_A']} | {r['n_B']} | {Ustr} | {pstr} | {sig}\n")
            # highlight significant methods
            significant_methods = [r['method'] for r in out_rows if r['significant']]
            f.write('\n')
            if significant_methods:
                f.write('**Significant differences (p < 0.05)**: ' + ', '.join(significant_methods) + '\n')
            else:
                f.write('No statistically significant differences found (p < 0.05).\n')
        print(f"Appended summary to {md_path}")
    except Exception as e:
        print(f"[WARN] could not update markdown: {e}", file=sys.stderr)

    return 0

if __name__ == '__main__':
    sys.exit(main())
