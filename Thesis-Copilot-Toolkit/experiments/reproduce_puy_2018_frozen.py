"""Frozen-configuration Puy-2018-style reconstruction audit.

Reference target:
- Puy et al. (2018), random sampling of bandlimited graph signals.

This script freezes a synthetic protocol and evaluates reconstruction quality
for puy vs gsp under varying missing ratios.
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
    data = load_synthetic_eeg(n_channels=48, n_times=300, random_state=11)
    signals = data["signals"]
    positions = data["positions"]

    graph = build_graph("knng", positions, signals=signals, k=6, sigma=1.0)
    adjacency = graph["adjacency"]
    if hasattr(adjacency, "toarray"):
        adjacency = adjacency.toarray()

    bandwidth = 12
    methods = [
        ("puy", {"alpha": 0.5}),
        ("gsp", {}),
    ]

    missing_ratios = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]
    seeds = [1, 7, 13, 21, 42, 77, 101]

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
    raw = out_dir / "puy_2018_frozen_raw.csv"
    summary = out_dir / "puy_2018_frozen_summary.csv"
    cfg = out_dir / "puy_2018_frozen_config.json"

    df.to_csv(raw, index=False)
    agg = (
        df.groupby(["missing_ratio", "method"], as_index=False)
        .agg(mae_mean=("mae", "mean"), mae_std=("mae", "std"), rmse_mean=("rmse", "mean"), snr_mean=("snr", "mean"))
        .sort_values(["missing_ratio", "mae_mean"])
    )
    agg.to_csv(summary, index=False)

    config = {
        "reference": "Puy et al. 2018",
        "graph_method": "knng",
        "graph_params": {"k": 6, "sigma": 1.0},
        "bandwidth": 12,
        "missing_ratios": [0.1, 0.2, 0.3, 0.4, 0.5, 0.6],
        "seeds": [1, 7, 13, 21, 42, 77, 101],
        "methods": ["puy", "gsp"],
    }
    with open(cfg, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=2)


if __name__ == "__main__":
    out = ensure_results_dir()
    df_res = run()
    save(df_res, out)
    print(f"Saved: {out / 'puy_2018_frozen_raw.csv'}")
    print(f"Saved: {out / 'puy_2018_frozen_summary.csv'}")
    print(f"Saved: {out / 'puy_2018_frozen_config.json'}")
