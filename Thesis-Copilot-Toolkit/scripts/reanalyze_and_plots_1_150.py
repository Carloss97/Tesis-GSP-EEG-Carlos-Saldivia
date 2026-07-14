#!/usr/bin/env python3
"""
Re-analyze all iterations (it1..it150), compute best-method-by-combo,
perform power estimates for top20 combos, generate boxplot/violin PDFs and
publication-ready figure for selected combos.

Outputs (under results/analysis/batches):
 - best_method_by_combo_stats_1_150.csv
 - top20_best_combos_1_150.csv
 - top10_delta_combos.csv (from existing top20_delta_combos.csv)
 - power_analysis_top20_1_150.csv
 - it1_150_top20_box_violin.pdf
 - it1_150_selected5_pubfig.png
 - it1_150_selected5_box_violin.pdf

Usage:
  python scripts/reanalyze_and_plots_1_150.py --topN 20 --select5 5

"""
from __future__ import annotations
import math
from pathlib import Path
import re
import json
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
try:
    import seaborn as sns
    sns.set(style='whitegrid')
except Exception:
    sns = None

from scipy import stats

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / 'results'
BATCH = RESULTS / 'analysis' / 'batches'
BATCH.mkdir(parents=True, exist_ok=True)

pattern = re.compile(r'it(\d+)_.*_raw\.csv')
raw_files = []
for p in sorted(RESULTS.glob('it*_raw.csv')):
    m = pattern.match(p.name)
    if not m:
        continue
    itn = int(m.group(1))
    if 1 <= itn <= 150:
        raw_files.append((itn, p))

if not raw_files:
    print('No raw files it1..it150 found in', RESULTS)
    raise SystemExit(1)

print('Found', len(raw_files), 'raw iteration files')

dfs = []
for itn, p in raw_files:
    try:
        df = pd.read_csv(p)
        df['it_num'] = itn
        # normalize missing_ratio column if present
        if 'missing_ratio' in df.columns:
            df['missing_ratio'] = df['missing_ratio'].astype(str)
        dfs.append(df)
    except Exception as e:
        print('Failed read', p, e)

all_df = pd.concat(dfs, ignore_index=True)
print('Combined rows:', len(all_df))

# choose metric
metric_candidates = ['mae', 'MAE', 'error', 'rmse']
metric = None
for c in metric_candidates:
    if c in all_df.columns:
        metric = c
        break
if metric is None:
    num_cols = all_df.select_dtypes(include=[np.number]).columns.tolist()
    metric = num_cols[0] if num_cols else None
if metric is None:
    raise SystemExit('No numeric metric found')
print('Using metric:', metric)

# standard combo keys
cols = ['dataset', 'graph', 'method']
for c in cols:
    if c not in all_df.columns:
        all_df[c] = ''

if 'missing_ratio' in all_df.columns:
    all_df['combo_key'] = all_df['dataset'].astype(str) + '|' + all_df['graph'].astype(str) + '|' + all_df['method'].astype(str) + '|mr=' + all_df['missing_ratio'].astype(str)
else:
    all_df['combo_key'] = all_df['dataset'].astype(str) + '|' + all_df['graph'].astype(str) + '|' + all_df['method'].astype(str)

# per-method-per-combo stats
group = all_df.groupby(['dataset', 'graph', 'method'] + (['missing_ratio'] if 'missing_ratio' in all_df.columns else []))
rows = []
for keys, g in group:
    n = len(g)
    mean = float(g[metric].mean())
    std = float(g[metric].std()) if n > 1 else float('nan')
    med = float(g[metric].median())
    rows.append({
        'dataset': keys[0], 'graph': keys[1], 'method': keys[2],
        'missing_ratio': (keys[3] if len(keys) > 3 else ''),
        'n': int(n), 'mean': mean, 'median': med, 'std': std,
    })
stats_df = pd.DataFrame.from_records(rows)
# save stats
stats_path = BATCH / 'per_method_combo_stats_1_150.csv'
stats_df.to_csv(stats_path, index=False)
print('Wrote', stats_path)

# build best-method-per-(dataset,graph,missing_ratio)
group2 = stats_df.groupby(['dataset', 'graph', 'missing_ratio'] if 'missing_ratio' in stats_df.columns else ['dataset', 'graph'])
best_rows = []
for keys, g in group2:
    g_sorted = g.sort_values('mean')
    best = g_sorted.iloc[0]
    second = g_sorted.iloc[1] if len(g_sorted) > 1 else None
    best_rows.append({
        'dataset': keys[0], 'graph': keys[1], 'missing_ratio': (keys[2] if len(keys) > 2 else ''),
        'best_method': best['method'], 'best_mean': best['mean'], 'best_n': int(best['n']),
        'second_method': second['method'] if second is not None else '', 'second_mean': float(second['mean']) if second is not None else np.nan, 'second_n': int(second['n']) if second is not None else 0,
    })
