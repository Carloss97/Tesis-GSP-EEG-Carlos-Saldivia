#!/usr/bin/env python3
import os
import re
import pandas as pd
import numpy as np
from datetime import datetime


def extract_iteration_from_text(s):
    if s is None:
        return None
    try:
        m = re.search(r"\bit[_-]?(\d{1,5})\b", s, flags=re.IGNORECASE)
        if m:
            return int(m.group(1))
        m = re.search(r"it(\d{1,5})", s, flags=re.IGNORECASE)
        if m:
            return int(m.group(1))
    except Exception:
        return None
    return None


def df_to_md(df):
    # Simple Markdown table without external deps
    if df is None or df.empty:
        return "(empty)"
    headers = list(df.columns)
    lines = []
    lines.append("|" + "|".join(headers) + "|")
    lines.append("|" + "|".join(["---"] * len(headers)) + "|")
    for _, row in df.iterrows():
        vals = [str(x) for x in row.tolist()]
        lines.append("|" + "|".join(vals) + "|")
    return "\n".join(lines)


def safe_write_csv(df, path):
    try:
        df.to_csv(path, index=False)
    except Exception as e:
        print('Failed to write', path, e)


def main():
    script_dir = os.path.dirname(__file__)
    out_dir = os.path.normpath(os.path.join(script_dir, '..', 'results', 'analysis', 'batches'))
    consolidated = os.path.join(out_dir, 'consolidated_all_batches.csv')
    if not os.path.exists(consolidated):
        print('Consolidated file not found:', consolidated)
        return 1

    print('Reading', consolidated)
    df = pd.read_csv(consolidated, low_memory=False)

    # Ensure numeric columns
    for c in ['mae', 'rmse', 'dtw', 'snr', 'missing_ratio']:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors='coerce')

    # Extract iteration if present in source_file or block
    df['iteration'] = df.apply(lambda r: extract_iteration_from_text(str(r.get('source_file','')) + ' ' + str(r.get('block',''))), axis=1)

    # Normalize columns existence
    if 'graph' not in df.columns:
        df['graph'] = 'None'
    df['graph'] = df['graph'].fillna('None').astype(str)
    df['method'] = df['method'].astype(str)
    df['dataset'] = df['dataset'].astype(str)
    df['scenario'] = df['scenario'].astype(str)

    # Combo key
    df['combo'] = df['method'] + '|' + df['graph'] + '|' + df['dataset'] + '|' + df['missing_ratio'].astype(str)

    aggregations = [
        (['method'], 'global_by_method.csv'),
        (['graph'], 'global_by_graph.csv'),
        (['dataset'], 'global_by_dataset.csv'),
        (['scenario'], 'global_by_scenario.csv'),
        (['iteration'], 'global_by_iteration.csv'),
        (['missing_ratio'], 'global_by_missing_ratio.csv'),
        (['combo'], 'global_by_combo.csv'),
        (['method','graph'], 'global_by_method_graph.csv'),
    ]

    for groupcols, fname in aggregations:
        cols_present = [c for c in groupcols if c in df.columns]
        if not cols_present:
            continue
        g = df.groupby(cols_present).agg(
            count = ('mae','count'),
            mean_mae = ('mae','mean'),
            std_mae = ('mae','std'),
            median_mae = ('mae','median'),
            mean_rmse = ('rmse','mean'),
            mean_dtw = ('dtw','mean'),
            mean_snr = ('snr','mean'),
        ).reset_index()
        outpath = os.path.join(out_dir, fname)
        safe_write_csv(g, outpath)
        print('Wrote', outpath)

    # Pivot: method by graph (mean mae)
    try:
        pivot = df.pivot_table(index='graph', columns='method', values='mae', aggfunc='mean')
        pivot.to_csv(os.path.join(out_dir, 'pivot_method_by_graph.csv'))
        print('Wrote pivot_method_by_graph.csv')
    except Exception as e:
        print('Pivot failed:', e)

    # Top-3 per block (count how often each method appears in top-3 by mean MAE within the block)
    top3_counts = {}
    if 'block' in df.columns:
        blocks = df['block'].dropna().unique()
        for b in blocks:
            sub = df[df['block']==b]
            if sub.empty:
                continue
            m = sub.groupby('method')['mae'].mean().sort_values()
            top3 = m.index[:3].tolist()
            for method in top3:
                top3_counts[method] = top3_counts.get(method, 0) + 1
    top3_df = pd.DataFrame(list(top3_counts.items()), columns=['method','top3_block_count']).sort_values('top3_block_count', ascending=False)
    safe_write_csv(top3_df, os.path.join(out_dir, 'top3_by_block_counts.csv'))
    print('Wrote top3_by_block_counts.csv')

    # Top-3 by dataset
    top3_ds = {}
    for ds in df['dataset'].dropna().unique():
        sub = df[df['dataset']==ds]
        if sub.empty:
            continue
        m = sub.groupby('method')['mae'].mean().sort_values()
        top3 = m.index[:3].tolist()
        for method in top3:
            top3_ds[method] = top3_ds.get(method,0) + 1
    top3_ds_df = pd.DataFrame(list(top3_ds.items()), columns=['method','top3_dataset_count']).sort_values('top3_dataset_count', ascending=False)
    safe_write_csv(top3_ds_df, os.path.join(out_dir, 'top3_by_dataset_counts.csv'))
    print('Wrote top3_by_dataset_counts.csv')

    # Overall ranking
    overall = df.groupby('method')['mae'].agg(['count','mean','std','median']).sort_values('mean').reset_index()
    safe_write_csv(overall, os.path.join(out_dir,'overall_method_ranking.csv'))
    print('Wrote overall_method_ranking.csv')

    # Markdown summary
    md_lines = []
    md_lines.append('# Resumen global de métodos\n')
    md_lines.append('Generado: ' + datetime.utcnow().isoformat() + 'Z\n')
    md_lines.append('## Top métodos (por media MAE)\n')
    md_lines.append(df_to_md(overall.head(10)))
    md_lines.append('\n## Top-3 apariciones por bloque\n')
    md_lines.append(df_to_md(top3_df))
    md_lines.append('\n## Top-3 apariciones por dataset\n')
    md_lines.append(df_to_md(top3_ds_df))

    with open(os.path.join(out_dir,'global_summary.md'), 'w', encoding='utf-8') as f:
        f.write('\n\n'.join(md_lines))
    print('Wrote global_summary.md')
    print('Done')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
