#!/usr/bin/env python3
import sys
from pathlib import Path
try:
    import pandas as pd
    import numpy as np
except Exception:
    print("ERROR: this script requires pandas and numpy. Install with: pip install pandas numpy")
    sys.exit(2)

root = Path(__file__).resolve().parent.parent
results_dir = root / 'results'
out_dir = Path(__file__).resolve().parent
it05_path = results_dir / 'it05_all_datasets_raw.csv'
it20_path = results_dir / 'it20_synthetic_alpha_high_missing_raw.csv'

for p in (it05_path, it20_path):
    if not p.exists():
        print(f"ERROR: required file not found: {p}")
        sys.exit(1)


def load_csv(path):
    df = pd.read_csv(path)
    # Ensure numeric columns
    for c in ['mae','rmse','snr','dtw']:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors='coerce')
    return df

it05 = load_csv(it05_path)
it20 = load_csv(it20_path)

# Helper: aggregate by (graph, method)
def aggregate(df):
    grp = df.groupby(['graph','method']).agg(
        mean_mae=('mae','mean'),
        std_mae=('mae','std'),
        median_mae=('mae','median'),
        count=('mae','count'),
        mean_rmse=('rmse','mean'),
        mean_snr=('snr','mean'),
        datasets_count=('dataset','nunique')
    ).reset_index()
    grp['std_mae'] = grp['std_mae'].fillna(0.0)
    # ranking metric prefers low mean and low variance
    grp['rank_metric'] = grp['mean_mae'] + 0.5 * grp['std_mae']
    return grp

agg05 = aggregate(it05)
agg20 = aggregate(it20)

# classification helpers
import re
def is_temporal(method):
    m = method.lower()
    tokens = ['temporal','tv','wavelet','time','trss','directed_tv','heat_diffusion','graph_time']
    return any(t in m for t in tokens)

baseline_methods = ["linear", "ica", "spherical_spline", "rbfi_tps"]

agg05['temporal'] = agg05['method'].apply(is_temporal)
agg05['baseline'] = agg05['method'].isin(baseline_methods)

agg20['temporal'] = agg20['method'].apply(is_temporal)
agg20['baseline'] = agg20['method'].isin(baseline_methods)

# Select generalist combos: appear in many datasets
min_datasets_for_generalist = max(3, int(it05['dataset'].nunique() * 0.1))

generalists = agg05[agg05['datasets_count'] >= min_datasets_for_generalist].sort_values(['rank_metric'])
top3_generalists = generalists.head(3)

temporal_candidates = agg05[agg05['temporal']].sort_values(['rank_metric'])
top3_temporal = temporal_candidates.head(3)

instant_candidates = agg05[~agg05['temporal']].sort_values(['rank_metric'])
# exclude very specialized synthetic-only combos with datasets_count==1 from instant selection
instant_candidates = instant_candidates[instant_candidates['datasets_count']>=1]
top3_instant = instant_candidates.head(3)

# Baselines: compute aggregated baseline stats (method-level)
baseline_df = it05[it05['method'].isin(baseline_methods)]
baseline_summary = baseline_df.groupby('method').agg(mean_mae=('mae','mean'), std_mae=('mae','std'), datasets_count=('dataset','nunique')).reset_index().sort_values('mean_mae')

# For each recommended combo, find top datasets where it performed best (lowest mae)
def top_datasets_for_combo(df_raw, graph, method, topk=5):
    sel = df_raw[(df_raw['graph']==graph)&(df_raw['method']==method)].copy()
    sel = sel[['dataset','mae','rmse','snr']].sort_values('mae').dropna(subset=['mae'])
    return sel.head(topk).to_dict(orient='records')

recommendations = {
    'generalists': [],
    'temporal': [],
    'instant': [],
    'baselines': []
}

for _, row in top3_generalists.iterrows():
    rec = dict(row)
    rec['top_datasets'] = top_datasets_for_combo(it05, row['graph'], row['method'], topk=5)
    # cross-check in it20
    match = agg20[(agg20['graph']==row['graph']) & (agg20['method']==row['method'])]
    rec['it20_mean_mae'] = float(match['mean_mae'].values[0]) if len(match) else None
    recommendations['generalists'].append(rec)

for _, row in top3_temporal.iterrows():
    rec = dict(row)
    rec['top_datasets'] = top_datasets_for_combo(it05, row['graph'], row['method'], topk=5)
    match = agg20[(agg20['graph']==row['graph']) & (agg20['method']==row['method'])]
    rec['it20_mean_mae'] = float(match['mean_mae'].values[0]) if len(match) else None
    recommendations['temporal'].append(rec)