best_df = pd.DataFrame.from_records(best_rows)
best_out = BATCH / 'best_method_by_combo_stats_1_150.csv'
best_df.to_csv(best_out, index=False)
print('Wrote', best_out)

# top20 combos by best_mean (lower is better)
top20 = best_df.sort_values('best_mean').head(20)
top20_path = BATCH / 'top20_best_combos_1_150.csv'
top20.to_csv(top20_path, index=False)
print('Wrote', top20_path)

# Power analysis: compare best vs second best for each top20 combo
try:
    from statsmodels.stats.power import TTestIndPower
    has_sm = True
except Exception:
    has_sm = False

power_rows = []
for _, r in top20.iterrows():
    key = r['dataset'] + '|' + r['graph'] + '|' + r['best_method'] + ('|mr=' + str(r['missing_ratio']) if r['missing_ratio'] != '' else '')
    # gather raw values
    mask_best = (all_df['dataset'] == r['dataset']) & (all_df['graph'] == r['graph']) & (all_df['method'] == r['best_method'])
    if r['missing_ratio'] != '':
        mask_best &= all_df['missing_ratio'] == str(r['missing_ratio'])
    vals_best = all_df.loc[mask_best, metric].dropna().values
    vals_second = np.array([])
    if r['second_method']:
        mask_second = (all_df['dataset'] == r['dataset']) & (all_df['graph'] == r['graph']) & (all_df['method'] == r['second_method'])
        if r['missing_ratio'] != '':
            mask_second &= all_df['missing_ratio'] == str(r['missing_ratio'])
        vals_second = all_df.loc[mask_second, metric].dropna().values

    n1 = len(vals_best)
    n2 = len(vals_second)
    mean1 = float(np.mean(vals_best)) if n1>0 else np.nan
    mean2 = float(np.mean(vals_second)) if n2>0 else np.nan
    std1 = float(np.std(vals_best, ddof=1)) if n1>1 else np.nan
    std2 = float(np.std(vals_second, ddof=1)) if n2>1 else np.nan

    if n1>1 and n2>1:
        # pooled sd
        s_pooled = math.sqrt(((n1-1)*std1**2 + (n2-1)*std2**2) / (n1+n2-2)) if (n1+n2-2)>0 else np.nan
        d = (mean1 - mean2) / s_pooled if s_pooled and s_pooled>0 else np.nan
        # required n per group for power=0.8 alpha=0.05 (two-sided)
        if has_sm and not np.isnan(d):
            power_analyzer = TTestIndPower()
            try:
                # compute achieved power with current n
                achieved = float(power_analyzer.power(effect_size=d, nobs1=n1, ratio=n2/n1 if n1>0 else 1.0, alpha=0.05))
            except Exception:
                achieved = float('nan')
            try:
                req = math.ceil(power_analyzer.solve_power(effect_size=d, power=0.8, alpha=0.05, ratio=1.0, alternative='two-sided'))
            except Exception:
                req = None
        else:
            achieved = float('nan')
            if not np.isnan(d) and d!=0:
                # approximation: n = 2*(Z(a/2)+Z(power))^2 / d^2
                Za = stats.norm.ppf(1-0.05/2)
                Zb = stats.norm.ppf(0.8)
                req = math.ceil(2*((Za+Zb)**2) / (d**2)) if d!=0 else None
            else:
                req = None
    else:
        d = np.nan
        achieved = np.nan
        req = None

    power_rows.append({
        'combo_key': key, 'dataset': r['dataset'], 'graph': r['graph'], 'missing_ratio': r['missing_ratio'],
        'best_method': r['best_method'], 'second_method': r['second_method'],
        'n_best': n1, 'n_second': n2, 'mean_best': mean1, 'mean_second': mean2,
        'cohens_d': float(d) if not np.isnan(d) else '', 'achieved_power': float(achieved) if not np.isnan(achieved) else '', 'required_n_per_group_for_80pct': int(req) if req is not None else ''
    })

power_df = pd.DataFrame.from_records(power_rows)
power_csv = BATCH / 'power_analysis_top20_1_150.csv'
power_df.to_csv(power_csv, index=False)
print('Wrote', power_csv)

