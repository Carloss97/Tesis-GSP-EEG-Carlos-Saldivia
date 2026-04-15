#!/usr/bin/env python3
from pathlib import Path
import sys, json
try:
    import pandas as pd
    import numpy as np
except Exception:
    print('ERROR: requires pandas and numpy. Install with: pip install pandas numpy')
    sys.exit(2)

root = Path(__file__).resolve().parent.parent
it05_path = root / 'results' / 'it05_all_datasets_raw.csv'
out_dir = root / 'experiments'
out_dir.mkdir(parents=True, exist_ok=True)

if not it05_path.exists():
    print('ERROR: input file not found:', it05_path)
    sys.exit(1)

print('Loading', it05_path)
df = pd.read_csv(it05_path)

# Ensure numeric columns
for c in ['mae','rmse','snr','dtw']:
    if c in df.columns:
        df[c] = pd.to_numeric(df[c], errors='coerce')

if 'dataset' not in df.columns:
    print('ERROR: column `dataset` not present in CSV')
    sys.exit(1)

phys = df[df['dataset']=='physionet_eegmmidb'].copy()
if phys.empty:
    print('No rows for physionet_eegmmidb found')
    sys.exit(0)

# Global stats for phys
def quantile_dict(s):
    return {k: float(s.quantile(k)) for k in [0.0, 0.01, 0.05, 0.1, 0.25, 0.5, 0.75, 0.9, 0.95, 0.99, 1.0]}

phys_stats = {
    'rows': int(phys.shape[0]),
    'unique_graphs': int(phys['graph'].nunique()) if 'graph' in phys.columns else None,
    'unique_methods': int(phys['method'].nunique()) if 'method' in phys.columns else None,
}
if 'mae' in phys.columns:
    s = phys['mae'].dropna()
    phys_stats['mae'] = {
        'min': float(s.min()) if not s.empty else None,
        'max': float(s.max()) if not s.empty else None,
        'mean': float(s.mean()) if not s.empty else None,
        'median': float(s.median()) if not s.empty else None,
        'quantiles': quantile_dict(s) if not s.empty else {}
    }
else:
    phys_stats['mae'] = None

# Per-combo stats
grp = None
if 'graph' in phys.columns and 'method' in phys.columns and 'mae' in phys.columns:
    grp = phys.groupby(['graph','method']).agg(
        count=('mae','count'),
        mean_mae=('mae','mean'),
        median_mae=('mae','median'),
        min_mae=('mae','min'),
        max_mae=('mae','max')
    ).reset_index()
    # sort
    grp = grp.sort_values('mean_mae')
    # find suspicious combos
    suspicious_mean = grp[grp['mean_mae'] < 1e-3]
    suspicious_min = grp[grp['min_mae'] < 1e-6]
else:
    suspicious_mean = pd.DataFrame()
    suspicious_min = pd.DataFrame()

# Compare medians across datasets
dataset_medians = df.groupby('dataset', dropna=False)['mae'].median().reset_index().rename(columns={'mae':'median_mae'})
phys_median = float(dataset_medians[dataset_medians['dataset']=='physionet_eegmmidb']['median_mae'].values[0]) if 'physionet_eegmmidb' in dataset_medians['dataset'].values else None
other_medians = dataset_medians[dataset_medians['dataset']!='physionet_eegmmidb']['median_mae'].dropna()
other_median_median = float(other_medians.median()) if not other_medians.empty else None
ratio = None
if phys_median is not None and other_median_median is not None and other_median_median != 0:
    ratio = phys_median / other_median_median

# RMSE and SNR checks for phys
rmse_stats = None
snr_stats = None
if 'rmse' in phys.columns:
    ps = phys['rmse'].dropna()
    rmse_stats = {'mean': float(ps.mean()), 'median': float(ps.median()), 'min': float(ps.min()), 'max': float(ps.max())} if not ps.empty else {}
if 'snr' in phys.columns:
    ss = phys['snr'].dropna()
    snr_stats = {'mean': float(ss.mean()), 'median': float(ss.median()), 'min': float(ss.min()), 'max': float(ss.max())} if not ss.empty else {}

# Build report
report = {
    'phys_stats': phys_stats,
    'phys_median': phys_median,
    'other_median_median': other_median_median,
    'median_ratio_phys_vs_others': ratio,
    'suspicious_mean_count': int(suspicious_mean.shape[0]) if isinstance(suspicious_mean, pd.DataFrame) else 0,
    'suspicious_min_count': int(suspicious_min.shape[0]) if isinstance(suspicious_min, pd.DataFrame) else 0,
    'top_suspicious_mean': [],
    'top_suspicious_min': [],
    'rmse_stats': rmse_stats,
    'snr_stats': snr_stats
}

