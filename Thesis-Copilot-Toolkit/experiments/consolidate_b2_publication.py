"""Consolidate B1+B2 experiment outputs into publication-ready B2 tables."""

from __future__ import annotations

import json
import os
from pathlib import Path

import numpy as np
import pandas as pd


def ensure_results_dir() -> Path:
    root = Path(__file__).resolve().parents[1]
    out = root / "results"
    out.mkdir(parents=True, exist_ok=True)
    return out


def _ci95(std: pd.Series, n: pd.Series) -> pd.Series:
    return 1.96 * (std / np.sqrt(np.maximum(n, 1)))


def load_optional_csv(path: Path) -> pd.DataFrame:
    if path.exists():
        return pd.read_csv(path)
    return pd.DataFrame()


def consolidate_metrics(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return pd.DataFrame()

    out = (
        df.groupby(["dataset", "scenario", "missing_ratio", "method", "family"], as_index=False)
        .agg(
            runs=("mae", "size"),
            mae_mean=("mae", "mean"),
            mae_std=("mae", "std"),
            rmse_mean=("rmse", "mean"),
            rmse_std=("rmse", "std"),
            dtw_mean=("dtw", "mean"),
            dtw_std=("dtw", "std"),
            snr_mean=("snr", "mean"),
            snr_std=("snr", "std"),
        )
        .fillna(0.0)
    )
    out["mae_ci95"] = _ci95(out["mae_std"], out["runs"])
    out["rmse_ci95"] = _ci95(out["rmse_std"], out["runs"])
    out["dtw_ci95"] = _ci95(out["dtw_std"], out["runs"])
    out["snr_ci95"] = _ci95(out["snr_std"], out["runs"])
    return out.sort_values(["mae_mean", "dtw_mean", "rmse_mean", "snr_mean"], ascending=[True, True, True, False])


def build_bgsrp_gap_report(results_dir: Path) -> pd.DataFrame:
    summary_path = results_dir / "bgsrp_vs_narang_check_summary.csv"
    df = load_optional_csv(summary_path)
    if df.empty:
        return pd.DataFrame(
            [
                {
                    "stack": "unavailable",
                    "comparison": "BGSRP_vs_Narang",
                    "gap_mae": np.nan,
                    "status": "deferred",
                    "notes": "Missing bgsrp_vs_narang_check_summary.csv",
                }
            ]
        )

    bg = df[df["method"] == "bgsrp"]
    nar = df[df["reference_family"] == "Narang"]
    if bg.empty or nar.empty:
        return pd.DataFrame(
            [
                {
                    "stack": "python_proxy",
                    "comparison": "BGSRP_vs_Narang",
                    "gap_mae": np.nan,
                    "status": "deferred",
                    "notes": "Insufficient rows to compute residual gap",
                }
            ]
        )

    bg_mae = float(bg["mae_mean"].iloc[0])
    nar_best = float(nar["mae_mean"].min())
    return pd.DataFrame(
        [
            {
                "stack": "python_proxy",
                "comparison": "BGSRP_vs_best_narang_family",
                "gap_mae": bg_mae - nar_best,
                "status": "accepted",
                "notes": "Controlled Python benchmark proxy. MATLAB/GSPBox 1:1 remains pending.",
            }
        ]
    )


def main() -> None:
    results_dir = ensure_results_dir()

    b1_raw = Path(os.environ.get("B2_B1_RAW", results_dir / "opt_benchmark_b1_protocol_raw.csv"))
    b2_raw = Path(os.environ.get("B2_B2_RAW", results_dir / "opt_benchmark_b2_full_scale_raw.csv"))
    top_k = int(os.environ.get("B2_TOP_K", "3"))

    b1_df = load_optional_csv(b1_raw)
    b2_df = load_optional_csv(b2_raw)

    if b1_df.empty and b2_df.empty:
        raise RuntimeError("No B1/B2 raw files found for consolidation")

    if not b1_df.empty:
        b1_df = b1_df.copy()
        b1_df["phase"] = "B1"
    if not b2_df.empty:
        b2_df = b2_df.copy()
        b2_df["phase"] = "B2"

    merged = pd.concat([x for x in (b1_df, b2_df) if not x.empty], ignore_index=True)
    ranking = consolidate_metrics(merged)

    ranking_path = results_dir / "b2_publication_ranking_final.csv"
    ranking.to_csv(ranking_path, index=False)

    topk = (
        ranking.sort_values(["dataset", "scenario", "missing_ratio", "family", "mae_mean", "dtw_mean"])
        .groupby(["dataset", "scenario", "missing_ratio", "family"], as_index=False)
        .head(top_k)
        .reset_index(drop=True)
    )
    topk_path = results_dir / "b2_publication_topk_by_family_scenario.csv"
    topk.to_csv(topk_path, index=False)

    gap = build_bgsrp_gap_report(results_dir)
    gap_path = results_dir / "b2_publication_bgsrp_gap_residual.csv"
    gap.to_csv(gap_path, index=False)

    cfg = {
        "b1_raw": str(b1_raw),
        "b2_raw": str(b2_raw),
        "top_k": top_k,
        "rows_b1": int(len(b1_df)),
        "rows_b2": int(len(b2_df)),
        "rows_merged": int(len(merged)),
    }
    cfg_path = results_dir / "b2_publication_consolidation_config.json"
    cfg_path.write_text(json.dumps(cfg, indent=2), encoding="utf-8")

    print(f"Saved: {ranking_path}")
    print(f"Saved: {topk_path}")
    print(f"Saved: {gap_path}")
    print(f"Saved: {cfg_path}")


if __name__ == "__main__":
    main()
