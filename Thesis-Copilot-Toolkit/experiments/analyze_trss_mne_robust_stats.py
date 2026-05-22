#!/usr/bin/env python3
"""Robust statistical analysis for TRSS vs MNE interpolate_bads benchmark.

Reads results/trss_vs_mne_bads_extensive/derived_balanced.csv and produces
hierarchical bootstrap summaries, paired Wilcoxon tests with Benjamini-Hochberg
correction, dataset stratification, and LaTeX tables for the thesis.

The hierarchy used by the bootstrap is:
  scenario cluster = dataset × missing_mode × missing_value
  replicate unit   = seed × bad_idx within each cluster

This keeps the bootstrap conservative relative to naive row-level resampling,
because repeated seeds inside the same dataset/scenario are not treated as fully
independent experimental designs.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable
import json
import math

import numpy as np
import pandas as pd
from scipy.stats import wilcoxon

ROOT = Path(__file__).resolve().parents[1]
RESULT_DIR = ROOT / "results" / "trss_vs_mne_bads_extensive"
IN_CSV = RESULT_DIR / "derived_balanced.csv"
OUT_DIR = RESULT_DIR / "robust_stats"
MNE_METHOD = "mne_interpolate_bads_spline"
CANDIDATES = ["trss_default", "trss_cv_tuned_seed0", "trss_oracle_grid"]
METRICS = [
    "mae",
    "rmse",
    "nrmse",
    "dtw",
    "snr",
    "lsd",
    "coherence_mean",
    "corr_mean",
    "r2",
    "runtime_s",
]
LOWER_BETTER = {"mae", "rmse", "nrmse", "dtw", "lsd", "runtime_s"}
HIGHER_BETTER = set(METRICS) - LOWER_BETTER
KEYS = ["dataset", "missing_mode", "missing_value", "seed", "bad_idx"]
SCENARIO_KEYS = ["dataset", "missing_mode", "missing_value"]
N_BOOT = 2000
RNG_SEED = 20260513
EPS = 1e-15


@dataclass(frozen=True)
class MetricSpec:
    name: str
    direction: str


def fnum(x: float, nd: int = 3) -> str:
    if pd.isna(x):
        return "--"
    ax = abs(float(x))
    if ax != 0 and (ax < 1e-3 or ax >= 1e4):
        return f"{x:.2e}"
    return f"{x:.{nd}f}"


def ptex(p: float) -> str:
    if pd.isna(p):
        return "--"
    if p < 1e-99:
        return "$<10^{-99}$"
    if p < 1e-3:
        exp = int(math.floor(math.log10(p)))
        mant = p / (10 ** exp)
        return f"${mant:.1f}\\times 10^{{{exp}}}$"
    return f"{p:.3f}"


def pct(x: float, nd: int = 1) -> str:
    if pd.isna(x):
        return "--"
    return f"{100*x:.{nd}f}"


def bh_fdr(pvalues: Iterable[float]) -> np.ndarray:
    p = np.asarray(list(pvalues), dtype=float)
    out = np.full_like(p, np.nan)
    valid = ~np.isnan(p)
    pv = p[valid]
    m = len(pv)
    if m == 0:
        return out
    order = np.argsort(pv)
    ranked = pv[order]
    q = ranked * m / np.arange(1, m + 1)
    q = np.minimum.accumulate(q[::-1])[::-1]
    q = np.minimum(q, 1.0)
    tmp = np.empty_like(q)
    tmp[order] = q
    out[valid] = tmp
    return out


def paired_table(df: pd.DataFrame, method_a: str, metric: str) -> pd.DataFrame:
    # KEYS already include the scenario columns; avoid duplicate labels because
    # pandas refuses merges when column names are not unique.
    a = df[df["method"] == method_a][KEYS + [metric]].copy()
    b = df[df["method"] == MNE_METHOD][KEYS + [metric]].copy()
    a = a.rename(columns={metric: "a"})
    b = b.rename(columns={metric: "b"})
    merged = a.merge(b, on=KEYS, how="inner", validate="one_to_one")
    if len(merged) == 0:
        raise RuntimeError(f"No paired rows for {method_a} vs {MNE_METHOD} on {metric}")
    return merged


def improvement(a: np.ndarray, b: np.ndarray, metric: str) -> np.ndarray:
    denom = np.maximum(np.abs(b), EPS)
    if metric in LOWER_BETTER:
        return (b - a) / denom
    return (a - b) / denom


def raw_diff(a: np.ndarray, b: np.ndarray, metric: str) -> np.ndarray:
    # Positive means candidate better, independent of metric direction.
    if metric in LOWER_BETTER:
        return b - a
    return a - b


def win_mask(a: np.ndarray, b: np.ndarray, metric: str) -> np.ndarray:
    if metric in LOWER_BETTER:
        return a < b
    return a > b


def paired_rank_biserial(diff_benefit: np.ndarray) -> float:
    # Rank-biserial effect size for paired signed differences, using absolute ranks.
    d = diff_benefit[np.isfinite(diff_benefit)]
    d = d[d != 0]
    if len(d) == 0:
        return 0.0
    ranks = pd.Series(np.abs(d)).rank(method="average").to_numpy()
    w_pos = ranks[d > 0].sum()
    w_neg = ranks[d < 0].sum()
    denom = len(d) * (len(d) + 1) / 2
    return float((w_pos - w_neg) / denom)


def cohen_dz(diff_benefit: np.ndarray) -> float:
    d = diff_benefit[np.isfinite(diff_benefit)]
    sd = d.std(ddof=1)
    if len(d) < 2 or sd == 0:
        return np.nan
    return float(d.mean() / sd)


def hierarchical_bootstrap(merged: pd.DataFrame, metric: str, n_boot: int = N_BOOT) -> dict[str, float]:
    # Stable metric-specific seed; avoid Python's salted hash for reproducibility.
    stable_offset = sum((i + 1) * ord(ch) for i, ch in enumerate(metric)) % 10_000
    rng = np.random.default_rng(RNG_SEED + stable_offset)
    scenarios = []
    for _, g in merged.groupby(SCENARIO_KEYS, sort=True):
        scenarios.append((g["a"].to_numpy(float), g["b"].to_numpy(float)))
    n_scen = len(scenarios)
    med_imp = np.empty(n_boot)
    mean_imp = np.empty(n_boot)
    med_benefit_diff = np.empty(n_boot)
    win_rate = np.empty(n_boot)
    for i in range(n_boot):
        a_parts = []
        b_parts = []
        for idx in rng.integers(0, n_scen, size=n_scen):
            ga, gb = scenarios[int(idx)]
            take = rng.integers(0, len(ga), size=len(ga))
            a_parts.append(ga[take])
            b_parts.append(gb[take])
        a = np.concatenate(a_parts)
        b = np.concatenate(b_parts)
        imp = improvement(a, b, metric)
        diff = raw_diff(a, b, metric)
        med_imp[i] = np.nanmedian(imp)
        mean_imp[i] = np.nanmean(imp)
        med_benefit_diff[i] = np.nanmedian(diff)
        win_rate[i] = np.nanmean(win_mask(a, b, metric))
    def ci(x: np.ndarray) -> tuple[float, float]:
        return tuple(np.nanpercentile(x, [2.5, 97.5]).astype(float))
    med_lo, med_hi = ci(med_imp)
    mean_lo, mean_hi = ci(mean_imp)
    diff_lo, diff_hi = ci(med_benefit_diff)
    wr_lo, wr_hi = ci(win_rate)
    return {
        "boot_median_improvement_ci_low": med_lo,
        "boot_median_improvement_ci_high": med_hi,
        "boot_mean_improvement_ci_low": mean_lo,
        "boot_mean_improvement_ci_high": mean_hi,
        "boot_median_benefit_diff_ci_low": diff_lo,
        "boot_median_benefit_diff_ci_high": diff_hi,
        "boot_win_rate_ci_low": wr_lo,
        "boot_win_rate_ci_high": wr_hi,
    }


def analyze_pair(df: pd.DataFrame, method_a: str, metric: str) -> dict[str, float | str | int]:
    m = paired_table(df, method_a, metric)
    a = m["a"].to_numpy(float)
    b = m["b"].to_numpy(float)
    imp = improvement(a, b, metric)
    diff_benefit = raw_diff(a, b, metric)
    try:
        # Test whether paired benefit differs from zero. Wilcoxon on benefit-aligned diffs.
        p = float(wilcoxon(diff_benefit, zero_method="wilcox", alternative="two-sided").pvalue)
    except ValueError:
        p = np.nan
    out = {
        "comparison": f"{method_a} vs MNE",
        "method_a": method_a,
        "method_b": MNE_METHOD,
        "metric": metric,
        "direction": "lower" if metric in LOWER_BETTER else "higher",
        "n_pairs": int(len(m)),
        "n_scenarios": int(m[SCENARIO_KEYS].drop_duplicates().shape[0]),
        "a_mean": float(np.nanmean(a)),
        "b_mean": float(np.nanmean(b)),
        "a_median": float(np.nanmedian(a)),
        "b_median": float(np.nanmedian(b)),
        "median_improvement": float(np.nanmedian(imp)),
        "mean_improvement": float(np.nanmean(imp)),
        "win_rate": float(np.nanmean(win_mask(a, b, metric))),
        "median_benefit_diff": float(np.nanmedian(diff_benefit)),
        "mean_benefit_diff": float(np.nanmean(diff_benefit)),
        "wilcoxon_p": p,
        "paired_rank_biserial": paired_rank_biserial(diff_benefit),
        "cohen_dz": cohen_dz(diff_benefit),
    }
    out.update(hierarchical_bootstrap(m, metric))
    return out


def dataset_stratification(df: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for method in CANDIDATES:
        for dataset in sorted(df["dataset"].unique()):
            sub = df[df["dataset"] == dataset]
            for metric in ["mae", "nrmse", "lsd", "runtime_s"]:
                m = paired_table(sub, method, metric)
                a = m["a"].to_numpy(float)
                b = m["b"].to_numpy(float)
                imp = improvement(a, b, metric)
                rows.append({
                    "method": method,
                    "dataset": dataset,
                    "metric": metric,
                    "n": len(m),
                    "win_rate": float(np.nanmean(win_mask(a, b, metric))),
                    "median_improvement": float(np.nanmedian(imp)),
                    "mne_median": float(np.nanmedian(b)),
                    "trss_median": float(np.nanmedian(a)),
                    "runtime_ratio_median": float(np.nanmedian(
                        m[m["a"].notna() & m["b"].notna()]["a"].to_numpy(float) / np.maximum(m["b"].to_numpy(float), EPS)
                    )) if metric == "runtime_s" else np.nan,
                })
    return pd.DataFrame(rows)


def scenario_stratification(df: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for method in CANDIDATES:
        for keys, sub in df.groupby(["missing_mode", "missing_value"], sort=True):
            mode, value = keys
            for metric in ["mae", "nrmse", "lsd", "runtime_s"]:
                m = paired_table(sub, method, metric)
                a = m["a"].to_numpy(float)
                b = m["b"].to_numpy(float)
                imp = improvement(a, b, metric)
                rows.append({
                    "method": method,
                    "missing_mode": mode,
                    "missing_value": value,
                    "metric": metric,
                    "n": len(m),
                    "win_rate": float(np.nanmean(win_mask(a, b, metric))),
                    "median_improvement": float(np.nanmedian(imp)),
                    "mne_median": float(np.nanmedian(b)),
                    "trss_median": float(np.nanmedian(a)),
                })
    return pd.DataFrame(rows)


def latex_escape(s: str) -> str:
    return str(s).replace("_", "\\_")


def write_main_latex(summary: pd.DataFrame, out_path: Path) -> None:
    label_map = {
        "trss_default": "TRSS fijo",
        "trss_cv_tuned_seed0": "TRSS calibrado",
        "trss_oracle_grid": "TRSS oráculo",
    }
    metric_map = {
        "mae": "MAE $\\downarrow$",
        "nrmse": "NRMSE $\\downarrow$",
        "lsd": "LSD $\\downarrow$",
        "corr_mean": "Correlación $\\uparrow$",
        "runtime_s": "Tiempo $\\downarrow$",
    }
    keep_metrics = list(metric_map)
    keep_methods = ["trss_default", "trss_cv_tuned_seed0"]
    lines = []
    lines.append("% Auto-generated by experiments/analyze_trss_mne_robust_stats.py")
    lines.append("\\begin{table}[H]")
    lines.append("\\centering")
    lines.append("\\small")
    lines.append("\\caption{Comparación robusta contra \\code{MNE interpolate\\_bads(method='spline')}. La mejora mediana positiva indica ventaja de TRSS; para tiempo una mejora negativa indica que TRSS es más lento que MNE. Los intervalos se obtienen mediante bootstrap jerárquico por dataset y escenario.}")
    lines.append("\\label{tab:trss_mne_robust_main}")
    lines.append("\\begin{tabular}{llrrrr}")
    lines.append("\\toprule")
    lines.append("Método & Métrica & Mejora mediana (IC95) & Win-rate & $q_{BH}$ & Efecto \\\\")
    lines.append("\\midrule")
    for method in keep_methods:
        sub = summary[(summary["method_a"] == method) & (summary["metric"].isin(keep_metrics))]
        for metric in keep_metrics:
            row = sub[sub["metric"] == metric].iloc[0]
            imp = f"{pct(row['median_improvement'])}\\% [{pct(row['boot_median_improvement_ci_low'])}, {pct(row['boot_median_improvement_ci_high'])}]"
            wr = f"{pct(row['win_rate'])}\\%"
            q = ptex(row["p_fdr_bh"])
            eff = fnum(row["paired_rank_biserial"], 2)
            lines.append(f"{label_map[method]} & {metric_map[metric]} & {imp} & {wr} & {q} & {eff} \\\\")
        if method != keep_methods[-1]:
            lines.append("\\addlinespace")
    lines.append("\\bottomrule")
    lines.append("\\end{tabular}")
    lines.append("\\end{table}")
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_dataset_latex(dataset_df: pd.DataFrame, out_path: Path) -> None:
    sub = dataset_df[(dataset_df["method"] == "trss_default") & (dataset_df["metric"] == "mae")].copy()
    sub = sub.sort_values("dataset")
    lines = []
    lines.append("% Auto-generated by experiments/analyze_trss_mne_robust_stats.py")
    lines.append("\\begin{table}[H]")
    lines.append("\\centering")
    lines.append("\\small")
    lines.append("\\caption{Estratificación por dataset para TRSS fijo frente a MNE en MAE. La ventaja de TRSS no es homogénea: mejora en datos reales y sintético rugoso, pero pierde en el caso sintético suave.}")
    lines.append("\\label{tab:trss_mne_by_dataset}")
    lines.append("\\begin{tabular}{lrrrr}")
    lines.append("\\toprule")
    lines.append("Dataset & $n$ & Win-rate & Mejora mediana & MAE MNE / TRSS \\\\")
    lines.append("\\midrule")
    for _, r in sub.iterrows():
        pair = f"{fnum(r['mne_median'], 2)} / {fnum(r['trss_median'], 2)}"
        lines.append(f"{latex_escape(r['dataset'])} & {int(r['n'])} & {pct(r['win_rate'])}\\% & {pct(r['median_improvement'])}\\% & {pair} \\\\")
    lines.append("\\bottomrule")
    lines.append("\\end{tabular}")
    lines.append("\\end{table}")
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_markdown(summary: pd.DataFrame, dataset_df: pd.DataFrame, out_path: Path) -> None:
    lines = []
    lines.append("# Robust TRSS vs MNE analysis")
    lines.append("")
    lines.append(f"Input: `{IN_CSV.relative_to(ROOT)}`")
    lines.append(f"Bootstrap: {N_BOOT} hierarchical resamples; scenario cluster = dataset × missing_mode × missing_value; replicate = seed × bad_idx.")
    lines.append("")
    for method in ["trss_default", "trss_cv_tuned_seed0", "trss_oracle_grid"]:
        lines.append(f"## {method} vs MNE")
        sub = summary[(summary.method_a == method) & (summary.metric.isin(["mae", "nrmse", "lsd", "corr_mean", "runtime_s"]))]
        lines.append(sub[["metric", "n_pairs", "n_scenarios", "median_improvement", "boot_median_improvement_ci_low", "boot_median_improvement_ci_high", "win_rate", "p_fdr_bh", "paired_rank_biserial"]].to_markdown(index=False))
        lines.append("")
    lines.append("## Dataset stratification: trss_default, MAE")
    lines.append(dataset_df[(dataset_df.method == "trss_default") & (dataset_df.metric == "mae")].to_markdown(index=False))
    lines.append("")
    out_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(IN_CSV)
    df = df[df["success"].astype(bool)].copy()
    needed = [MNE_METHOD] + CANDIDATES
    missing = sorted(set(needed) - set(df["method"].unique()))
    if missing:
        raise RuntimeError(f"Missing methods in input: {missing}")

    rows = []
    for method in CANDIDATES:
        for metric in METRICS:
            rows.append(analyze_pair(df, method, metric))
    summary = pd.DataFrame(rows)
    summary["p_fdr_bh"] = bh_fdr(summary["wilcoxon_p"])
    summary["significant_fdr05"] = summary["p_fdr_bh"] < 0.05
    summary.to_csv(OUT_DIR / "robust_pairwise_summary.csv", index=False)

    ds = dataset_stratification(df)
    ds.to_csv(OUT_DIR / "robust_by_dataset.csv", index=False)
    sc = scenario_stratification(df)
    sc.to_csv(OUT_DIR / "robust_by_missing_scenario.csv", index=False)

    write_main_latex(summary, OUT_DIR / "table_trss_mne_robust_main.tex")
    write_dataset_latex(ds, OUT_DIR / "table_trss_mne_by_dataset.tex")
    write_markdown(summary, ds, OUT_DIR / "ROBUST_ANALYSIS_TRSS_MNE.md")

    metadata = {
        "input_csv": str(IN_CSV.relative_to(ROOT)),
        "n_input_rows_success": int(len(df)),
        "methods": needed,
        "metrics": METRICS,
        "n_bootstrap": N_BOOT,
        "rng_seed": RNG_SEED,
        "scenario_keys": SCENARIO_KEYS,
        "paired_keys": KEYS,
        "outputs": sorted(p.name for p in OUT_DIR.iterdir()),
    }
    (OUT_DIR / "metadata.json").write_text(json.dumps(metadata, indent=2), encoding="utf-8")
    print(json.dumps(metadata, indent=2))
    print("\nHeadline:")
    print(summary[(summary.method_a == "trss_default") & (summary.metric.isin(["mae", "nrmse", "lsd", "corr_mean", "runtime_s"]))][["metric", "median_improvement", "boot_median_improvement_ci_low", "boot_median_improvement_ci_high", "win_rate", "p_fdr_bh", "paired_rank_biserial"]].to_string(index=False))


if __name__ == "__main__":
    main()
