#!/usr/bin/env python3
"""Generate B1-B4 selection sets from the IT05+IT20 analysis that excludes physionet.

Writes CSV/JSON/MD artifacts for cutoffs 0.05 and 0.20 into
`experiments/selections_archive_2026-04-14/`.

This script uses only files present in the repository (`experiments/` and `results/`).
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, Any

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
EXP = Path(__file__).resolve().parent
ARCHIVE = EXP / "selections_archive_2026-04-14"
ARCHIVE.mkdir(parents=True, exist_ok=True)


def load_summary(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path)
    # ensure numeric columns
    for c in ["mean_mae", "median_mae", "std_mae", "datasets_count"]:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors="coerce")
    return df


def top_k(df: pd.DataFrame, by: str, k: int = 3) -> pd.DataFrame:
    return df.sort_values(by).head(k)


def select_and_export(df_it05: pd.DataFrame, cutoff: float) -> Dict[str, Any]:
    out: Dict[str, Any] = {"cutoff": cutoff, "median_filter": {}, "mean_filter": {}, "B_sets": {}}

    # Filters (following existing workflow): median < cutoff and datasets_count >= 3
    med_filter = df_it05[(df_it05["median_mae"] < cutoff) & (df_it05["datasets_count"] >= 3)]
    mean_filter = df_it05[(df_it05["mean_mae"] < cutoff) & (df_it05["datasets_count"] >= 3)]

    med_csv = ARCHIVE / f"filtered_threshold_median_{int(cutoff*100)}_no_physionet.csv"
    mean_csv = ARCHIVE / f"filtered_threshold_mean_{int(cutoff*100)}_no_physionet.csv"
    med_filter.to_csv(med_csv, index=False)
    mean_filter.to_csv(mean_csv, index=False)

    out["median_filter"]["csv"] = str(med_csv)
    out["mean_filter"]["csv"] = str(mean_csv)
    out["median_filter"]["count"] = int(len(med_filter))
    out["mean_filter"]["count"] = int(len(mean_filter))

    # B1-B4 creation using the it05 aggregated rows
    b1 = top_k(df_it05, by="mean_mae", k=3)
    b2 = top_k(df_it05, by="mean_mae", k=3)  # real_only_mean: same here because physionet excluded
    b3 = top_k(df_it05, by="median_mae", k=3)
    b4 = df_it05.sort_values(["std_mae", "mean_mae"]).head(3)

    def df_to_list(df_in: pd.DataFrame):
        return [r.to_dict() for _, r in df_in.iterrows()]

    out["B_sets"]["B1_mean_based"] = df_to_list(b1)
    out["B_sets"]["B2_real_mean"] = df_to_list(b2)
    out["B_sets"]["B3_median_based"] = df_to_list(b3)
    out["B_sets"]["B4_stability_first"] = df_to_list(b4)

    # Save JSON summary
    json_path = ARCHIVE / f"selections_summary_{int(cutoff*100)}_no_physionet.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)

    # Save compact MD summary
    md_path = ARCHIVE / f"SELECTIONS_{int(cutoff*100)}_no_physionet.md"
    lines = [f"# SELECTIONS — cutoff {cutoff} (no physionet)", ""]
    lines.append(f"- Median filter matches: {out['median_filter']['count']}")
    lines.append(f"- Mean filter matches: {out['mean_filter']['count']}")
    lines.append("")
    lines.append("## B1 — Mean-based (top 3)")
    for r in out["B_sets"]["B1_mean_based"]:
        lines.append(f"- {r.get('graph')} | {r.get('method')}: mean_mae={r.get('mean_mae')}")
    lines.append("")
    lines.append("## B2 — Real-only mean (top 3)")
    for r in out["B_sets"]["B2_real_mean"]:
        lines.append(f"- {r.get('graph')} | {r.get('method')}: mean_mae={r.get('mean_mae')}")
    lines.append("")
    lines.append("## B3 — Median-based (top 3)")
    for r in out["B_sets"]["B3_median_based"]:
        lines.append(f"- {r.get('graph')} | {r.get('method')}: median_mae={r.get('median_mae')}")
    lines.append("")
    lines.append("## B4 — Stability-first (top 3 by std_mae then mean_mae)")
    for r in out["B_sets"]["B4_stability_first"]:
        lines.append(f"- {r.get('graph')} | {r.get('method')}: std_mae={r.get('std_mae')} mean_mae={r.get('mean_mae')}")

    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return out


def write_normalization_note(path: Path) -> None:
    text = []
    text.append("# Physionet vs Synthetic scale note")
    text.append("")
    text.append("Investigation revealed a units/scale mismatch between synthetic datasets and the PhysioNet EEG data:")
    text.append("")
    text.append("- Synthetic generators (e.g. make_synthetic_alpha in experiments/run_canonical_experiment.py) produce sinusoids with amplitudes ~1.0 (noise ~0.08).")
    text.append("- PhysioNet loading (src/data/data_loader.py -> load_physionet_eegmmidb) returns raw EEG in Volts/microvolts (typical values ~1e-6), without rescaling.")
    text.append("")
    text.append("This causes MAE values from physionet rows to be orders of magnitude smaller than synthetic MAE, biasing global aggregations.")
    text.append("")
    text.append("Recommendation: either normalize per-dataset (e.g. z-score or scale to unit range) before computing MAE, or exclude physionet in cross-dataset aggregations. This run uses the latter (no physionet).")
    path.write_text("\n".join(text) + "\n", encoding="utf-8")


def main() -> None:
    summary_path = EXP / "analysis_it05_it20_summary_no_physionet.csv"
    if not summary_path.exists():
        print(f"ERROR: summary not found: {summary_path}")
        return

    df = load_summary(summary_path)
    # use only it05 aggregated rows (experiment == 'it05_no_physionet' if present)
    if "experiment" in df.columns and (df["experiment"] == "it05_no_physionet").any():
        df_it05 = df[df["experiment"] == "it05_no_physionet"].copy()
    else:
        df_it05 = df.copy()

    # canonical cutoffs
    for cutoff in (0.05, 0.20):
        print(f"Processing cutoff={cutoff} ...")
        select_and_export(df_it05, cutoff=cutoff)

    # write normalization note
    write_normalization_note(ARCHIVE / "PHYSIONET_NORMALIZATION_NOTE.md")

    print("Wrote selection artifacts to:", ARCHIVE)


if __name__ == "__main__":
    main()
