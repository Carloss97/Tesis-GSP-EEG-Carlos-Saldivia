#!/usr/bin/env python3
"""Export significant combinations to XLSX and generate visualizations.

Outputs:
 - results/analysis/batches/significant_combinations.xlsx
 - results/analysis/batches/figures/significant_best_method_counts.png
 - results/analysis/batches/figures/significant_heatmap_graph_dataset.png
"""
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys


def safe_bool_series(s):
    return s.astype(str).str.lower().isin(["true", "1"]) if s is not None else pd.Series(False)


def autofit_columns(worksheet, df):
    for i, col in enumerate(df.columns):
        try:
            col_vals = df[col].astype(str)
            maxlen = max(col_vals.map(len).max(), len(str(col)))
            width = min(60, maxlen + 2)
            worksheet.set_column(i, i, width)
        except Exception:
            try:
                worksheet.set_column(i, i, max(10, len(str(col)) + 2))
            except Exception:
                pass
    try:
        worksheet.freeze_panes(1, 0)
    except Exception:
        pass


def main():
    script_path = Path(__file__).resolve()
    root = script_path.parent.parent
    batches_dir = root / 'results' / 'analysis' / 'batches'
    if not batches_dir.exists():
        print('Batches dir not found:', batches_dir, file=sys.stderr)
        sys.exit(1)

    in_csv = batches_dir / 'best_method_by_combo_stats.csv'
    if not in_csv.exists():
        print('Input CSV missing:', in_csv, file=sys.stderr)
        sys.exit(1)

    df = pd.read_csv(in_csv)

    # determine significance mask
    sig_mask = safe_bool_series(df.get('significant'))
    try:
        p_adj = pd.to_numeric(df.get('p_adj'), errors='coerce')
        sig_mask = sig_mask | (p_adj < 0.05)
    except Exception:
        pass

    sig_df = df[sig_mask].copy()

    out_xlsx = batches_dir / 'significant_combinations.xlsx'
    fig_dir = batches_dir / 'figures'
    fig_dir.mkdir(parents=True, exist_ok=True)

    # write xlsx with sheets: significant, counts_by_method, pivot_graph_dataset_counts
    with pd.ExcelWriter(out_xlsx, engine='xlsxwriter') as writer:
        workbook = writer.book

        sig_df.to_excel(writer, sheet_name='significant', index=False)
        ws = writer.sheets['significant']
        autofit_columns(ws, sig_df)

        # counts by best_method
        counts = sig_df['best_method'].value_counts().rename_axis('best_method').reset_index(name='count')
        counts.to_excel(writer, sheet_name='counts_by_method', index=False)
        ws2 = writer.sheets['counts_by_method']
        autofit_columns(ws2, counts)

        # pivot graph x dataset counts
        try:
            pivot = sig_df.pivot_table(index='graph', columns='dataset', values='best_method', aggfunc='count', fill_value=0)
            pivot.to_excel(writer, sheet_name='pivot_graph_dataset_counts')
            ws3 = writer.sheets['pivot_graph_dataset_counts']
            # pivot has MultiIndex columns if any; convert to str df for width sizing
            pivot_df = pivot.reset_index()
            autofit_columns(ws3, pivot_df)
        except Exception as e:
            print('Could not create pivot:', e, file=sys.stderr)

    print(f'Wrote {out_xlsx}')

    # Generate bar chart of counts
    if len(counts):
        plt.figure(figsize=(10, 6))
        sns.barplot(data=counts, x='count', y='best_method', palette='viridis')
        plt.title('Significant combinations: best_method counts')
        plt.tight_layout()
        bar_out = fig_dir / 'significant_best_method_counts.png'
        plt.savefig(bar_out, dpi=150)
        plt.close()
        print(f'Wrote {bar_out}')

    # Generate heatmap for pivot
    try:
        pivot = sig_df.pivot_table(index='graph', columns='dataset', values='best_method', aggfunc='count', fill_value=0)
        if pivot.size > 0:
            plt.figure(figsize=(max(8, pivot.shape[1] * 0.6), max(6, pivot.shape[0] * 0.25)))
            sns.heatmap(pivot, annot=True, fmt='d', cmap='coolwarm', cbar_kws={'label': 'significant_count'})
            plt.title('Significant combos count per graph × dataset')
            plt.tight_layout()
            heat_out = fig_dir / 'significant_heatmap_graph_dataset.png'
            plt.savefig(heat_out, dpi=150)
            plt.close()
            print(f'Wrote {heat_out}')
    except Exception as e:
        print('Could not generate heatmap:', e, file=sys.stderr)


if __name__ == '__main__':
    main()
