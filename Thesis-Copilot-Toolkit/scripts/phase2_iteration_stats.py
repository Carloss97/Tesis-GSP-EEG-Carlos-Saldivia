"""
Phase 2 analysis (iteration-level statistics)

This script collects per-iteration stats files `itX*_stats.csv` from
`Thesis-Copilot-Toolkit/results/`, builds a table of method-level metrics
across iterations and performs paired Wilcoxon signed-rank tests,
Cliff's delta effect size, and bootstrap 95% CI for median differences.

Outputs:
- results/tablas_resumen/phase2_iteration_stats.csv  (pairwise comparisons)
- results/tablas_resumen/phase2_iteration_metrics_pivot.csv (pivot used)

Usage:
    python phase2_iteration_stats.py

"""
import re
import sys
from pathlib import Path
import numpy as np
import pandas as pd
from scipy.stats import wilcoxon


ROOT = Path(__file__).resolve().parents[1] / "results"
STATS_GLOB = "itX*_stats.csv"
OUT_DIR = ROOT / "tablas_resumen"
OUT_DIR.mkdir(parents=True, exist_ok=True)


def cliff_delta(x, y):
    # compute Cliff's delta (probability that a value from x > y minus reverse)
    x = np.asarray(x)
    y = np.asarray(y)
    nx = x.size
    ny = y.size
    if nx == 0 or ny == 0:
        return np.nan
    # pairwise comparisons
    diff = np.sign(np.subtract.outer(x, y)).ravel()
    return diff.sum() / (nx * ny)


def bootstrap_ci_median_diff(a, b, n_boot=5000, alpha=0.05, rng=None):
    rng = np.random.default_rng(rng)
    a = np.asarray(a)
    b = np.asarray(b)
    n = a.size
    if n == 0:
        return (np.nan, np.nan)
    diffs = np.empty(n_boot)
    for i in range(n_boot):
        idx = rng.integers(0, n, n)
        diffs[i] = np.median(a[idx] - b[idx])
    lo = np.percentile(diffs, 100 * (alpha / 2))
    hi = np.percentile(diffs, 100 * (1 - alpha / 2))
    return lo, hi


def collect_iteration_stats(root: Path):
    files = sorted(root.glob(STATS_GLOB))
    if not files:
        print(f"No stats files found with pattern {STATS_GLOB} in {root}")
        return None
    records = []
    for f in files:
        itname = f.stem  # e.g., itX0001_stats -> itX0001_stats
        try:
            df = pd.read_csv(f)
        except Exception as e:
            print(f"Warning: could not read {f}: {e}")
            continue
        # add iteration id
        iter_id = re.sub(r"_stats$", "", f.stem)
        for _, row in df.iterrows():
            rec = {
                "iteration": iter_id,
                "method": row.get("method"),
                "mae_mean": row.get("mae_mean"),
                "mae_std": row.get("mae_std"),
                "mae_median": row.get("mae_median"),
                "time_mean_sec": row.get("time_mean_sec"),
            }
            records.append(rec)
    if not records:
        print("No records collected from stats files.")
        return None
    return pd.DataFrame.from_records(records)


def pivot_metrics(df: pd.DataFrame, metric: str = "mae_median"):
    pivot = df.pivot(index="iteration", columns="method", values=metric)
    # drop iterations with NaNs across all
    pivot = pivot.dropna(how="all")
    return pivot


def pairwise_tests(pivot: pd.DataFrame, out_csv: Path):
    methods = list(pivot.columns)
    rows = []
    for i, a in enumerate(methods):
        for b in methods[i+1:]:
            a_vals = pivot[a].dropna()
            b_vals = pivot[b].dropna()
            # align by index (iteration)
            common = pivot[[a, b]].dropna()
            n = len(common)
            if n < 3:
                stat = np.nan
                p = np.nan
                cliff = np.nan
                med_diff = np.nan
                ci_lo, ci_hi = (np.nan, np.nan)
            else:
                try:
                    stat, p = wilcoxon(common[a], common[b], zero_method='wilcox', alternative='two-sided')
                except Exception:
                    # fallback to signed rank without zero_method
                    stat, p = wilcoxon(common[a], common[b])
                cliff = cliff_delta(common[a].values, common[b].values)
                med_diff = np.median(common[a].values - common[b].values)
                ci_lo, ci_hi = bootstrap_ci_median_diff(common[a].values, common[b].values, n_boot=5000, rng=42)
            rows.append({
                "method_a": a,
                "method_b": b,
                "n_iterations": n,
                "wilcoxon_stat": stat,
                "p_value": p,
                "cliff_delta": cliff,
                "median_diff": med_diff,
                "ci_lo": ci_lo,
                "ci_hi": ci_hi,
            })
    out = pd.DataFrame(rows)
    out.to_csv(out_csv, index=False)
    return out


def main():
    print("Collecting iteration stats...")
    df = collect_iteration_stats(ROOT)
    if df is None:
        print("No data to analyze. Exiting.")
        sys.exit(1)
    pivot = pivot_metrics(df, metric="mae_median")
    pivot_csv = OUT_DIR / "phase2_iteration_metrics_pivot.csv"
    pivot.to_csv(pivot_csv)
    print(f"Saved pivot table to {pivot_csv}")
    out_csv = OUT_DIR / "phase2_iteration_stats.csv"
    print("Running pairwise tests (Wilcoxon, Cliff's delta, bootstrap CI)...")
    res = pairwise_tests(pivot, out_csv)
    print(f"Results written to {out_csv}")


if __name__ == "__main__":
    main()