# Create plots for top20: boxplots/violins per combo comparing methods
pdf_path = BATCH / 'it1_150_top20_box_violin.pdf'
from matplotlib.backends.backend_pdf import PdfPages
with PdfPages(str(pdf_path)) as pp:
    for _, r in top20.iterrows():
        ds = r['dataset']; gr = r['graph']; mr = r['missing_ratio']
        mask = (all_df['dataset']==ds) & (all_df['graph']==gr)
        if mr!='':
            mask &= (all_df['missing_ratio']==str(mr))
        sub = all_df[mask].copy()
        if sub.empty:
            continue
        sub['combo_short'] = sub['dataset'].astype(str) + ' / ' + sub['graph'].astype(str) + ' / ' + sub['method'].astype(str)
        plt.figure(figsize=(10,6))
        try:
            if sns is not None:
                sns.boxplot(x='method', y=metric, data=sub)
                sns.stripplot(x='method', y=metric, data=sub, color='0.3', size=3, jitter=True)
            else:
                unique = sub['method'].unique()
                data_to_plot = [sub.loc[sub['method']==m, metric].dropna().values for m in unique]
                plt.boxplot(data_to_plot)
                plt.xticks(range(1, len(unique)+1), unique, rotation=45)
        except Exception as e:
            print('Plot error for', ds, gr, e)
        plt.title(f"{ds} | {gr} | mr={mr}")
        plt.tight_layout()
        pp.savefig()
        plt.close()
print('Wrote', pdf_path)

# Top10 delta combos from existing top20_delta_combos.csv
delta_src = BATCH / 'top20_delta_combos.csv'
if delta_src.exists():
    ddf = pd.read_csv(delta_src)
    # create a readable combo key if not present
    if 'combo_key' not in ddf.columns:
        ddf['combo_key'] = ddf['dataset'].astype(str) + '|' + ddf['graph'].astype(str) + '|mr=' + ddf.get('missing_ratio', '').astype(str)
    if 'delta_mean' in ddf.columns:
        top10delta = ddf.sort_values('delta_mean', ascending=False).head(10)
        top10_path = BATCH / 'top10_delta_combos.csv'
        top10delta.to_csv(top10_path, index=False)
        print('Wrote', top10_path)
        print('Top10 delta combos:')
        # print a compact table
        print(top10delta[['combo_key', 'delta_mean']].to_string(index=False))
    else:
        print('delta_mean not in', delta_src)
else:
    print('No delta source file at', delta_src)

# Select 5 combos for publication figure: choose top5 by delta (if available) else top5 by best_mean
if delta_src.exists() and 'delta_mean' in ddf.columns:
    sel = ddf.sort_values('delta_mean', ascending=False).head(5)['combo_key'].tolist()
else:
    sel = (top20['dataset'].astype(str) + '|' + top20['graph'].astype(str) + '|' + top20['best_method'].astype(str) + ('|mr=' + top20['missing_ratio'].astype(str)))
    sel = sel.tolist()[:5]

# produce boxplots/violins for selected 5 combos and a publication-ready figure
sel_pdf = BATCH / 'it1_150_selected5_box_violin.pdf'
pub_png = BATCH / 'it1_150_selected5_pubfig.png'
with PdfPages(str(sel_pdf)) as pp:
    fig, axes = plt.subplots(1, len(sel), figsize=(5*len(sel), 5))
    if len(sel) == 1:
        axes = [axes]
    for ax, combo in zip(axes, sel):
        # parse combo_key
        parts = combo.split('|')
        ds = parts[0] if len(parts)>0 else ''
        gr = parts[1] if len(parts)>1 else ''
        me = parts[2] if len(parts)>2 else ''
        mr = ''
        if len(parts)>3:
            mr = parts[3]
        mask = (all_df['dataset']==ds) & (all_df['graph']==gr)
        if mr:
            mask &= (all_df['missing_ratio']==mr)
        sub = all_df[mask]
        if sub.empty:
            ax.text(0.5,0.5,'No data', ha='center')
            continue
        try:
            if sns is not None:
                sns.violinplot(x='method', y=metric, data=sub, ax=ax, inner='quartile')
                sns.boxplot(x='method', y=metric, data=sub, ax=ax, width=0.2)
            else:
                unique = sub['method'].unique()
                data_to_plot = [sub.loc[sub['method']==m, metric].dropna().values for m in unique]
                ax.boxplot(data_to_plot)
                ax.set_xticks(range(1, len(unique)+1))
                ax.set_xticklabels(unique, rotation=45)
        except Exception as e:
            ax.text(0.5,0.5,'Plot error')
        ax.set_title(f"{ds} | {gr} | {me}")
    plt.tight_layout()
    pp.savefig()
    # also save PNG (first page)
    fig.savefig(str(pub_png), dpi=200)
    plt.close(fig)
print('Wrote', sel_pdf, 'and', pub_png)

print('All done')
