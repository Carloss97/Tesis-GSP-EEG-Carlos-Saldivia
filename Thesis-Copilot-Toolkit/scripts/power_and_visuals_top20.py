#!/usr/bin/env python3
"""Compute power estimates and generate boxplot/violin figures for top20 combos.

Writes:
 - results/analysis/batches/power_analysis_top20.csv
 - results/analysis/batches/borderline_combos.csv
 - PNG figures under results/analysis/batches/figures/

Usage: python scripts/power_and_visuals_top20.py
"""
from pathlib import Path
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from math import ceil

try:
    import seaborn as sns
    _HAS_SEABORN = True
except Exception:
    _HAS_SEABORN = False

from scipy.stats import norm


def find_samples_df(batches):
    candidates = [batches / 'consolidated_all_batches.csv']
    # fallback: any batch_*_consolidated.csv concatenated
    if not candidates[0].exists():
        candidates = list(batches.glob('batch_*_consolidated.csv'))
    if candidates and candidates[0].exists():
        df = pd.read_csv(candidates[0])
        return df

    # otherwise try to concat all batch consolidated
    parts = list(batches.glob('batch_*_consolidated.csv'))
    if parts:
        dfs = [pd.read_csv(p) for p in parts]
        return pd.concat(dfs, ignore_index=True)

    raise FileNotFoundError('No per-run consolidated CSV found in batches')


def sanitize_filename(s: str) -> str:
    return ''.join(c if c.isalnum() or c in '-_.' else '_' for c in str(s))


def compute_required_n_paired(delta, sd_diff, alpha=0.05, power=0.8):
    if delta == 0 or sd_diff == 0 or math.isnan(delta) or math.isnan(sd_diff):
        return float('inf')
    z_alpha = norm.ppf(1 - alpha / 2)
    z_beta = norm.ppf(power)
    n = ((z_alpha + z_beta) * sd_diff / delta) ** 2
    return ceil(n)


def compute_required_n_unpaired(delta, pooled_sd, alpha=0.05, power=0.8):
    if pooled_sd is None:
        return float('inf')
    if delta == 0 or pooled_sd == 0 or math.isnan(delta) or math.isnan(pooled_sd):
        return float('inf')
    z_alpha = norm.ppf(1 - alpha / 2)
    z_beta = norm.ppf(power)
    d = abs(delta) / pooled_sd
    if d == 0:
        return float('inf')
    n_per_group = 2 * ((z_alpha + z_beta) ** 2) / (d ** 2)
    return ceil(n_per_group)


