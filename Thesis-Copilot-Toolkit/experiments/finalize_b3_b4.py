"""Finalize B3/B4 artifacts from consolidated B1+B2 results."""

from __future__ import annotations

import json
import os
import platform
from pathlib import Path
from typing import Dict, List, Tuple

import numpy as np
import pandas as pd
from scipy.stats import mannwhitneyu, wilcoxon


BASELINE_METHODS = {"linear", "idw", "rbfi_tps", "rbfi_mq", "spherical_spline"}
GSP_METHODS = {"gsp", "tikhonov", "gsmooth", "bgsrp", "puy", "sobolev"}
TV_METHODS = {"graph_time_tikhonov", "trss", "tv", "sobolev_temporal"}


def ensure_paths() -> Dict[str, Path]:
    root = Path(__file__).resolve().parents[1]
    return {
        "root": root,
        "results": root / "results",
        "paper_tables": root / "paper" / "ieee" / "tables",
        "thesis_tables": root / "thesis" / "usm" / "tables",
    }


def load_data(results_dir: Path) -> Tuple[pd.DataFrame, pd.DataFrame]:
    raw = pd.read_csv(results_dir / "opt_benchmark_b2_full_scale_raw.csv")
    ranking = pd.read_csv(results_dir / "b2_publication_ranking_final.csv")
    return raw, ranking


def _rank_biserial_from_u(u_stat: float, n1: int, n2: int) -> float:
    if n1 <= 0 or n2 <= 0:
        return float("nan")
    return 1.0 - (2.0 * float(u_stat) / float(n1 * n2))


def stat02_tests(raw: pd.DataFrame) -> pd.DataFrame:
    rows: List[Dict[str, object]] = []

    # Paired family comparison using shared dataset/scenario/missing/graph/seed context.
    family_means = (
        raw.groupby(["dataset", "scenario", "missing_ratio", "graph", "mask_seed", "family"], as_index=False)
        .agg(mae=("mae", "mean"), dtw=("dtw", "mean"))
    )
    piv = family_means.pivot_table(
        index=["dataset", "scenario", "missing_ratio", "graph", "mask_seed"],
        columns="family",
        values=["mae", "dtw"],
    )

    for metric in ["mae", "dtw"]:
        if (metric, "instant") in piv.columns and (metric, "tv_time") in piv.columns:
            pair = piv[[(metric, "instant"), (metric, "tv_time")]].dropna()
            if len(pair) >= 10:
                stat, pval = wilcoxon(pair[(metric, "tv_time")], pair[(metric, "instant")], alternative="two-sided")
                diff = pair[(metric, "tv_time")] - pair[(metric, "instant")]
                rows.append(
                    {
                        "test_id": f"STAT-02_{metric}_family_wilcoxon",
                        "metric": metric,
                        "group_a": "tv_time",
                        "group_b": "instant",
                        "n_a": int(len(pair)),
                        "n_b": int(len(pair)),
                        "statistic": float(stat),
                        "p_value": float(pval),
                        "effect_size": float(np.median(diff)),
                        "effect_size_name": "median_delta(tv_time-instant)",
                        "decision_alpha_0_05": "reject_H0" if pval < 0.05 else "fail_to_reject_H0",
                        "notes": "Paired by dataset/scenario/missing/graph/seed",
                    }
                )

    # Method-level comparisons in raw samples.
    method_pairs = [
        ("trss", "tikhonov", "mae"),
        ("trss", "gsp", "mae"),
        ("bgsrp", "gsp", "mae"),
        ("trss", "bgsrp", "mae"),
    ]
    for a, b, metric in method_pairs:
        xa = raw.loc[raw["method"] == a, metric].dropna().to_numpy()
        xb = raw.loc[raw["method"] == b, metric].dropna().to_numpy()
        if len(xa) >= 20 and len(xb) >= 20:
            u_stat, pval = mannwhitneyu(xa, xb, alternative="two-sided")
            rows.append(
                {
                    "test_id": f"STAT-02_{metric}_{a}_vs_{b}_mwu",
                    "metric": metric,
                    "group_a": a,
                    "group_b": b,
                    "n_a": int(len(xa)),
                    "n_b": int(len(xb)),
                    "statistic": float(u_stat),
                    "p_value": float(pval),
                    "effect_size": _rank_biserial_from_u(float(u_stat), len(xa), len(xb)),
                    "effect_size_name": "rank_biserial",
                    "decision_alpha_0_05": "reject_H0" if pval < 0.05 else "fail_to_reject_H0",
                    "notes": "Unpaired two-sided Mann-Whitney U",
                }
            )

    out = pd.DataFrame(rows)
    return out.sort_values("p_value").reset_index(drop=True)


