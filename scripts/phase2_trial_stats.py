"""
Phase 2: Trial-level statistics reanalysis

Searches for per-trial raw CSVs (pattern: "*_raw.csv") under `results/` and
computes paired Wilcoxon tests, bootstrap confidence intervals for median
differences and Cliff's delta effect sizes between two families (configurable).

Usage:
  python scripts/phase2_trial_stats.py --results-dir results --family-a "TV/Tiempo" --family-b "Baseline" --metric MAE

If no raw CSVs are found the script exits gracefully with instructions.
"""
from pathlib import Path
import argparse
import sys
import pandas as pd
import numpy as np
from scipy.stats import wilcoxon
import math


def cliffs_delta(x, y):
    # non-parametric effect size: probability difference P(x>y)-P(y>x)
    nx = len(x)
    ny = len(y)
    gt = 0
    lt = 0
    for xi in x:
        gt += np.sum(y < xi)
        lt += np.sum(y > xi)
    return (gt - lt) / (nx * ny)


def bootstrap_median_diff(a, b, n_boot=2000, seed=42):
    rng = np.random.RandomState(seed)
    diffs = []
    n = len(a)
    for _ in range(n_boot):
        idx = rng.randint(0, n, size=n)
        diffs.append(np.median(a[idx] - b[idx]))
    lo = np.percentile(diffs, 2.5)
    hi = np.percentile(diffs, 97.5)
    return lo, hi


def find_raw_csvs(results_dir: Path):
    patterns = ["*_raw.csv", "*final*_raw.csv", "it*_raw.csv"]
    files = []
    for pat in patterns:
        files.extend(list(results_dir.rglob(pat)))
    return sorted(set(files))


def load_union_csv(files):
    dfs = []
    for f in files:
        try:
            df = pd.read_csv(f)
            df['_source_file'] = str(f.name)
            dfs.append(df)
        except Exception as e:
            print(f"Warning: failed reading {f}: {e}", file=sys.stderr)
    if not dfs:
        return None
    return pd.concat(dfs, ignore_index=True)


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--results-dir', default='results', help='Path to results directory')
    p.add_argument('--family-a', required=True, help='Family label A (e.g., "TV/Tiempo")')
    p.add_argument('--family-b', required=True, help='Family label B (e.g., "Baseline")')
    p.add_argument('--metric', default='MAE', help='Metric column to analyze (e.g., MAE, RMSE)')
    p.add_argument('--output', default='results/tablas_resumen/phase2_trial_stats_results.csv')
    args = p.parse_args()

    results_dir = Path(args.results_dir)
    if not results_dir.exists():
        print(f"Results directory not found: {results_dir}")
        sys.exit(1)

    raw_files = find_raw_csvs(results_dir)
    if not raw_files:
        print("No per-trial raw CSV files found under", results_dir)
        print("Expected files like 'it01_raw.csv' or '<tag>_raw.csv'.")
        print("If you want me to generate them, run the experiment scripts or provide the path to raw CSVs.")
        sys.exit(2)

    print(f"Found {len(raw_files)} raw CSV files. Loading...")
    df = load_union_csv(raw_files)
    if df is None:
        print("No valid CSV content could be loaded.")
        sys.exit(3)

    # Normalize column names to be tolerant
    cols = {c.lower(): c for c in df.columns}
    # Expect at least: 'familia' or 'family', 'dataset', metric column, and a trial/seed column
    family_col = cols.get('familia') or cols.get('family') or cols.get('familia_name') or None
    dataset_col = cols.get('dataset') or cols.get('data') or None
    metric_col = cols.get(args.metric.lower()) or cols.get(args.metric.upper()) or None
    trial_col = cols.get('trial') or cols.get('seed') or cols.get('seed_id') or None

    if family_col is None:
        print("Could not find a family column in CSVs. Available columns:", ','.join(df.columns))
        sys.exit(4)
    if metric_col is None and args.metric not in df.columns:
        # try approximate match
        possible = [c for c in df.columns if args.metric.lower() in c.lower()]
        if possible:
            metric_col = possible[0]
        else:
            print(f"Metric column '{args.metric}' not found. Available columns:", ','.join(df.columns))
            sys.exit(5)

    print(f"Using family column: {family_col}, metric column: {metric_col}, trial id column: {trial_col}")

    # Work on pairwise comparisons grouped by dataset (if available), otherwise global
    group_cols = [c for c in [dataset_col] if c]

    results = []
    groups = df.groupby(group_cols) if group_cols else [(None, df)]
    for gname, gdf in groups:
        # select rows for each family
        a_df = gdf[gdf[family_col] == args.family_a]
        b_df = gdf[gdf[family_col] == args.family_b]
        if a_df.empty or b_df.empty:
            print(f"Skipping group {gname}: missing families {args.family_a} or {args.family_b}")
            continue

        # align by trial/seed if available
        if trial_col:
            # perform inner join on trial id
            merged = pd.merge(a_df, b_df, on=trial_col, suffixes=('_a','_b'))
            if merged.empty:
                print(f"No matching trial ids between families in group {gname}; falling back to index-based pairing")
                vals_a = a_df[metric_col].values[:min(len(a_df), len(b_df))]
                vals_b = b_df[metric_col].values[:min(len(a_df), len(b_df))]
            else:
                vals_a = merged[f"{metric_col}_a"].values
                vals_b = merged[f"{metric_col}_b"].values
        else:
            vals_a = a_df[metric_col].values[:min(len(a_df), len(b_df))]
            vals_b = b_df[metric_col].values[:min(len(a_df), len(b_df))]

        if len(vals_a) < 5:
            print(f"Too few paired samples in group {gname} (n={len(vals_a)}); skipping statistical test")
            continue

        # Wilcoxon paired test
        try:
            stat, p = wilcoxon(vals_a, vals_b)
        except Exception as e:
            print(f"Wilcoxon failed for group {gname}: {e}")
            stat, p = math.nan, math.nan

        # bootstrap CI for median difference
        try:
            lo, hi = bootstrap_median_diff(vals_a, vals_b)
        except Exception as e:
            lo, hi = math.nan, math.nan

        # Cliff's delta
        try:
            cd = cliffs_delta(vals_a, vals_b)
        except Exception:
            cd = math.nan

        row = {
            'group': gname if gname is not None else 'global',
            'n_pairs': len(vals_a),
            'metric': args.metric,
            'wilcoxon_stat': stat,
            'wilcoxon_p': p,
            'median_diff_ci_lo': lo,
            'median_diff_ci_hi': hi,
            'cliffs_delta': cd
        }
        results.append(row)

    out_df = pd.DataFrame(results)
    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_df.to_csv(out_path, index=False)
    print(f"Saved results to {out_path}")

    # Emit a minimal LaTeX table snippet to stdout
    print('\nLaTeX snippet:')
    print('\\begin{table}[ht]')
    print('\\centering')
    print('\\caption{Phase 2: Trial-level Wilcoxon results (paired)}')
    print('\\begin{tabular}{lrrrr}')
    print('\\toprule')
    print('Group & n & W & p & Cliff\\\\')
    print('\\midrule')
    for _, r in out_df.iterrows():
        print(f"{r['group']} & {int(r['n_pairs'])} & {r['wilcoxon_stat']:.3g} & {r['wilcoxon_p']:.3g} & {r['cliffs_delta']:.3g} \\\")
    print('\\bottomrule')
    print('\\end{tabular}')
    print('\\end{table}')


if __name__ == '__main__':
    main()
