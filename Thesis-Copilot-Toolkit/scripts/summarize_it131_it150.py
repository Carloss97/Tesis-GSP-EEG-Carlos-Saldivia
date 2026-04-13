#!/usr/bin/env python3
"""
Summarize it131-it150 iterations and compare to a baseline (it120/unified).
Outputs:
 - Thesis-Copilot-Toolkit/results/analysis/batches/it131_it150_summary.csv
 - Thesis-Copilot-Toolkit/results/analysis/batches/it131_it150_vs_it120_comparison.csv (if baseline found)
 - Thesis-Copilot-Toolkit/results/analysis/batches/it131_it150_summary.md
"""
import sys
from pathlib import Path
import re
import pandas as pd
import numpy as np
from scipy import stats

BASE = Path(__file__).resolve().parents[1] / 'results'
OUTDIR = BASE / 'analysis' / 'batches'
OUTDIR.mkdir(parents=True, exist_ok=True)

pattern = re.compile(r'it(\d+)_.*_raw\.csv')
files = []
for f in sorted(BASE.glob('it*_raw.csv')):
    m = pattern.match(f.name)
    if not m:
        continue
    itnum = int(m.group(1))
    if 131 <= itnum <= 150:
        files.append((itnum, f))

if not files:
    print('No se encontraron archivos it131..it150 en', BASE)
    sys.exit(1)

print(f'Found {len(files)} iteration files (it131-it150)')

dfs = []
for itnum, fpath in files:
    try:
        df = pd.read_csv(fpath)
        df['it_num'] = itnum
        df['source_file'] = fpath.name
        dfs.append(df)
    except Exception as e:
        print('ERROR reading', fpath, e)

if not dfs:
    print('No dataframes loaded, aborting')
    sys.exit(1)

all_df = pd.concat(dfs, ignore_index=True)

# Determine metric column
metric_candidates = ['mae', 'MAE', 'error', 'rmse']
metric = None
for c in metric_candidates:
    if c in all_df.columns:
        metric = c
        break
if metric is None:
    num_cols = all_df.select_dtypes(include=[np.number]).columns.tolist()
    metric = 'mae' if 'mae' in num_cols else (num_cols[0] if num_cols else None)
if metric is None:
    raise SystemExit('No numeric metric found to analyze')

print('Using metric:', metric)

# create a combo key
if 'missing_ratio' in all_df.columns:
    all_df['combo_key'] = all_df['dataset'].astype(str) + '|' + all_df['graph'].astype(str) + '|' + all_df['method'].astype(str) + '|mr=' + all_df['missing_ratio'].astype(str)
else:
    all_df['combo_key'] = all_df['dataset'].astype(str) + '|' + all_df['graph'].astype(str) + '|' + all_df['method'].astype(str)

# helper: bootstrap CI95 for the mean
rng = np.random.default_rng(12345)
def ci95_bootstrap_mean(x, n_boot=2000):
    x = np.asarray(x)
    if len(x) <= 1:
        return (np.nan, np.nan)
    idx = rng.integers(0, len(x), size=(n_boot, len(x)))
    means = x[idx].mean(axis=1)
    lo = np.percentile(means, 2.5)
    hi = np.percentile(means, 97.5)
    return lo, hi

grouped = all_df.groupby(['dataset', 'graph', 'method'] + (['missing_ratio'] if 'missing_ratio' in all_df.columns else []))
records = []
for keys, g in grouped:
    n = len(g)
    mean = g[metric].mean()
    median = g[metric].median()
    std = g[metric].std()
    lo, hi = ci95_bootstrap_mean(g[metric].dropna().values, n_boot=2000)
    rec = {
        'dataset': keys[0], 'graph': keys[1], 'method': keys[2],
        'missing_ratio': (keys[3] if len(keys) > 3 else ''),
        'n': int(n), 'mean': float(mean), 'median': float(median), 'std': float(std),
        'ci95_lo': float(lo) if not np.isnan(lo) else '', 'ci95_hi': float(hi) if not np.isnan(hi) else ''
    }
    records.append(rec)

summary_df = pd.DataFrame.from_records(records)
summary_csv = OUTDIR / 'it131_it150_summary.csv'
summary_df.to_csv(summary_csv, index=False)
print('Wrote', summary_csv)

