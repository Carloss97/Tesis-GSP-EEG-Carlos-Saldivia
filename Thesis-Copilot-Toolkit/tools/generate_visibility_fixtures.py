"""Generate visibility graph fixtures (features, kernel, adjacency, recon).

Usage:
  python tools/generate_visibility_fixtures.py --outdir tests/fixtures/visibility --input data.npy
If input is not provided, a synthetic signal is generated.
"""
from __future__ import annotations

import argparse
import os
import numpy as np


def make_synthetic(n_t=60, n_ch=16, seed=0):
    rng = np.random.default_rng(seed)
    t = np.linspace(0, 2 * np.pi, n_t)
    base = np.sin(t)
    signals = np.zeros((n_t, n_ch), dtype=float)
    for ch in range(n_ch):
        signals[:, ch] = base * (1.0 + 0.03 * ch) + 0.02 * rng.normal(size=n_t)
    # inject NaNs
    signals[2, [1, 3]] = np.nan
    signals[5, [2]] = np.nan
    return signals


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--input", help="Input .npy file with signals (n_t, n_ch)")
    p.add_argument("--outdir", default="tests/fixtures/visibility", help="Output folder for fixtures")
    p.add_argument("--k", type=int, default=4)
    args = p.parse_args()

    outdir = args.outdir
    os.makedirs(outdir, exist_ok=True)

    if args.input:
        signals = np.load(args.input)
    else:
        signals = make_synthetic()

    # Import locally to avoid heavy imports when not used
    from src.graph_construction.graph_constructors import build_graph
    from src.interpolation_methods import interpolate_trss

    print("Building visibility_nnk adjacency...")
    bg = build_graph("visibility_nnk", signals=signals, k=args.k, use_hvg=False)
    adjacency = bg.get("adjacency")
    info = bg.get("info", {})

    # Save adjacency
    np.save(os.path.join(outdir, "adjacency.npy"), adjacency)
    np.save(os.path.join(outdir, "info.npy"), np.array([str(info)]))

    # Save features and kernel if present (recompute here to capture intermediate arrays)
    # Recompute features: same logic as build_graph
    from scipy.spatial.distance import cdist

    # Extract features as in build_graph
    n_t, n_ch = signals.shape
    F = np.zeros((n_ch, 4), dtype=float)
    from src.graph_construction.graph_constructors import nvg_adjacency

    for ch in range(n_ch):
        s = signals[:, ch].copy()
        if np.isnan(s).all():
            s[:] = 0.0
        else:
            m = np.nanmean(s)
            s[np.isnan(s)] = m
        adj_t = nvg_adjacency(s)
        deg = adj_t.sum(axis=0).astype(float)
        clust = np.zeros(n_t, dtype=float)
        for ti in range(n_t):
            nbr = np.where(adj_t[ti] > 0)[0]
            k_i = nbr.size
            if k_i < 2:
                clust[ti] = 0.0
            else:
                sub = adj_t[np.ix_(nbr, nbr)].astype(float)
                E = sub.sum() / 2.0
                clust[ti] = (2.0 * E) / (k_i * (k_i - 1))
        F[ch, 0] = float(np.mean(deg))
        F[ch, 1] = float(np.std(deg))
        F[ch, 2] = float(np.nanmean(clust))
        F[ch, 3] = float(np.nanstd(clust))

    dmat = cdist(F, F, metric="euclidean")
    vals = dmat[np.triu_indices(n_ch, k=1)]
    vals = vals[vals > 0]
    sigma = float(np.median(vals)) if vals.size > 0 else 1.0
    G = np.exp(-(dmat ** 2) / (2.0 * sigma ** 2))
    np.fill_diagonal(G, np.max(G))

    np.save(os.path.join(outdir, "F.npy"), F)
    np.save(os.path.join(outdir, "G.npy"), G)

    # Run TRSS reconstructor to save reconstruction
    print("Running TRSS reconstructor (short run)...")
    recon = interpolate_trss(signals, adjacency=adjacency, alpha=0.55, beta=0.2, n_iter=50, lr=0.05)
    np.save(os.path.join(outdir, "recon.npy"), recon)

    print("Fixtures saved to:", outdir)


if __name__ == "__main__":
    main()
