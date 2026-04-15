#!/usr/bin/env python3
"""Regenerate per-method summary using the no-physionet aggregated summary."""
from pathlib import Path
import pandas as pd

EXP = Path(__file__).resolve().parent
ARCH = EXP / "selections_archive_2026-04-14"
OUT_DIR = EXP / "selections_analysis"
OUT_DIR.mkdir(parents=True, exist_ok=True)


def main():
    src = EXP / "analysis_it05_it20_summary_no_physionet.csv"
    if not src.exists():
        print("Summary file not found:", src)
        return
    df = pd.read_csv(src)
    # use only it05 rows
    if "experiment" in df.columns and (df["experiment"] == "it05_no_physionet").any():
        df = df[df["experiment"] == "it05_no_physionet"].copy()

    per_method = (
        df.groupby("method", as_index=False)
        .agg(
            combos=("graph", "count"),
            mean_of_mean_mae=("mean_mae", "mean"),
            mean_of_median_mae=("median_mae", "mean"),
            mean_of_std_mae=("std_mae", "mean"),
        )
        .sort_values("mean_of_mean_mae")
    )

    out_csv = OUT_DIR / "per_method_summary_no_physionet.csv"
    per_method.to_csv(out_csv, index=False)
    print("Wrote:", out_csv)


if __name__ == "__main__":
    main()