# Comparison to baseline (prefer it120 final pack, else unified_final)
baseline_candidates = [BASE / 'it120_final_multidomain_publication_pack_raw.csv', BASE / 'unified_final_raw.csv']
baseline_path = None
for b in baseline_candidates:
    if b.exists():
        baseline_path = b
        break

comp_csv = None
if baseline_path is not None:
    base_df = pd.read_csv(baseline_path)
    if 'missing_ratio' in base_df.columns:
        base_df['combo_key'] = base_df['dataset'].astype(str) + '|' + base_df['graph'].astype(str) + '|' + base_df['method'].astype(str) + '|mr=' + base_df['missing_ratio'].astype(str)
    else:
        base_df['combo_key'] = base_df['dataset'].astype(str) + '|' + base_df['graph'].astype(str) + '|' + base_df['method'].astype(str)

    comp_records = []
    for _, row in summary_df.iterrows():
        key = (row['dataset'] + '|' + row['graph'] + '|' + row['method'] + ('|mr=' + str(row['missing_ratio']) if row['missing_ratio'] != '' else ''))
        base_group = base_df[base_df['combo_key'] == key]
        if len(base_group) >= 2 and row['n'] >= 2:
            new_vals = all_df[all_df['combo_key'] == key][metric].dropna().values
            old_vals = base_group[metric].dropna().values
            try:
                res = stats.mannwhitneyu(new_vals, old_vals, alternative='two-sided')
                U = res.statistic
                p = float(res.pvalue)
                n1 = len(new_vals); n2 = len(old_vals)
                r_rb = 1.0 - (2.0 * U) / (n1 * n2)
            except Exception:
                p = np.nan; r_rb = np.nan
            comp_records.append({
                'combo_key': key, 'n_new': int(row['n']), 'mean_new': row['mean'], 'n_old': int(len(old_vals)), 'mean_old': float(old_vals.mean()), 'delta_mean': row['mean'] - float(old_vals.mean()), 'mw_p': p, 'r_rb': r_rb
            })
    comp_df = pd.DataFrame.from_records(comp_records)
    comp_csv = OUTDIR / 'it131_it150_vs_it120_comparison.csv'
    comp_df.to_csv(comp_csv, index=False)
    print('Wrote', comp_csv)
else:
    print('No baseline file found; skipping comparison')

# Create markdown summary
md_lines = []
md_lines.append('# Resumen it131–it150')
md_lines.append('')
md_lines.append(f'- Archivos analizados: {len(files)}')
md_lines.append(f'- Filas combinadas: {len(all_df)}')
md_lines.append(f'- Métrica: `{metric}`')
md_lines.append('')
md_lines.append('## Estadísticas por combo (see CSV)')
md_lines.append(f'- CSV resumen: {summary_csv.name}')
if comp_csv:
    md_lines.append(f'- CSV comparación vs baseline: {comp_csv.name}')
md_lines.append('')
md_lines.append('## Top 10 combos (mejor media)')
for _, r in summary_df.sort_values('mean').head(10).iterrows():
    md_lines.append(f"- {r['dataset']} | {r['graph']} | {r['method']} | missing={r['missing_ratio']} — n={int(r['n'])}, mean={r['mean']:.6e} CI95=[{r['ci95_lo']:.6e},{r['ci95_hi']:.6e}]")

if comp_csv is not None and not comp_df.empty:
    md_lines.append('')
    md_lines.append('## Comparación vs baseline (it120/unified)')
    md_lines.append('### Top 10 mejoras (delta negativo = mejor)')
    for _, r in comp_df.sort_values('delta_mean').head(10).iterrows():
        md_lines.append(f"- {r['combo_key']} — mean_new={r['mean_new']:.6e}, mean_old={r['mean_old']:.6e}, delta={r['delta_mean']:.6e}, p={r['mw_p']:.3g}, r_rb={r['r_rb']:.3f}")
    md_lines.append('')
    md_lines.append('### Top 10 empeoramientos')
    for _, r in comp_df.sort_values('delta_mean', ascending=False).head(10).iterrows():
        md_lines.append(f"- {r['combo_key']} — mean_new={r['mean_new']:.6e}, mean_old={r['mean_old']:.6e}, delta={r['delta_mean']:.6e}, p={r['mw_p']:.3g}, r_rb={r['r_rb']:.3f}")

md_text = '\n'.join(md_lines)
md_path = OUTDIR / 'it131_it150_summary.md'
md_path.write_text(md_text, encoding='utf-8')
print('Wrote', md_path)

print('Done')
