"""Verify BGSRP behavior against Narang-style interpolation baselines.

This script does not claim BGSRP is a Narang method.
Instead, it benchmarks BGSRP (RKHS, Zhang et al.) against Narang-family methods
(`gsp`, `tikhonov`, `gsmooth`) on the same synthetic setup to verify practical consistency.
"""

from __future__ import annotations

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
    root = Path(__file__).resolve().parents[1]
    out = root / "results"
    out.mkdir(parents=True, exist_ok=True)
    return out


def make_bandlimited_signal(signals: np.ndarray, adjacency: np.ndarray, bandwidth: int) -> np.ndarray:
    """Project synthetic signal to low graph frequencies to emulate Narang assumptions."""
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
    data = load_synthetic_eeg(n_channels=22, n_times=260, random_state=42)
    signals = data["signals"]
    positions = data["positions"]

    graph = build_graph("knng", positions, signals=signals, k=6, sigma=1.0)
    adjacency = graph["adjacency"]
    if hasattr(adjacency, "toarray"):
        adjacency = adjacency.toarray()

    # Narang-style setup: evaluate on a graph-bandlimited signal.
    bandlimited = make_bandlimited_signal(signals, adjacency, bandwidth=8)

    methods = [
        ("gsp", {}),
        ("tikhonov", {"alpha": 0.5}),
        ("gsmooth", {"lam": 0.5, "n_iter": 50}),
        ("bgsrp", {"bandwidth": 8, "gamma": 0.1}),
    ]

    rows = []
    for seed in [1, 7, 13, 21, 42]:
        masked = simulate_missing_channels(bandlimited, missing_ratio=0.2, random_state=seed)
        for method, params in methods:
            rec = interpolate_signals(method, masked, adjacency=adjacency, **params)
            met = evaluate_signals(bandlimited, rec["reconstructed"], metrics=["mae", "rmse", "snr"])
            rows.append(
                {
                    "seed": seed,
                    "method": method,
                    "params": str(params),
                    "mae": met["mae"],
                    "rmse": met["rmse"],
                    "snr": met["snr"],
                    "reference_family": "Narang" if method in {"gsp", "tikhonov", "gsmooth"} else "Zhang_RKHS",
                }
            )

    return pd.DataFrame(rows)


def save(df: pd.DataFrame, out_dir: Path) -> None:
    out_csv = out_dir / "bgsrp_vs_narang_check.csv"
    out_summary = out_dir / "bgsrp_vs_narang_check_summary.csv"

    df.to_csv(out_csv, index=False)
    summary = (
        df.groupby(["method", "reference_family"], as_index=False)
        .agg(mae_mean=("mae", "mean"), mae_std=("mae", "std"), rmse_mean=("rmse", "mean"), snr_mean=("snr", "mean"))
        .sort_values("mae_mean")
    )
    summary.to_csv(out_summary, index=False)


if __name__ == "__main__":
    out_dir = ensure_results_dir()
    df_res = run()
    save(df_res, out_dir)
    print(df_res.groupby("method")["mae"].mean().sort_values())
    print(f"Saved: {out_dir / 'bgsrp_vs_narang_check.csv'}")
    print(f"Saved: {out_dir / 'bgsrp_vs_narang_check_summary.csv'}")
