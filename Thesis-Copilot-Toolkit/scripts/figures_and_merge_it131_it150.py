#!/usr/bin/env python3
"""
Generate boxplots and heatmap for it131-it150 and merge pages into the
global report PDF (if present).

Outputs:
 - results/analysis/batches/it131_it150_figures.pdf
 - results/analysis/batches/report_summary_updated_it131_it150.pdf (if merge succeeds)
"""
import sys
from pathlib import Path
import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

try:
    import seaborn as sns
    sns.set(style='whitegrid')
except Exception:
    sns = None

# Try to import PDF merger
PdfReader = None
PdfWriter = None
try:
    from PyPDF2 import PdfReader, PdfWriter
except Exception:
    try:
        from pypdf import PdfReader, PdfWriter
    except Exception:
        PdfReader = None
        PdfWriter = None

BASE = Path(__file__).resolve().parents[1] / 'results'
BATCH_DIR = BASE / 'analysis' / 'batches'
BATCH_DIR.mkdir(parents=True, exist_ok=True)
FIG_PDF = BATCH_DIR / 'it131_it150_figures.pdf'
UPDATED_PDF = BATCH_DIR / 'report_summary_updated_it131_it150.pdf'
EXISTING_PDF = BATCH_DIR / 'report_summary.pdf'

# collect raw files it131..it150
pattern = re.compile(r'it(\d+)_.*_raw\.csv')
raw_files = []
for p in sorted(BASE.glob('it*_raw.csv')):
    m = pattern.match(p.name)
    if not m:
        continue
    itn = int(m.group(1))
    if 131 <= itn <= 150:
        raw_files.append((itn, p))

if not raw_files:
    print('No raw files found for it131..it150 in', BASE)
    sys.exit(1)

# read and concat
dfs = []
for itn, p in raw_files:
    try:
        d = pd.read_csv(p)
        d['it_num'] = itn
        # keep source filename for traceability
        d['source_file'] = p.name
        dfs.append(d)
    except Exception as e:
        print('Failed reading', p, e)

if not dfs:
    print('No dataframes loaded, aborting')
    sys.exit(1)

all_df = pd.concat(dfs, ignore_index=True)

# pick metric
metric_candidates = ['mae', 'MAE', 'error', 'rmse']
metric = None
for c in metric_candidates:
    if c in all_df.columns:
        metric = c
        break
if metric is None:
    # fallback to first numeric column
    num_cols = all_df.select_dtypes(include=[np.number]).columns.tolist()
    metric = num_cols[0] if num_cols else None
if metric is None:
    print('No numeric metric found to plot')
    sys.exit(1)

print('Using metric:', metric)

# normalize string columns
for col in ['dataset', 'graph', 'method']:
    if col in all_df.columns:
        all_df[col] = all_df[col].astype(str)
    else:
        all_df[col] = ''

if 'missing_ratio' in all_df.columns:
    all_df['missing_ratio'] = all_df['missing_ratio'].astype(str)
    all_df['combo_key'] = all_df['dataset'] + '|' + all_df['graph'] + '|' + all_df['method'] + '|mr=' + all_df['missing_ratio']
else:
    all_df['combo_key'] = all_df['dataset'] + '|' + all_df['graph'] + '|' + all_df['method']