if isinstance(suspicious_mean, pd.DataFrame) and not suspicious_mean.empty:
    for _, r in suspicious_mean.head(20).iterrows():
        report['top_suspicious_mean'].append({
            'graph': r['graph'], 'method': r['method'], 'mean_mae': float(r['mean_mae']), 'median_mae': float(r['median_mae']), 'min_mae': float(r['min_mae']), 'count': int(r['count'])
        })

if isinstance(suspicious_min, pd.DataFrame) and not suspicious_min.empty:
    for _, r in suspicious_min.head(20).iterrows():
        report['top_suspicious_min'].append({
            'graph': r['graph'], 'method': r['method'], 'mean_mae': float(r['mean_mae']), 'median_mae': float(r['median_mae']), 'min_mae': float(r['min_mae']), 'count': int(r['count'])
        })

# Save JSON and human-readable TXT
out_json = out_dir / 'physionet_investigation.json'
out_txt = out_dir / 'physionet_investigation.txt'
with open(out_json, 'w', encoding='utf-8') as f:
    json.dump(report, f, indent=2)

lines = []
lines.append('Physionet EEG MMIDB anomaly investigation')
lines.append('-----------------------------------------')
lines.append(f"Rows for physionet: {report['phys_stats']['rows']}")
lines.append(f"Unique graphs: {report['phys_stats']['unique_graphs']}, unique methods: {report['phys_stats']['unique_methods']}")
if report['phys_stats'].get('mae'):
    m = report['phys_stats']['mae']
    lines.append(f"MAE min={m['min']}, median={m['median']}, mean={m['mean']}")
    lines.append(f"MAE quantiles (0.01/0.05/0.1/0.5/0.9/0.99): {m['quantiles'].get(0.01)} / {m['quantiles'].get(0.05)} / {m['quantiles'].get(0.1)} / {m['quantiles'].get(0.5)} / {m['quantiles'].get(0.9)} / {m['quantiles'].get(0.99)}")

lines.append('')
lines.append(f"Median MAE (physionet): {report['phys_median']}")
lines.append(f"Median-of-medians (other datasets): {report['other_median_median']}")
lines.append(f"Ratio phys_median / others_median_median: {report['median_ratio_phys_vs_others']}")
lines.append('')
lines.append(f"Suspicious combos with mean MAE < 1e-3: {report['suspicious_mean_count']}")
for s in report['top_suspicious_mean']:
    lines.append(f" - {s['graph']} | {s['method']}: mean={s['mean_mae']}, median={s['median_mae']}, min={s['min_mae']}, count={s['count']}")

lines.append('')
lines.append(f"Combos with min MAE < 1e-6: {report['suspicious_min_count']}")
for s in report['top_suspicious_min']:
    lines.append(f" - {s['graph']} | {s['method']}: mean={s['mean_mae']}, median={s['median_mae']}, min={s['min_mae']}, count={s['count']}")

lines.append('')
if report['rmse_stats']:
    lines.append(f"RMSE stats (phys): mean={report['rmse_stats']['mean']}, median={report['rmse_stats']['median']}, min={report['rmse_stats']['min']}, max={report['rmse_stats']['max']}")
if report['snr_stats']:
    lines.append(f"SNR stats (phys): mean={report['snr_stats']['mean']}, median={report['snr_stats']['median']}, min={report['snr_stats']['min']}, max={report['snr_stats']['max']}")

lines.append('')
# Recommendation heuristic
rec = []
if report['median_ratio_phys_vs_others'] is not None:
    if report['median_ratio_phys_vs_others'] < 0.01:
        rec.append('Physionet MAE medians are two orders of magnitude smaller than other datasets; recommend excluding or investigating preprocessing/metric pipeline differences.')
    elif report['median_ratio_phys_vs_others'] < 0.1:
        rec.append('Physionet MAE medians are an order of magnitude smaller; investigate further before including in aggregate metrics.')
    else:
        rec.append('Physionet MAE medians are comparable to other datasets.')
else:
    rec.append('Insufficient data to compare medians.')

lines.append('Recommendations:')
for r in rec:
    lines.append(' - ' + r)

with open(out_txt, 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))

print('Investigation saved to:', out_json, out_txt)
print('\nShort summary:')
print('\n'.join(lines[:20]))
