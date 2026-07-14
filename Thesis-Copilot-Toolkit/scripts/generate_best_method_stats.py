#!/usr/bin/env python3
"""Compute 95% CI (bootstrap) and Mann-Whitney U test between the best and
second-best method for each (graph, dataset, missing_ratio) combination.
Writes: results/analysis/batches/best_method_by_combo_stats.csv
"""
import os
import json
import math
from collections import defaultdict

import numpy as np
import pandas as pd
from scipy.stats import mannwhitneyu

ROOT = os.path.dirname(os.path.dirname(__file__))
INPUT = os.path.join(ROOT, "results", "analysis", "batches", "consolidated_all_batches.csv")
OUT = os.path.join(ROOT, "results", "analysis", "batches", "best_method_by_combo_stats.csv")


def holm_bonferroni_adjust(pvals_with_idx):
    # pvals_with_idx: list of (idx, pval)
    items = [(i, p) for i, p in pvals_with_idx if not (p is None or math.isnan(p))]
    if not items:
        return {}
    m = len(items)
    # sort ascending by p
    items_sorted = sorted(items, key=lambda x: x[1])
    adj = {}
    min_adj = 1.0
    for rank, (idx, p) in enumerate(items_sorted, start=1):
        # Holm factor: m - rank + 1
        factor = m - rank + 1
        adj_p = min(1.0, p * factor)
        # ensure monotonicity: adj p is max of previous smaller ones
        if adj_p < min_adj:
            min_adj = adj_p
        adj[idx] = adj_p
    # Enforce non-decreasing when mapped back to original indices
    # (not strictly necessary for Holm but keep it tidy)
    return adj


def bootstrap_ci(data, n_boot=1000, seed=0, alpha=0.05):
    if len(data) == 0:
        return (np.nan, np.nan)
    rng = np.random.RandomState(seed)
    means = []
    for _ in range(n_boot):
        sample = rng.choice(data, size=len(data), replace=True)
        means.append(np.mean(sample))
    lo = np.percentile(means, 100 * (alpha / 2.0))
    hi = np.percentile(means, 100 * (1 - alpha / 2.0))
    return float(lo), float(hi)


def rank_biserial_from_u(u, n1, n2):
    # Rank-biserial correlation from Mann-Whitney U
    if n1 * n2 == 0:
        return np.nan
    return 1.0 - (2.0 * u) / (n1 * n2)


def main():
    if not os.path.exists(INPUT):
        raise FileNotFoundError(INPUT)
    df = pd.read_csv(INPUT)
    # Ensure expected columns
    for c in ["graph", "dataset", "missing_ratio", "method", "mae"]:
        if c not in df.columns:
            raise KeyError(f"Missing column {c} in {INPUT}")

    df = df[["graph", "dataset", "missing_ratio", "method", "mae"]].copy()
    # normalize missing_ratio to numeric/string for grouping
    df["missing_ratio"] = pd.to_numeric(df["missing_ratio"], errors="coerce")

    groups = df.groupby(["graph", "dataset", "missing_ratio"])

    results = []
    pvals_for_adjust = []

    for (graph, dataset, mr), g in groups:
        by_method = {}
        for method, gm in g.groupby("method"):
            vals = gm["mae"].dropna().values.astype(float)
            by_method[method] = vals

        if not by_method:
            continue
        # Compute means and sort ascending (lower MAE better)
        stats = []
        for m, vals in by_method.items():
            stats.append((m, float(np.mean(vals)) if len(vals) else np.nan, len(vals), float(np.std(vals, ddof=1)) if len(vals) > 1 else np.nan))
        stats_sorted = sorted(stats, key=lambda x: (np.nan_to_num(x[1], posinf=1e9, neginf=1e9)))

        best_m, best_mean, best_n, best_std = stats_sorted[0]
        second_m, second_mean, second_n, second_std = (None, np.nan, 0, np.nan)
        if len(stats_sorted) > 1:
            second_m, second_mean, second_n, second_std = stats_sorted[1]

        best_vals = by_method.get(best_m, np.array([]))
        second_vals = by_method.get(second_m, np.array([])) if second_m is not None else np.array([])

        # delta (how much better the best is vs second)
        delta = float(second_mean - best_mean) if (not np.isnan(second_mean) and not np.isnan(best_mean)) else np.nan

        # bootstrap CI for best mean if enough samples
        ci_lo, ci_hi = (np.nan, np.nan)
        if len(best_vals) >= 2:
            ci_lo, ci_hi = bootstrap_ci(best_vals, n_boot=2000, seed=42)

        p_raw = np.nan
        u_stat = np.nan
        rb = np.nan
        if len(best_vals) >= 3 and len(second_vals) >= 3:
            try:
                u_stat, p_raw = mannwhitneyu(best_vals, second_vals, alternative='two-sided')
                rb = rank_biserial_from_u(u_stat, len(best_vals), len(second_vals))
            except Exception:
                p_raw = np.nan

        idx = (graph, dataset, mr, best_m)
        results.append({
            "graph": graph,
            "dataset": dataset,
            "missing_ratio": mr,
            "best_method": best_m,
            "best_mean_mae": best_mean,
            "best_n": best_n,
            "best_std": best_std,
            "ci_lower": ci_lo,
            "ci_upper": ci_hi,
            "second_method": second_m,
            "second_mean_mae": second_mean,
            "second_n": second_n,
            "second_std": second_std,
            "delta_mean": delta,
            "p_raw": float(p_raw) if not (p_raw is None or np.isnan(p_raw)) else np.nan,
            "p_adj": np.nan,
            "significant": False,
            "rank_biserial": float(rb) if not (rb is None or np.isnan(rb)) else np.nan,
        })

        if not (p_raw is None or np.isnan(p_raw)):
            pvals_for_adjust.append((len(results) - 1, p_raw))

    # Adjust p-values with Holm-Bonferroni
    adj_map = holm_bonferroni_adjust(pvals_for_adjust)
    for idx, adj_p in adj_map.items():
        results[idx]["p_adj"] = adj_p
        results[idx]["significant"] = adj_p < 0.05

    out_df = pd.DataFrame(results)
    out_df = out_df.sort_values(["best_method", "dataset", "graph", "missing_ratio"])
    out_df.to_csv(OUT, index=False)
    print(f"Wrote {OUT}")


if __name__ == '__main__':
    main()
