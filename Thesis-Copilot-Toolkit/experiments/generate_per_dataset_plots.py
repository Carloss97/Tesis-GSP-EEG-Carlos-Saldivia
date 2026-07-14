#!/usr/bin/env python3
from pathlib import Path
import sys
import json

try:
    import pandas as pd
    import numpy as np
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    import seaborn as sns
except Exception:
    print('ERROR: this script requires pandas, numpy, matplotlib, seaborn. Install with: pip install pandas numpy matplotlib seaborn')
    sys.exit(2)

root = Path(__file__).resolve().parent.parent
results_dir = root / 'results'
experiments_dir = root / 'experiments'
out_root = experiments_dir / 'per_dataset_plots'
out_root.mkdir(parents=True, exist_ok=True)

it05_path = results_dir / 'it05_all_datasets_raw.csv'
if not it05_path.exists():
    print('ERROR: missing file:', it05_path)
    sys.exit(1)

# load raw it05
print('Loading', it05_path)
df = pd.read_csv(it05_path)
for c in ['mae','rmse','snr','dtw']:
    if c in df.columns:
        df[c] = pd.to_numeric(df[c], errors='coerce')

# load recommendations to pick combos
recs_path = experiments_dir / 'analysis_it05_it20_recommendations_no_physionet.json'
combos = []
if recs_path.exists():
    recs = json.loads(recs_path.read_text(encoding='utf-8'))
    for cat in ['generalists','temporal','instant']:
        for r in recs.get(cat, []):
            combos.append((r.get('graph'), r.get('method')))
    for b in recs.get('baselines', []):
        if b.get('best_graph'):
            combos.append((b.get('best_graph'), b.get('method')))
else:
    print('Warning: recommendations JSON not found; will attempt to infer combos from summary CSV')
    summary_csv = experiments_dir / 'analysis_it05_it20_summary_no_physionet.csv'
    if summary_csv.exists():
        s = pd.read_csv(summary_csv)
        top = s.sort_values(['rank_metric']).head(9)
        for _, r in top.iterrows():
            combos.append((r['graph'], r['method']))

# unique combos preserving order
seen = set(); uniq = []
for g,m in combos:
    if (g,m) not in seen and pd.notna(g) and pd.notna(m):
        seen.add((g,m)); uniq.append((g,m))

if not uniq:
    print('No combos found. Aborting.')
    sys.exit(1)

print(f'Using {len(uniq)} combos for per-dataset plots')
combos_set = set([f"{g}|{m}" for g,m in uniq])

datasets = df['dataset'].dropna().unique()
all_summaries = []
for ds in datasets:
    ds_dir = out_root / ds
    ds_dir.mkdir(parents=True, exist_ok=True)
    df_ds = df[df['dataset'] == ds].copy()
    if df_ds.empty:
        continue
    df_ds['combo'] = df_ds['graph'].astype(str) + '|' + df_ds['method'].astype(str)
    df_sel = df_ds[df_ds['combo'].isin(combos_set)].dropna(subset=['mae'])
    if df_sel.empty:
        print(f'Skipping {ds}: no data for selected combos')
        continue
    # summary CSV per dataset
    per_sum = df_sel.groupby(['graph','method']).agg(
        mean_mae=('mae','mean'), median_mae=('mae','median'), std_mae=('mae','std'), count=('mae','count')
    ).reset_index()
    per_sum.to_csv(ds_dir / 'per_dataset_summary.csv', index=False)
    df_sel.to_csv(ds_dir / 'per_dataset_raw_filtered.csv', index=False)
    all_summaries.append(per_sum.assign(dataset=ds))
    # plot
    plt.figure(figsize=(max(6, len(df_sel['combo'].unique())*0.9), 5))
    order = sorted(df_sel['combo'].unique(), key=lambda x: df_sel[df_sel['combo']==x]['mae'].median())
    sns.boxplot(x='combo', y='mae', data=df_sel, order=order)
    plt.xticks(rotation=45, ha='right')
    plt.title(f'{ds} — MAE by combo')
    plt.tight_layout()
    out_png = ds_dir / 'mae_boxplot.png'
    plt.savefig(out_png, dpi=150)
    plt.close()
    print(f'Wrote {out_png} and summary for {ds}')

if all_summaries:
    pd.concat(all_summaries, sort=False).to_csv(out_root / 'all_datasets_summary.csv', index=False)
    print('Wrote overall summary:', out_root / 'all_datasets_summary.csv')
else:
    print('No per-dataset summaries generated')

print('Done.')
