"""Frozen-configuration Narang-2013-style interpolation reproduction.

Reference target:
- Narang et al. (2013) interpolation in graph structured data.

The script freezes protocol and parameters for gsp/tikhonov/gsmooth comparison
on graph-bandlimited synthetic signals.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

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
    out = ROOT / "results"
    out.mkdir(parents=True, exist_ok=True)
    return out


def make_bandlimited_signal(signals: np.ndarray, adjacency: np.ndarray, bandwidth: int) -> np.ndarray:
    from scipy.sparse import csgraph

    lap = csgraph.laplacian(adjacency, normed=False)
    _, u = np.linalg.eigh(lap)
    k = int(np.clip(bandwidth, 2, u.shape[1] - 1))
    u_k = u[:, :k]

    projected = np.zeros_like(signals)
    for t in range(signals.shape[0]):
        y = signals[t]
        coeffs, *_ = np.linalg.lstsq(u_k, y, rcond=None)
        projected[t] = u_k @ coeffs
    return projected


def run() -> pd.DataFrame:
    data = load_synthetic_eeg(n_channels=64, n_times=320, random_state=7)
    signals = data["signals"]
    positions = data["positions"]

    graph = build_graph("knng", positions, signals=signals, k=8, sigma=0.9)
    adjacency = graph["adjacency"]
    if hasattr(adjacency, "toarray"):
        adjacency = adjacency.toarray()

    bandwidth = 16
    methods = [
        ("gsp", {}),
        ("tikhonov", {"alpha": 0.5}),
        ("gsmooth", {"lam": 0.5, "n_iter": 50}),
    ]

    missing_ratios = [0.1, 0.2, 0.3, 0.4, 0.5]
    seeds = [1, 7, 13, 21, 42]

    bandlimited = make_bandlimited_signal(signals, adjacency=adjacency, bandwidth=bandwidth)

    rows = []
    for miss in missing_ratios:
        for seed in seeds:
            masked = simulate_missing_channels(bandlimited, missing_ratio=miss, random_state=seed)
            for method, params in methods:
                rec = interpolate_signals(method, masked, adjacency=adjacency, **params)
                met = evaluate_signals(bandlimited, rec["reconstructed"], metrics=["mae", "rmse", "snr"])
                rows.append(
                    {
                        "missing_ratio": miss,
                        "seed": seed,
                        "method": method,
                        "params": str(params),
                        "mae": met["mae"],
                        "rmse": met["rmse"],
                        "snr": met["snr"],
                    }
                )

    return pd.DataFrame(rows)


def save(df: pd.DataFrame, out_dir: Path) -> None:
    raw = out_dir / "narang_2013_frozen_raw.csv"
    summary = out_dir / "narang_2013_frozen_summary.csv"
    cfg = out_dir / "narang_2013_frozen_config.json"

    df.to_csv(raw, index=False)
    agg = (
        df.groupby(["missing_ratio", "method"], as_index=False)
        .agg(mae_mean=("mae", "mean"), mae_std=("mae", "std"), rmse_mean=("rmse", "mean"), snr_mean=("snr", "mean"))
        .sort_values(["missing_ratio", "mae_mean"])
    )
    agg.to_csv(summary, index=False)

    config = {
        "reference": "Narang et al. 2013",
        "graph_method": "knng",
        "graph_params": {"k": 8, "sigma": 0.9},
        "bandwidth": 16,
        "missing_ratios": [0.1, 0.2, 0.3, 0.4, 0.5],
        "seeds": [1, 7, 13, 21, 42],
        "methods": ["gsp", "tikhonov", "gsmooth"],
    }
    with open(cfg, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=2)


if __name__ == "__main__":
    out = ensure_results_dir()
    df_res = run()
    save(df_res, out)
    print(f"Saved: {out / 'narang_2013_frozen_raw.csv'}")
    print(f"Saved: {out / 'narang_2013_frozen_summary.csv'}")
    print(f"Saved: {out / 'narang_2013_frozen_config.json'}")
