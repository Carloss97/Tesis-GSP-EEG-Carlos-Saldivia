#!/usr/bin/env python3
"""Generate human-readable files summarizing the best methods per combination.

Outputs (saved to results/analysis/batches/):
- top_method_counts.csv
- top20_delta_combos.csv
- best_by_combo_sorted.csv
- significant_combinations.csv (if not already present, overwritten)
- readable_best_summary.txt
"""
from pathlib import Path
import pandas as pd
import sys


def main():
    script_path = Path(__file__).resolve()
    root = script_path.parent.parent
    batches = root / 'results' / 'analysis' / 'batches'
    if not batches.exists():
        print('Batches dir not found:', batches, file=sys.stderr)
        sys.exit(1)

    candidates = [batches / 'best_method_by_combo_stats.csv', batches / 'best_method_by_combo.csv']
    infile = None
    for c in candidates:
        if c.exists():
            infile = c
            break
    if infile is None:
        print('No input best_method_by_combo CSV found in', batches, file=sys.stderr)
        sys.exit(1)

    df = pd.read_csv(infile)

    # Ensure numeric columns
    df['delta_mean'] = pd.to_numeric(df.get('delta_mean'), errors='coerce')
    df['p_adj'] = pd.to_numeric(df.get('p_adj'), errors='coerce')

    # Normalize significant column if present
    if 'significant' in df.columns:
        try:
            if df['significant'].dtype == object:
                df['significant'] = df['significant'].astype(str).str.lower().isin(['true', '1', 'yes'])
            else:
                df['significant'] = df['significant'].astype(bool)
        except Exception:
            df['significant'] = False
    else:
        df['significant'] = False

    # top method counts
    counts = df['best_method'].value_counts().rename_axis('best_method').reset_index(name='count')
    out_counts = batches / 'top_method_counts.csv'
    counts.to_csv(out_counts, index=False)

    # significant combinations (p_adj < 0.05 OR significant flag)
    sig_mask = (df['significant'] == True) | (df['p_adj'] < 0.05)
    sig_df = df[sig_mask].copy()
    out_sig = batches / 'significant_combinations.csv'
    sig_df.to_csv(out_sig, index=False)

    # top delta combos (highest difference between second and best)
    topdelta = df.dropna(subset=['delta_mean']).sort_values('delta_mean', ascending=False)
    out_topdelta = batches / 'top20_delta_combos.csv'
    topdelta.head(20).to_csv(out_topdelta, index=False)

    # full sorted best_by_combo
    sorted_df = df.sort_values(['best_method', 'dataset', 'graph', 'missing_ratio'])
    out_sorted = batches / 'best_by_combo_sorted.csv'
    sorted_df.to_csv(out_sorted, index=False)

    # human-readable text summary
    out_txt = batches / 'readable_best_summary.txt'
    with out_txt.open('w', encoding='utf-8') as fh:
        fh.write(f'Input file: {infile.name}\n')
        fh.write(f'Total combinations: {len(df)}\n')
        fh.write(f'Significant combinations: {len(sig_df)}\n\n')
        fh.write('Top methods by count:\n')
        for _, r in counts.head(20).iterrows():
            fh.write(f"- {r['best_method']}: {r['count']}\n")
        fh.write('\nTop 10 combos by delta_mean (second_mean - best_mean):\n')
        for _, r in topdelta.head(10).iterrows():
            gm = r.get('graph', '')
            ds = r.get('dataset', '')
            mr = r.get('missing_ratio', '')
            fh.write(f"- {gm} | {ds} | {mr} -> {r.get('best_method')} (delta={r.get('delta_mean')})\n")

    print('Wrote:', out_counts)
    print('Wrote:', out_sig)
    print('Wrote:', out_topdelta)
    print('Wrote:', out_sorted)
    print('Wrote:', out_txt)


if __name__ == '__main__':
    main()
