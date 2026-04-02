"""Run B2 benchmark in manageable batches and consolidate final full-scale artifacts."""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Dict, List

import pandas as pd

from experiments.optimize_and_benchmark import (
    build_stat_summary,
    build_topk_table,
    ensure_results_dir,
    run_benchmark,
)
from src.interpolation_warning_registry import summarize_registry


GRAPH_CHUNKS: List[List[str]] = [
    ["knn", "knng", "vknng"],
    ["gaussian", "nnk"],
    ["aew", "kalofolias"],
]

METHOD_CHUNKS: List[List[str]] = [
    ["linear", "idw", "rbfi_tps", "rbfi_mq", "spherical_spline"],
    ["gsp", "tikhonov", "bgsrp", "gsmooth"],
    ["graph_time_tikhonov", "trss", "tv"],
]


def _save_warns(records: List[Dict[str, object]], path: Path) -> None:
    if not records:
        pd.DataFrame(
            columns=["method", "warning_code", "severity", "decision", "count", "sample_message"]
        ).to_csv(path, index=False)
        return
    pd.DataFrame(records).to_csv(path, index=False)


def main() -> None:
    out_dir = ensure_results_dir()

    include_mne = os.environ.get("INCLUDE_MNE", "1") == "1"
    max_time_samples = int(os.environ.get("MAX_TIME_SAMPLES", "220"))
    missing_levels = [float(x) for x in os.environ.get("B2_MISSING_LEVELS", "0.10,0.20,0.30,0.40").split(",")]
    random_seed = int(os.environ.get("B2_RANDOM_SEED", "42"))
    top_k = int(os.environ.get("B2_TOP_K", "3"))

    all_rows: List[pd.DataFrame] = []
    all_warns: List[pd.DataFrame] = []
    batch_index = 0

    for graphs in GRAPH_CHUNKS:
        for methods in METHOD_CHUNKS:
            batch_index += 1
            os.environ["B2_GRAPH_NAMES"] = ",".join(graphs)
            os.environ["B2_METHOD_NAMES"] = ",".join(methods)

            print(f"[B2] Batch {batch_index}: graphs={graphs} methods={methods}")
            df, _ = run_benchmark(
                include_mne=include_mne,
                max_time_samples=max_time_samples,
                missing_levels=missing_levels,
                random_seed=random_seed,
            )

            batch_raw = out_dir / f"opt_benchmark_b2_batch_{batch_index:02d}_raw.csv"
            df.to_csv(batch_raw, index=False)
            all_rows.append(df)

            batch_warn = out_dir / f"opt_benchmark_b2_batch_{batch_index:02d}_warnings.csv"
            warn_records = summarize_registry(reset=True)
            _save_warns(warn_records, batch_warn)
            all_warns.append(pd.read_csv(batch_warn))

    merged = pd.concat(all_rows, ignore_index=True) if all_rows else pd.DataFrame()
    merged_raw = out_dir / "opt_benchmark_b2_full_scale_raw.csv"
    merged.to_csv(merged_raw, index=False)

    summary = build_stat_summary(merged)
    summary_path = out_dir / "opt_benchmark_b2_full_scale_summary.csv"
    summary.to_csv(summary_path, index=False)

    cfg = {
        "mode": "batched_full_scale",
        "include_mne": include_mne,
        "max_time_samples": max_time_samples,
        "missing_levels": missing_levels,
        "random_seed": random_seed,
        "top_k": top_k,
        "graph_chunks": GRAPH_CHUNKS,
        "method_chunks": METHOD_CHUNKS,
        "rows": int(len(merged)),
    }
    cfg_path = out_dir / "opt_benchmark_b2_full_scale_config.json"
    cfg_path.write_text(json.dumps(cfg, indent=2), encoding="utf-8")

    ranking = summary.sort_values(["mae_mean", "rmse_mean", "dtw_mean", "snr_mean"], ascending=[True, True, True, False])
    ranking_path = out_dir / "opt_benchmark_b2_full_scale_ranking_final.csv"
    ranking.to_csv(ranking_path, index=False)

    topk = build_topk_table(summary, top_k=top_k)
    topk_path = out_dir / "opt_benchmark_b2_full_scale_topk_by_family_scenario.csv"
    topk.to_csv(topk_path, index=False)

    warns = pd.concat(all_warns, ignore_index=True) if all_warns else pd.DataFrame()
    warns_summary = (
        warns.groupby(["method", "warning_code", "severity", "decision"], as_index=False)
        .agg(count=("count", "sum"), sample_message=("sample_message", "first"))
        if not warns.empty
        else pd.DataFrame(columns=["method", "warning_code", "severity", "decision", "count", "sample_message"])
    )
    warns_path = out_dir / "opt_benchmark_b2_full_scale_warnings_registry.csv"
    warns_summary.to_csv(warns_path, index=False)

    print(f"Saved: {merged_raw}")
    print(f"Saved: {summary_path}")
    print(f"Saved: {cfg_path}")
    print(f"Saved: {ranking_path}")
    print(f"Saved: {topk_path}")
    print(f"Saved: {warns_path}")


if __name__ == "__main__":
    main()
