"""Robustness run over top-10 combinations from optimization results."""

from __future__ import annotations

import ast
import os
from pathlib import Path

import pandas as pd

from src.data.data_loader import load_mne_sample_dataset, load_synthetic_eeg, simulate_missing_channels
from src.evaluation import evaluate_signals
from src.graph_construction.graph_constructors import build_graph
from src.interpolation_methods import interpolate_signals


GRAPH_BASED = {
    "gsp",
    "tikhonov",
    "bgsrp",
    "gsmooth",
    "graph_time_tikhonov",
    "trss",
    "tv",
    "puy",
    "sobolev",
}

POSITION_BASED = {
    "idw",
    "spherical_spline",
    "rbfi_tps",
    "rbfi_mq",
    "spline_surface",
}


def parse_dict(s: str) -> dict:
    if isinstance(s, dict):
        return s
    if not isinstance(s, str) or s.strip() == "":
        return {}
    try:
        return dict(ast.literal_eval(s))
    except Exception:
        return {}


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    results_dir = root / "results"
    rank_path = results_dir / "opt_benchmark_rank_all.csv"
    if not rank_path.exists():
        raise FileNotFoundError(f"No existe {rank_path}. Ejecuta optimize_and_benchmark.py primero.")

    top_n = int(os.environ.get("TOP_N", "10"))
    max_time_samples = int(os.environ.get("MAX_TIME_SAMPLES", "400"))
    seeds = [1, 7, 13, 21, 42]

    rank = pd.read_csv(rank_path)
    top = rank.head(top_n).copy()

    datasets = {
        "synthetic": lambda: load_synthetic_eeg(n_channels=22, n_times=max_time_samples, random_state=42),
        "mne_sample": load_mne_sample_dataset,
    }

    rows = []
    for _, row in top.iterrows():
        graph_name = row["graph"]
        method = row["method"]
        gparams = parse_dict(row.get("graph_params", "{}"))
        mparams = parse_dict(row.get("method_params", "{}"))

        for ds_name, loader in datasets.items():
            sample = loader()
            signals = sample["signals"]
            positions = sample["positions"]
            if signals.shape[0] > max_time_samples:
                signals = signals[:max_time_samples]

            try:
                graph = build_graph(graph_name, positions, signals=signals, **gparams)
                adjacency = graph["adjacency"]
                if hasattr(adjacency, "toarray"):
                    adjacency = adjacency.toarray()
            except Exception as exc:
                print(f"[WARN] graph failed {graph_name}/{ds_name}: {exc}")
                continue

            for seed in seeds:
                masked = simulate_missing_channels(signals, missing_ratio=0.2, random_state=seed)
                try:
                    if method in GRAPH_BASED:
                        rec = interpolate_signals(method, masked, adjacency=adjacency, **mparams)
                    elif method in POSITION_BASED:
                        rec = interpolate_signals(method, masked, positions=positions, **mparams)
                    else:
                        rec = interpolate_signals(method, masked, **mparams)

                    met = evaluate_signals(signals, rec["reconstructed"], metrics=["mae", "rmse", "snr"])
                    rows.append(
                        {
                            "dataset": ds_name,
                            "seed": seed,
                            "graph": graph_name,
                            "graph_params": str(gparams),
                            "method": method,
                            "method_params": str(mparams),
                            "mae": met["mae"],
                            "rmse": met["rmse"],
                            "snr": met["snr"],
                        }
                    )
                except Exception as exc:
                    print(f"[WARN] method failed {method}/{ds_name}/seed={seed}: {exc}")
                    continue

    out = pd.DataFrame(rows)
    out_csv = results_dir / "robust_top10_runs.csv"
    out.to_csv(out_csv, index=False)

    if not out.empty:
        summary = (
            out.groupby(["dataset", "graph", "method", "graph_params", "method_params"], as_index=False)
            .agg(mae_mean=("mae", "mean"), mae_std=("mae", "std"), rmse_mean=("rmse", "mean"), snr_mean=("snr", "mean"))
            .sort_values("mae_mean")
        )
        summary.to_csv(results_dir / "robust_top10_summary.csv", index=False)
        print(summary.head(20).to_string(index=False))

    print(f"Saved robustness outputs in: {results_dir}")


if __name__ == "__main__":
    main()
