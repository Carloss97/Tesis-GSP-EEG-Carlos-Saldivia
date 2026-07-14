#!/usr/bin/env python3
"""
Select best method per combination (graph, dataset, missing_ratio).

Outputs:
- results/analysis/batches/best_method_by_combo.csv
- results/analysis/batches/best_method_counts.csv
- results/analysis/batches/pivot_best_method_by_graph_counts.csv
- results/analysis/batches/figures/heatmap_best_method_by_graph_counts.png
- results/analysis/batches/figures/top_best_methods_overall.png

The script reads `global_by_combo.csv` (preferred) or falls back to
`consolidated_all_batches.csv` if needed.
"""
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
import argparse
import sys


def read_csv_safe(path: Path):
    if not path.exists():
        print(f"Missing file: {path}", file=sys.stderr)
        return None
    try:
        return pd.read_csv(path)
    except Exception as e:
        print(f"Error reading {path}: {e}", file=sys.stderr)
        return None


def parse_combo_column(df: pd.DataFrame):
    # Expect a column named 'combo' with format method|graph|dataset|missing_ratio
    if 'combo' not in df.columns:
        return df
    parts = df['combo'].astype(str).str.split('|', n=3, expand=True)
    if parts.shape[1] >= 4:
        df = df.copy()
        df['method'] = parts[0].str.strip()
        df['graph'] = parts[1].str.strip()
        df['dataset'] = parts[2].str.strip()
        df['missing_ratio'] = parts[3].str.strip()
    else:
        print('Could not parse combo into 4 parts; leaving original dataframe', file=sys.stderr)
    return df


def ensure_numeric(df: pd.DataFrame, cols):
    for c in cols:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors='coerce')


def main():
    parser = argparse.ArgumentParser(description='Generate best-method-by-combo tables and plots')
    parser.add_argument('--batches-dir', default=None, help='Path to results/analysis/batches')
    args = parser.parse_args()

    script_path = Path(__file__).resolve()
    root = script_path.parent.parent
    default_batches = root / 'results' / 'analysis' / 'batches'
    batches_dir = Path(args.batches_dir) if args.batches_dir else default_batches
    if not batches_dir.exists():
        print(f'Batches dir not found: {batches_dir}', file=sys.stderr)
        sys.exit(1)

    fig_dir = batches_dir / 'figures'
    fig_dir.mkdir(parents=True, exist_ok=True)

    f_combo = batches_dir / 'global_by_combo.csv'
    f_cons = batches_dir / 'consolidated_all_batches.csv'

    df = None
    if f_combo.exists():
        df = read_csv_safe(f_combo)
    elif f_cons.exists():
        df = read_csv_safe(f_cons)
    else:
        print('No input CSV found (global_by_combo.csv or consolidated_all_batches.csv)', file=sys.stderr)
        sys.exit(1)

    if df is None or df.empty:
        print('Input dataframe is empty or unreadable', file=sys.stderr)
        sys.exit(1)

    df = parse_combo_column(df)
    # Normalize expected numeric columns
    ensure_numeric(df, ['mean_mae', 'median_mae', 'count'])
    # missing_ratio might be string '0.1' etc.
    if 'missing_ratio' in df.columns:
        df['missing_ratio'] = pd.to_numeric(df['missing_ratio'], errors='coerce')

    # Check we have necessary columns
    required = ['method', 'graph', 'dataset', 'missing_ratio', 'mean_mae']
    if not all(c in df.columns for c in required):
        print(f'Missing required columns. Found: {list(df.columns)}', file=sys.stderr)
        sys.exit(1)

    group_cols = ['graph', 'dataset', 'missing_ratio']

    rows = []
    for keys, grp in df.groupby(group_cols):
        g, d, m = keys
        grp_sorted = grp.sort_values('mean_mae', na_position='last')
        best = grp_sorted.iloc[0]
        second = grp_sorted.iloc[1] if len(grp_sorted) > 1 else None
        row = {
            'graph': g,
            'dataset': d,
            'missing_ratio': m,
            'best_method': best.get('method'),
            'best_mean_mae': float(best.get('mean_mae')) if pd.notna(best.get('mean_mae')) else np.nan,
            'best_median_mae': float(best.get('median_mae')) if 'median_mae' in best and pd.notna(best.get('median_mae')) else np.nan,
            'best_count': int(best.get('count')) if 'count' in best and pd.notna(best.get('count')) else np.nan,
            'n_methods': int(len(grp_sorted)),
        }
        if second is not None:
            row['second_mean_mae'] = float(second.get('mean_mae')) if pd.notna(second.get('mean_mae')) else np.nan
            row['delta_to_second'] = float(second.get('mean_mae') - best.get('mean_mae')) if pd.notna(second.get('mean_mae')) and pd.notna(best.get('mean_mae')) else np.nan
            row['second_method'] = second.get('method')
        else:
            row['second_mean_mae'] = np.nan
            row['delta_to_second'] = np.nan
            row['second_method'] = None
        rows.append(row)

    best_df = pd.DataFrame(rows)
    out_best = batches_dir / 'best_method_by_combo.csv'
    best_df.to_csv(out_best, index=False)
    print(f'Wrote {out_best}')

    # Counts per method
    counts = best_df['best_method'].value_counts().reset_index()
    counts.columns = ['method', 'best_count']
    out_counts = batches_dir / 'best_method_counts.csv'
    counts.to_csv(out_counts, index=False)
    print(f'Wrote {out_counts}')

    # Pivot method x graph counts
    pivot = pd.crosstab(best_df['best_method'], best_df['graph'])
    out_pivot = batches_dir / 'pivot_best_method_by_graph_counts.csv'
    pivot.to_csv(out_pivot)
    print(f'Wrote {out_pivot}')

    # Heatmap of pivot
    try:
        plt.figure(figsize=(max(6, pivot.shape[1] * 0.6), max(6, pivot.shape[0] * 0.3)))
        sns.heatmap(pivot, cmap='magma', linewidths=0.5, linecolor='gray', cbar_kws={'label': 'best-counts'})
        plt.title('Counts of being best: method × graph')
        plt.tight_layout()
        out_heat = fig_dir / 'heatmap_best_method_by_graph_counts.png'
        plt.savefig(out_heat, dpi=200)
        plt.close()
        print(f'Wrote {out_heat}')
    except Exception as e:
        print('Error creating heatmap: ', e, file=sys.stderr)

    # Bar plot of top methods overall
    try:
        topn = counts.sort_values('best_count', ascending=False).head(20)
        plt.figure(figsize=(8, max(4, len(topn) * 0.25)))
        sns.barplot(y='method', x='best_count', data=topn, palette='tab10')
        plt.title('Top methods by best-combo counts')
        plt.tight_layout()
        out_bar = fig_dir / 'top_best_methods_overall.png'
        plt.savefig(out_bar, dpi=200)
        plt.close()
        print(f'Wrote {out_bar}')
    except Exception as e:
        print('Error creating bar plot: ', e, file=sys.stderr)

    print('Done.')


if __name__ == '__main__':
    main()