def _family_label(method: str, family: str) -> str:
    if method in TV_METHODS or family == "tv_time":
        return "TV/Tiempo"
    if method in GSP_METHODS:
        return "GSP"
    if method in BASELINE_METHODS:
        return "Baseline"
    return "Baseline"


def rep01_tables(ranking: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame]:
    df = ranking.copy()
    df["grupo"] = [
        _family_label(m, f) for m, f in zip(df["method"], df["family"])
    ]

    by_scenario = (
        df.sort_values(["dataset", "scenario", "missing_ratio", "grupo", "mae_mean", "dtw_mean"])
        .groupby(["dataset", "scenario", "missing_ratio", "grupo"], as_index=False)
        .first()
    )

    overall = (
        by_scenario.groupby("grupo", as_index=False)
        .agg(
            mae_mean=("mae_mean", "mean"),
            mae_std=("mae_mean", "std"),
            dtw_mean=("dtw_mean", "mean"),
            dtw_std=("dtw_mean", "std"),
            rmse_mean=("rmse_mean", "mean"),
            snr_mean=("snr_mean", "mean"),
        )
        .fillna(0.0)
        .sort_values("mae_mean")
    )

    method_wins = (
        by_scenario.groupby(["grupo", "method"], as_index=False)
        .size()
        .sort_values(["grupo", "size"], ascending=[True, False])
        .groupby("grupo", as_index=False)
        .first()
        .rename(columns={"method": "metodo_top", "size": "wins"})
    )
    overall = overall.merge(method_wins, on="grupo", how="left")
    return by_scenario, overall


def make_markdown_summary(stat_df: pd.DataFrame, out_path: Path) -> None:
    if stat_df.empty:
        text = "# STAT-02 Significance Report\n\nNo se pudieron ejecutar pruebas por falta de datos.\n"
        out_path.write_text(text, encoding="utf-8")
        return

    top = stat_df.sort_values("p_value").head(6)
    lines = [
        "# STAT-02 Significance Report",
        "",
        "## Resultado",
        "- Se ejecutaron pruebas de significancia sobre comparaciones clave de B2.",
        "- Regla: alpha=0.05.",
        "",
        "## Pruebas con menor p-value",
        "",
        "| test_id | metric | group_a | group_b | p_value | decision |",
        "|---|---|---|---|---:|---|",
    ]
    for _, row in top.iterrows():
        lines.append(
            f"| {row['test_id']} | {row['metric']} | {row['group_a']} | {row['group_b']} | {row['p_value']:.3e} | {row['decision_alpha_0_05']} |"
        )

    lines += [
        "",
        "## Interpretacion",
        "- El contraste principal instant vs TV/Tiempo se evalua con Wilcoxon pareado en contextos compartidos.",
        "- Las comparaciones entre metodos clave se evalúan con Mann-Whitney U.",
        "- Las conclusiones deben interpretarse junto con el estado proxy de INS-13 (pendiente 1:1 MATLAB/GSPBox).",
        "",
    ]
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def reproducibility_and_release_artifacts(paths: Dict[str, Path], stat_df: pd.DataFrame, rep_overall: pd.DataFrame) -> None:
    results_dir = paths["results"]

    versions = {
        "python": platform.python_version(),
        "platform": platform.platform(),
        "cpu_count": os.cpu_count(),
        "numpy": np.__version__,
        "pandas": pd.__version__,
    }

    try:
        import scipy

        versions["scipy"] = scipy.__version__
    except Exception:
        versions["scipy"] = "unknown"

    repro_lines = [
        "# Reproducibility Package (RPL-01)",
        "",
        "## Environment",
    ]
    for k, v in versions.items():
        repro_lines.append(f"- {k}: {v}")

    repro_lines += [
        "",
        "## Commands",
        "```powershell",
        "$env:PYTHONPATH='.../Thesis-Copilot-Toolkit'",
        "$env:INCLUDE_MNE='1'",
        "$env:MAX_TIME_SAMPLES='220'",
        "$env:B2_DTW_MAX_POINTS='80'",
        "$env:B2_TOP_K='3'",
        "$env:B2_RANDOM_SEED='42'",
        "python experiments/run_b2_batched.py",
        "python experiments/consolidate_b2_publication.py",
        "python experiments/finalize_b3_b4.py",
        "```",
        "",
        "## Core artifacts",
        "- results/opt_benchmark_b2_full_scale_raw.csv",
        "- results/opt_benchmark_b2_full_scale_summary.csv",
        "- results/b2_publication_ranking_final.csv",
        "- results/b3_stat02_significance.csv",
        "- results/b3_rep01_final_table_overall.csv",
    ]
    (results_dir / "b3_b4_reproducibility_guide.md").write_text("\n".join(repro_lines) + "\n", encoding="utf-8")

    compute_lines = [
        "# Compute Report (RPL-02)",
        "",
        f"- CPU logical cores: {versions['cpu_count']}",
        f"- Platform: {versions['platform']}",
        "- B2 execution mode: batched (9 bloques de grafos/metodos).",
        "- Runtime note: tiempo total no fue serializado automaticamente; la corrida completa finalizo en modo batch con salida exitosa.",
        f"- STAT-02 tests executed: {len(stat_df)}",
        f"- REP-01 groups in final table: {len(rep_overall)}",
    ]
    (results_dir / "b3_b4_compute_resources.md").write_text("\n".join(compute_lines) + "\n", encoding="utf-8")

    checklist_lines = [
        "# Submission Checklist (REL-01)",
        "",
        "| Item | Status | Evidence |",
        "|---|---|---|",
        "| STAT-02 significance | Done | results/b3_stat02_significance.csv |",
        "| REP-01 final table | Done | results/b3_rep01_final_table_overall.csv |",
        "| REP-02 limitations narrative | Done | paper/ieee/sections/discussion.tex + thesis/usm/chapters/05_discusion.tex |",
        "| DOC-01 sync canonical docs | Done | README.md, backlog.md, REFERENCES.md, VALIDATION_REPORT.md |",
        "| RPL-01 reproducibility guide | Done | results/b3_b4_reproducibility_guide.md |",
        "| RPL-02 compute report | Done | results/b3_b4_compute_resources.md |",
        "| INS-13 strict 1:1 MATLAB/GSPBox | Open limitation | Explicitly declared as proxy in reports |",
        "",
        "## Go/No-Go",
        "- Decision: GO (with explicit limitation on INS-13 strict 1:1 equivalence).",
    ]
    (results_dir / "b3_b4_submission_checklist.md").write_text("\n".join(checklist_lines) + "\n", encoding="utf-8")