# create figures and save to a single PDF
with PdfPages(str(FIG_PDF)) as pp:
    # 1) Boxplot by method
    plt.figure(figsize=(10, 6))
    try:
        if sns is not None:
            ax = sns.boxplot(x='method', y=metric, data=all_df)
        else:
            ax = plt.gca()
            unique_methods = sorted(all_df['method'].unique())
            data_to_plot = [all_df.loc[all_df['method'] == m, metric].dropna().values for m in unique_methods]
            ax.boxplot(data_to_plot)
            ax.set_xticks(range(1, len(unique_methods) + 1))
            ax.set_xticklabels(unique_methods, rotation=45)
    except Exception as e:
        print('Boxplot by method failed:', e)
    plt.title('Distribution of ' + metric + ' by method (it131-it150)')
    plt.tight_layout()
    pp.savefig()
    plt.close()

    # 2) Boxplots for top-10 best combos (by mean)
    grp = all_df.groupby('combo_key')[metric].mean().sort_values()
    top10 = list(grp.head(10).index)
    if top10:
        sub = all_df[all_df['combo_key'].isin(top10)].copy()
        sub['combo_short'] = sub['combo_key'].str.replace('\|', ' / ', regex=False)
        plt.figure(figsize=(12, 6))
        try:
            if sns is not None:
                sns.boxplot(x='combo_short', y=metric, data=sub)
            else:
                unique_combo = list(sub['combo_short'].unique())
                data_to_plot = [sub.loc[sub['combo_short'] == c, metric].dropna().values for c in unique_combo]
                plt.boxplot(data_to_plot)
                plt.xticks(range(1, len(unique_combo) + 1), unique_combo, rotation=45)
        except Exception as e:
            print('Boxplot top10 failed:', e)
        plt.title('Top 10 combos by mean ' + metric)
        plt.xticks(rotation=45)
        plt.tight_layout()
        pp.savefig()
        plt.close()

    # 3) Boxplots for top-10 worst combos
    worst10 = list(grp.tail(10).index)
    if worst10:
        subw = all_df[all_df['combo_key'].isin(worst10)].copy()
        subw['combo_short'] = subw['combo_key'].str.replace('|', ' / ', regex=False)
        plt.figure(figsize=(12, 6))
        try:
            if sns is not None:
                sns.boxplot(x='combo_short', y=metric, data=subw)
            else:
                unique_combo = list(subw['combo_short'].unique())
                data_to_plot = [subw.loc[subw['combo_short'] == c, metric].dropna().values for c in unique_combo]
                plt.boxplot(data_to_plot)
                plt.xticks(range(1, len(unique_combo) + 1), unique_combo, rotation=45)
        except Exception as e:
            print('Boxplot worst10 failed:', e)
        plt.title('Worst 10 combos by mean ' + metric)
        plt.xticks(rotation=45)
        plt.tight_layout()
        pp.savefig()
        plt.close()

    # 4) Heatmap of delta_mean from comparison CSV if available
    comp_csv = BATCH_DIR / 'it131_it150_vs_it120_comparison.csv'
    if comp_csv.exists():
        try:
            comp = pd.read_csv(comp_csv)
            # expect combo_key and delta_mean
            if 'combo_key' in comp.columns:
                def parse_key(k):
                    parts = k.split('|')
                    ds = parts[0] if len(parts) > 0 else ''
                    gr = parts[1] if len(parts) > 1 else ''
                    me = parts[2] if len(parts) > 2 else ''
                    return ds, gr, me
                comp[['dataset','graph','method']] = comp['combo_key'].apply(lambda s: pd.Series(parse_key(s)))
                comp['dset_graph'] = comp['dataset'].astype(str) + ' / ' + comp['graph'].astype(str)
                pivot = comp.pivot_table(index='dset_graph', columns='method', values='delta_mean', aggfunc='mean')
                plt.figure(figsize=(12, max(6, pivot.shape[0]*0.25)))
                try:
                    sns.heatmap(pivot, cmap='vlag', center=0, annot=True, fmt='.2e')
                except Exception:
                    plt.imshow(pivot.fillna(0).values, aspect='auto', cmap='vlag')
                    plt.colorbar()
                plt.title('Delta mean (it131..150 - baseline)')
                plt.tight_layout()
                pp.savefig()
                plt.close()
            else:
                print('Comparison CSV found but missing combo_key column')
        except Exception as e:
            print('Failed to create heatmap:', e)
    else:
        print('Comparison CSV not found at', comp_csv)

print('Figures PDF written to', FIG_PDF)

# Attempt to merge with existing report_summary.pdf
if FIG_PDF.exists():
    if EXISTING_PDF.exists() and PdfReader is not None:
        try:
            writer = PdfWriter()
            for p in [str(EXISTING_PDF), str(FIG_PDF)]:
                reader = PdfReader(p)
                # PdfReader.pages is iterable
                for page in reader.pages:
                    writer.add_page(page)
            with open(str(UPDATED_PDF), 'wb') as fh:
                writer.write(fh)
            print('Merged report written to', UPDATED_PDF)
        except Exception as e:
            print('PDF merge failed:', e)
            # fallback: copy figures PDF as updated
            try:
                import shutil
                shutil.copy(str(FIG_PDF), str(UPDATED_PDF))
                print('Copied figures PDF to', UPDATED_PDF)
            except Exception as e2:
                print('Fallback copy failed:', e2)
    else:
        # cannot merge (missing existing PDF or PyPDF2); copy figures as updated
        try:
            import shutil
            shutil.copy(str(FIG_PDF), str(UPDATED_PDF))
            print('No base report or PDF merger; copied figures to', UPDATED_PDF)
        except Exception as e:
            print('Copy failed:', e)
else:
    print('Figures PDF missing, cannot merge')

print('Done')