def main():
    ROOT = Path(__file__).resolve().parents[1]
    batches = ROOT / 'results' / 'analysis' / 'batches'
    figures_dir = batches / 'figures'
    figures_dir.mkdir(parents=True, exist_ok=True)

    samples = find_samples_df(batches)
    # columns expected: dataset, graph, missing_ratio, method, mae, block

    top20_csv = batches / 'top20_delta_combos.csv'
    if top20_csv.exists():
        top20 = pd.read_csv(top20_csv)
    else:
        # fall back to top20 by delta in stats
        stats = pd.read_csv(batches / 'best_method_by_combo_stats.csv')
        top20 = stats.sort_values('delta_mean', ascending=False).head(20)

    out_rows = []

    for idx, row in top20.reset_index(drop=True).iterrows():
        graph = row.get('graph')
        dataset = row.get('dataset')
        try:
            missing_ratio = float(row.get('missing_ratio'))
        except Exception:
            missing_ratio = row.get('missing_ratio')

        best = row.get('best_method')
        second = row.get('second_method')
        p_adj = row.get('p_adj') if 'p_adj' in row else None

        # filter samples
        df_combo = samples[(samples['dataset'] == dataset) & (samples['graph'] == graph)]
        # allow numeric missing_ratio matching
        if 'missing_ratio' in samples.columns:
            try:
                df_combo = df_combo[pd.to_numeric(df_combo['missing_ratio'], errors='coerce') == float(missing_ratio)]
            except Exception:
                df_combo = df_combo[df_combo['missing_ratio'] == missing_ratio]

        if df_combo.empty:
            print(f'No sample rows for combo {dataset}/{graph}/{missing_ratio}')
            continue

        # ensure mae numeric
        df_combo['mae'] = pd.to_numeric(df_combo['mae'], errors='coerce')

        # decide runner-up
        if not second or pd.isna(second):
            means = df_combo.groupby('method')['mae'].mean().sort_values()
            if len(means) >= 2:
                best = means.index[0]
                second = means.index[1]
            else:
                second = None

        # pivot by block to match runs (paired)
        paired = False
        if 'block' in df_combo.columns:
            pivot = df_combo.pivot_table(index='block', columns='method', values='mae')
            if best in pivot.columns and second in pivot.columns:
                paired = True
                pivot2 = pivot[[best, second]].dropna()
                diff = pivot2[second] - pivot2[best]
                delta_mean = float(diff.mean())
                sd_diff = float(diff.std(ddof=1)) if len(diff) > 1 else float('nan')
                n_current = len(diff)
            else:
                paired = False

        if not paired:
            # unpaired fallback
            grp = df_combo.groupby('method')['mae']
            best_vals = grp.get_group(best) if best in grp.groups else pd.Series(dtype=float)
            second_vals = grp.get_group(second) if second and second in grp.groups else pd.Series(dtype=float)
            delta_mean = float(second_vals.mean() - best_vals.mean()) if (not best_vals.empty and not second_vals.empty) else float('nan')
            var1 = float(best_vals.var(ddof=1)) if len(best_vals) > 1 else float('nan')
            var2 = float(second_vals.var(ddof=1)) if len(second_vals) > 1 else float('nan')
            n1 = len(best_vals)
            n2 = len(second_vals)
            pooled_sd = None
            if not math.isnan(var1) and not math.isnan(var2) and (n1 + n2 - 2) > 0:
                pooled_sd = math.sqrt(((n1 - 1) * var1 + (n2 - 1) * var2) / (n1 + n2 - 2))
            sd_diff = float('nan')
            n_current = max(n1, n2)

        # compute required ns
        req_n_p80 = compute_required_n_paired(delta_mean, sd_diff, power=0.8)
        req_n_p90 = compute_required_n_paired(delta_mean, sd_diff, power=0.9)

        # unpaired
        req_unp80 = compute_required_n_unpaired(delta_mean, pooled_sd if 'pooled_sd' in locals() else None, power=0.8)
        req_unp90 = compute_required_n_unpaired(delta_mean, pooled_sd if 'pooled_sd' in locals() else None, power=0.9)

        out_rows.append({
            'graph': graph,
            'dataset': dataset,
            'missing_ratio': missing_ratio,
            'best_method': best,
            'second_method': second,
            'delta_mean': delta_mean,
            'sd_diff': sd_diff,
            'n_current': n_current,
            'req_n_paired_80': req_n_p80,
            'req_n_paired_90': req_n_p90,
            'req_n_unpaired_80': req_unp80,
            'req_n_unpaired_90': req_unp90,
            'p_adj': p_adj,
        })

        # prepare plot data: best, second, optionally top3
        plot_methods = [m for m in [best, second] if m and m in df_combo['method'].unique()]
        if plot_methods:
            plot_df = df_combo[df_combo['method'].isin(plot_methods)].copy()
            # replace missing_ratio for label
            label = f"{dataset} | {graph} | m={missing_ratio}"
            fname_base = f"top20_{idx+1}_{sanitize_filename(dataset)}_{sanitize_filename(graph)}_{str(missing_ratio).replace('.','p')}"
            # boxplot
            plt.figure(figsize=(6,4))
            if _HAS_SEABORN:
                sns.boxplot(x='method', y='mae', data=plot_df, order=plot_methods)
            else:
                # matplotlib boxplot grouped
                groups = [plot_df[plot_df['method']==m]['mae'].dropna() for m in plot_methods]
                plt.boxplot(groups, labels=plot_methods)
            plt.title('Boxplot: ' + label)
            plt.tight_layout()
            out_png = figures_dir / f"boxplot_{fname_base}.png"
            plt.savefig(out_png, dpi=150)
            plt.close()

            # violin
            plt.figure(figsize=(6,4))
            if _HAS_SEABORN:
                sns.violinplot(x='method', y='mae', data=plot_df, order=plot_methods)
            else:
                groups = [plot_df[plot_df['method']==m]['mae'].dropna() for m in plot_methods]
                plt.boxplot(groups, labels=plot_methods)
            plt.title('Violin: ' + label)
            plt.tight_layout()
            out_png = figures_dir / f"violin_{fname_base}.png"
            plt.savefig(out_png, dpi=150)
            plt.close()

    out_df = pd.DataFrame(out_rows)
    out_csv = batches / 'power_analysis_top20.csv'
    out_df.to_csv(out_csv, index=False)

    # borderline combos: required paired <=200 and greater than current n
    borderline = out_df[(out_df['req_n_paired_80'] != float('inf')) & (out_df['req_n_paired_80'] <= 200) & (out_df['req_n_paired_80'] > out_df['n_current'])]
    borderline_csv = batches / 'borderline_combos.csv'
    borderline.to_csv(borderline_csv, index=False)

    print('Wrote:', out_csv)
    print('Wrote:', borderline_csv)


if __name__ == '__main__':
    main()