for _, row in top3_instant.iterrows():
    rec = dict(row)
    rec['top_datasets'] = top_datasets_for_combo(it05, row['graph'], row['method'], topk=5)
    match = agg20[(agg20['graph']==row['graph']) & (agg20['method']==row['method'])]
    rec['it20_mean_mae'] = float(match['mean_mae'].values[0]) if len(match) else None
    recommendations['instant'].append(rec)

# Baselines
for _, row in baseline_summary.iterrows():
    rec = dict(row)
    # find best graph for this baseline method in it05
    best_graph_row = agg05[agg05['method']==row['method']].sort_values('mean_mae').head(1)
    if not best_graph_row.empty:
        rec['best_graph'] = best_graph_row.iloc[0]['graph']
        rec['best_graph_mean_mae'] = float(best_graph_row.iloc[0]['mean_mae'])
        rec['best_graph_top_datasets'] = top_datasets_for_combo(it05, best_graph_row.iloc[0]['graph'], row['method'], topk=5)
    else:
        rec['best_graph'] = None
    recommendations['baselines'].append(rec)

# Write outputs
out_summary = out_dir / 'analysis_it05_it20_summary.csv'
full_agg = pd.concat([agg05.assign(experiment='it05'), agg20.assign(experiment='it20')], sort=False)
full_agg.to_csv(out_summary, index=False)

out_recs = out_dir / 'analysis_it05_it20_recommendations.json'
import json
with open(out_recs, 'w', encoding='utf-8') as f:
    json.dump(recommendations, f, indent=2, ensure_ascii=False)

# Human-readable report
report = []
report.append('Analysis IT05 + IT20 — resumen y recomendaciones')
report.append('---')
report.append('\n**Top 3 generalistas (it05 aggregated)**')
for r in recommendations['generalists']:
    report.append(f"- {r['graph']} | {r['method']}: mean_mae={r['mean_mae']:.4f}, std={r['std_mae']:.4f}, datasets={int(r['datasets_count'])}, it20_mean_mae={r['it20_mean_mae']}")
    for d in r['top_datasets']:
        report.append(f"    - {d['dataset']}: mae={d.get('mae')}")

report.append('\n**Top 3 temporales (it05 aggregated)**')
for r in recommendations['temporal']:
    report.append(f"- {r['graph']} | {r['method']}: mean_mae={r['mean_mae']:.4f}, std={r['std_mae']:.4f}, datasets={int(r['datasets_count'])}, it20_mean_mae={r['it20_mean_mae']}")
    for d in r['top_datasets']:
        report.append(f"    - {d['dataset']}: mae={d.get('mae')}")

report.append('\n**Top 3 instantáneos (it05 aggregated)**')
for r in recommendations['instant']:
    report.append(f"- {r['graph']} | {r['method']}: mean_mae={r['mean_mae']:.4f}, std={r['std_mae']:.4f}, datasets={int(r['datasets_count'])}, it20_mean_mae={r['it20_mean_mae']}")
    for d in r['top_datasets']:
        report.append(f"    - {d['dataset']}: mae={d.get('mae')}")

report.append('\n**Baselines (aggregated it05)**')
for r in recommendations['baselines']:
    report.append(f"- method={r['method']}: mean_mae={r['mean_mae']:.4f}, std={r.get('std_mae'):.4f}, best_graph={r.get('best_graph')}, best_graph_mean_mae={r.get('best_graph_mean_mae')}")
    if r.get('best_graph_top_datasets'):
        for d in r['best_graph_top_datasets']:
            report.append(f"    - {d['dataset']}: mae={d.get('mae')}")

report_path = out_dir / 'analysis_it05_it20_report.txt'
with open(report_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(report))

print('Done.')
print(f'Wrote summary CSV: {out_summary}')
print(f'Wrote recommendations JSON: {out_recs}')
print(f'Wrote human report: {report_path}')

# Print short summary to stdout
print('\n==== Short Summary ====')
print('Top generalists:')
for r in recommendations['generalists']:
    print(f" - {r['graph']} | {r['method']} -> mean_mae={r['mean_mae']:.4f}")
print('Top temporal:')
for r in recommendations['temporal']:
    print(f" - {r['graph']} | {r['method']} -> mean_mae={r['mean_mae']:.4f}")
print('Top instant:')
for r in recommendations['instant']:
    print(f" - {r['graph']} | {r['method']} -> mean_mae={r['mean_mae']:.4f}")

print('\nReport saved at:', report_path)
