"""Replicate BGSRP exfig4-style timing experiment with frozen configuration.

Reference target:
- Papers/Code-for-BGSRP-master/gsp_BGSRP_recon_exfig4.m

This Python version is sensor-graph-like (random geometric graph), fixed-label setup,
and fixed BGSRP params (labs=400, bandwidth=400, gamma=0.1), matching the MATLAB script
as closely as possible in this repository environment.
"""

from __future__ import annotations

import json
import os
import sys
import time
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.graph_construction.graph_constructors import build_graph
from src.interpolation_methods import interpolate_signals


def ensure_results_dir() -> Path:
    out = ROOT / "results"
    out.mkdir(parents=True, exist_ok=True)
    return out


def make_sensor_like_graph(n_nodes: int, seed: int) -> tuple[np.ndarray, np.ndarray]:
    rng = np.random.default_rng(seed)
    positions = rng.random((n_nodes, 2))
    graph = build_graph("knng", positions, k=min(10, n_nodes - 1), sigma=0.2)
    adjacency = graph["adjacency"]
    if hasattr(adjacency, "toarray"):
        adjacency = adjacency.toarray()
    return positions, adjacency


def make_bandlimited_signal(adjacency: np.ndarray, seed: int, frac: float = 1 / 8) -> np.ndarray:
    from scipy.sparse import csgraph

    rng = np.random.default_rng(seed)
    n = adjacency.shape[0]
    lap = csgraph.laplacian(adjacency, normed=False)
    _, u = np.linalg.eigh(lap)

    k = max(2, int(n * frac))
    x = 2.0 * rng.random(n) - 1.0
    fx = u.T @ x
    f = u[:, :k] @ fx[:k]
    return f


def run() -> pd.DataFrame:
    nodes = [int(x) for x in os.environ.get("BGSRP_N_LIST", "800,1200,1600,2000,2400,2800,3200,3600,4000").split(",")]
    n_runs = int(os.environ.get("BGSRP_N_RUNS", "50"))
    labs = int(os.environ.get("BGSRP_LABS", "400"))
    bandw = int(os.environ.get("BGSRP_BANDW", "400"))
    gamma = float(os.environ.get("BGSRP_GAMMA", "0.1"))

    rows = []
    for n in nodes:
        if n <= max(labs, bandw):
            continue

        positions, adjacency = make_sensor_like_graph(n_nodes=n, seed=0)
        for run_id in range(n_runs):
            f = make_bandlimited_signal(adjacency, seed=run_id, frac=1 / 8)
            rng = np.random.default_rng(run_id)
            p = rng.permutation(n)
            x0 = p[:labs]

            signal_row = np.full((1, n), np.nan, dtype=float)
            signal_row[0, x0] = f[x0]

            t1 = time.perf_counter()
            rec = interpolate_signals("bgsrp", signal_row, adjacency=adjacency, bandwidth=bandw, gamma=gamma)
            t2 = time.perf_counter()

            xhat = rec["reconstructed"][0]
            rows.append(
                {
                    "n_nodes": n,
                    "run": run_id,
                    "labs": labs,
                    "bandwidth": bandw,
                    "gamma": gamma,
                    "elapsed_sec": t2 - t1,
                    "mae": float(np.mean(np.abs(xhat - f))),
                }
            )

    return pd.DataFrame(rows)


def save(df: pd.DataFrame, out_dir: Path) -> None:
    raw = out_dir / "bgsrp_exfig4_like_raw.csv"
    summary = out_dir / "bgsrp_exfig4_like_summary.csv"
    cfg = out_dir / "bgsrp_exfig4_like_config.json"

    config = {
        "source": "Papers/Code-for-BGSRP-master/gsp_BGSRP_recon_exfig4.m",
        "notes": "Python sensor-like approximation with frozen config",
        "nodes": sorted(df["n_nodes"].unique().tolist()) if not df.empty else [],
        "n_runs": int(df["run"].max() + 1) if not df.empty else 0,
        "labs": int(df["labs"].iloc[0]) if not df.empty else None,
        "bandwidth": int(df["bandwidth"].iloc[0]) if not df.empty else None,
        "gamma": float(df["gamma"].iloc[0]) if not df.empty else None,
    }

    df.to_csv(raw, index=False)
    if not df.empty:
        agg = (
            df.groupby("n_nodes", as_index=False)
            .agg(
                elapsed_mean_sec=("elapsed_sec", "mean"),
                elapsed_std_sec=("elapsed_sec", "std"),
                mae_mean=("mae", "mean"),
                mae_std=("mae", "std"),
            )
            .sort_values("n_nodes")
        )
        agg.to_csv(summary, index=False)
    else:
        pd.DataFrame().to_csv(summary, index=False)

    with open(cfg, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=2)


if __name__ == "__main__":
    out = ensure_results_dir()
    df_res = run()
    save(df_res, out)
    print(f"Saved: {out / 'bgsrp_exfig4_like_raw.csv'}")
    print(f"Saved: {out / 'bgsrp_exfig4_like_summary.csv'}")
    print(f"Saved: {out / 'bgsrp_exfig4_like_config.json'}")
