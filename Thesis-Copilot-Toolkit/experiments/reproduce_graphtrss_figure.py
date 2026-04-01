"""Reproduce a main GraphTRSS-style figure: MAE vs missing ratio.

The script builds a publication-style comparison between TRSS and baseline graph methods
across increasing missingness levels.
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.data.data_loader import load_synthetic_eeg, simulate_missing_channels
from src.evaluation import evaluate_signals
from src.graph_construction.graph_constructors import build_graph
from src.interpolation_methods import interpolate_signals


def ensure_results_dir() -> Path:
    root = Path(__file__).resolve().parents[1]
    out = root / "results"
    out.mkdir(parents=True, exist_ok=True)
    return out


def run() -> pd.DataFrame:
    data = load_synthetic_eeg(n_channels=22, n_times=300, random_state=123)
    signals = data["signals"]
    positions = data["positions"]

    graph = build_graph("aew", positions, signals=signals, k=5, sigma_dist=1.0, sigma_corr=0.5)
    adjacency = graph["adjacency"]
    if hasattr(adjacency, "toarray"):
        adjacency = adjacency.toarray()

    methods = {
        "trss": {"alpha": 0.8, "beta": 0.15, "n_iter": 120, "lr": 0.05},
        "graph_time_tikhonov": {"alpha": 0.7, "beta": 0.1},
        "tv": {"lam": 0.2, "n_iter": 30, "eps": 1e-5},
        "tikhonov": {"alpha": 0.5},
    }

    missing_levels = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]
    seeds = [1, 7, 13, 21, 42]

    rows = []
    for miss in missing_levels:
        for seed in seeds:
            masked = simulate_missing_channels(signals, missing_ratio=miss, random_state=seed)
            for method, params in methods.items():
                rec = interpolate_signals(method, masked, adjacency=adjacency, **params)
                met = evaluate_signals(signals, rec["reconstructed"], metrics=["mae", "rmse"])
                rows.append(
                    {
                        "missing_ratio": miss,
                        "seed": seed,
                        "method": method,
                        "mae": met["mae"],
                        "rmse": met["rmse"],
                    }
                )

    return pd.DataFrame(rows)


def save(df: pd.DataFrame, out_dir: Path) -> None:
    raw_csv = out_dir / "graphtrss_main_figure_raw.csv"
    summary_csv = out_dir / "graphtrss_main_figure_summary.csv"
    fig_path = out_dir / "graphtrss_main_figure.png"

    df.to_csv(raw_csv, index=False)

    summary = (
        df.groupby(["missing_ratio", "method"], as_index=False)
        .agg(mae_mean=("mae", "mean"), mae_std=("mae", "std"))
        .sort_values(["missing_ratio", "method"])
    )
    summary.to_csv(summary_csv, index=False)

    plt.figure(figsize=(10, 6))
    for method in summary["method"].unique():
        sub = summary[summary["method"] == method]
        plt.errorbar(
            sub["missing_ratio"],
            sub["mae_mean"],
            yerr=sub["mae_std"].fillna(0.0),
            marker="o",
            capsize=3,
            label=method,
        )

    plt.xlabel("Missing ratio")
    plt.ylabel("MAE")
    plt.title("GraphTRSS-style comparison: MAE vs Missing Ratio")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig(fig_path, dpi=200)
    plt.close()


if __name__ == "__main__":
    out = ensure_results_dir()
    df_res = run()
    save(df_res, out)
    print("Saved:", out / "graphtrss_main_figure_raw.csv")
    print("Saved:", out / "graphtrss_main_figure_summary.csv")
    print("Saved:", out / "graphtrss_main_figure.png")
