"""Microbenchmarks: measure latency (ms) of selected interpolation methods.

Saves results to: results/tablas_resumen/phase2_microbench_latency.csv
and a short human-readable note to .agent_work/PHASE2_MICROBENCH.txt
"""
from pathlib import Path
import time
import numpy as np
import pandas as pd

import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src.interpolation_methods import interpolate_signals

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "results" / "tablas_resumen"
OUT_DIR.mkdir(parents=True, exist_ok=True)
OUT_CSV = OUT_DIR / "phase2_microbench_latency.csv"
OUT_TXT = ROOT / ".agent_work" / "PHASE2_MICROBENCH.txt"
OUT_TXT.parent.mkdir(parents=True, exist_ok=True)


def make_fixture(n_t=50, n_ch=64, missing_ratio=0.1, seed=42):
    rng = np.random.default_rng(seed)
    signals = rng.normal(size=(n_t, n_ch)).astype(float)
    # introduce missing channels per sample (random positions)
    mask = rng.random(size=signals.shape) < missing_ratio
    signals[mask] = np.nan

    # adjacency: symmetric positive weights (simple RBF on random positions)
    pos = rng.normal(size=(n_ch, 3))
    pos = pos / np.linalg.norm(pos, axis=1, keepdims=True)
    d = np.linalg.norm(pos[:, None, :] - pos[None, :, :], axis=2)
    sigma = np.median(d)
    adjacency = np.exp(-(d**2) / (2 * (sigma**2 + 1e-12)))
    np.fill_diagonal(adjacency, 0.0)

    return signals, adjacency, pos


def time_method(method, signals, adjacency=None, positions=None, repeats=3):
    times = []
    for _ in range(repeats):
        t0 = time.perf_counter()
        try:
            if method in {"linear", "nearest", "mean", "random"}:
                interpolate_signals(method, signals)
            elif method in {"idw", "rbfi_tps", "spherical_spline"}:
                interpolate_signals(method, signals, positions=positions)
            else:
                interpolate_signals(method, signals, adjacency=adjacency)
        except Exception as e:
            return None, str(e)
        t1 = time.perf_counter()
        times.append((t1 - t0) * 1000.0)
    return float(np.median(times)), None


def main():
    signals, adjacency, positions = make_fixture()
    methods = [
        "linear",
        "nearest",
        "mean",
        "idw",
        "rbfi_tps",
        "spherical_spline",
        "ica",
        "tikhonov",
        "bgsrp",
        "trss",
        "tv",
        "temporal_laplacian",
        "sobolev",
        "visibility_nnk",
    ]

    rows = []
    for m in methods:
        ms, err = time_method(m, signals, adjacency=adjacency, positions=positions, repeats=3)
        if ms is None:
            rows.append({"method": m, "median_ms": None, "error": err})
        else:
            rows.append({"method": m, "median_ms": ms, "error": None})

    df = pd.DataFrame(rows)
    df.to_csv(OUT_CSV, index=False)

    txt = ["Phase 2 microbench results\n"]
    for _, r in df.iterrows():
        if pd.isna(r.median_ms):
            txt.append(f"{r.method}: ERROR -> {r.error}\n")
        else:
            txt.append(f"{r.method}: median {r.median_ms:.2f} ms per call\n")
    OUT_TXT.write_text("".join(txt), encoding="utf-8")
    print(f"Wrote microbench CSV to {OUT_CSV}")
    print(f"Wrote microbench summary to {OUT_TXT}")


if __name__ == '__main__':
    main()