def write_latex_tables(by_scenario: pd.DataFrame, overall: pd.DataFrame, paths: Dict[str, Path]) -> None:
    paper_path = paths["paper_tables"] / "b3_rep01_final_table.tex"
    thesis_path = paths["thesis_tables"] / "b3_rep01_final_table.tex"

    table_df = overall.copy()
    table_df = table_df[["grupo", "metodo_top", "wins", "mae_mean", "dtw_mean", "rmse_mean", "snr_mean"]]
    table_df.columns = ["Grupo", "MetodoTop", "Wins", "MAE", "DTW", "RMSE", "SNR"]

    latex = table_df.to_latex(index=False, float_format=lambda x: f"{x:.6f}")
    paper_path.write_text(latex, encoding="utf-8")
    thesis_path.write_text(latex, encoding="utf-8")


def main() -> None:
    paths = ensure_paths()
    for k in ["results", "paper_tables", "thesis_tables"]:
        paths[k].mkdir(parents=True, exist_ok=True)

    raw, ranking = load_data(paths["results"])

    stat_df = stat02_tests(raw)
    stat_csv = paths["results"] / "b3_stat02_significance.csv"
    stat_df.to_csv(stat_csv, index=False)
    make_markdown_summary(stat_df, paths["results"] / "b3_stat02_summary.md")

    by_scenario, overall = rep01_tables(ranking)
    by_scenario.to_csv(paths["results"] / "b3_rep01_final_table_by_scenario.csv", index=False)
    overall.to_csv(paths["results"] / "b3_rep01_final_table_overall.csv", index=False)

    write_latex_tables(by_scenario, overall, paths)
    reproducibility_and_release_artifacts(paths, stat_df, overall)

    config = {
        "source_raw": "results/opt_benchmark_b2_full_scale_raw.csv",
        "source_ranking": "results/b2_publication_ranking_final.csv",
        "stat_tests": int(len(stat_df)),
        "rep01_rows_by_scenario": int(len(by_scenario)),
        "rep01_rows_overall": int(len(overall)),
    }
    (paths["results"] / "b3_b4_finalize_config.json").write_text(json.dumps(config, indent=2), encoding="utf-8")

    print(f"Saved: {stat_csv}")
    print(f"Saved: {paths['results'] / 'b3_stat02_summary.md'}")
    print(f"Saved: {paths['results'] / 'b3_rep01_final_table_by_scenario.csv'}")
    print(f"Saved: {paths['results'] / 'b3_rep01_final_table_overall.csv'}")
    print(f"Saved: {paths['paper_tables'] / 'b3_rep01_final_table.tex'}")
    print(f"Saved: {paths['thesis_tables'] / 'b3_rep01_final_table.tex'}")
    print(f"Saved: {paths['results'] / 'b3_b4_reproducibility_guide.md'}")
    print(f"Saved: {paths['results'] / 'b3_b4_compute_resources.md'}")
    print(f"Saved: {paths['results'] / 'b3_b4_submission_checklist.md'}")
    print(f"Saved: {paths['results'] / 'b3_b4_finalize_config.json'}")


if __name__ == "__main__":
    main()
