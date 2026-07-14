import os
import sys
import numpy as np

# Ensure the package `src` inside Thesis-Copilot-Toolkit is importable when running pytest
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from src.graph_construction.graph_constructors import build_graph
from src.interpolation_methods import interpolate_visibility_graphs


def make_synthetic(n_t: int = 12, n_ch: int = 6, random_state: int = 0) -> np.ndarray:
    rng = np.random.default_rng(random_state)
    t = np.linspace(0, 2 * np.pi, n_t)
    base = np.sin(t)
    signals = np.zeros((n_t, n_ch), dtype=float)
    for ch in range(n_ch):
        signals[:, ch] = base * (1.0 + 0.05 * ch) + 0.02 * rng.normal(size=n_t)

    # inject some NaNs to exercise imputation paths
    signals[2, [1, 3]] = np.nan
    signals[5, [2]] = np.nan
    return signals


def test_build_visibility_nnk_basic():
    signals = make_synthetic()
    res = build_graph("visibility_nnk", signals=signals, k=3)
    assert isinstance(res, dict)
    adj = res.get("adjacency")
    info = res.get("info", {})
    assert adj is not None
    adj = np.asarray(adj)
    n_ch = signals.shape[1]
    assert adj.shape == (n_ch, n_ch)
    # symmetry
    assert np.allclose(adj, adj.T, atol=1e-8)
    # non-negative and zero diagonal
    assert adj.min() >= -1e-12
    assert np.allclose(np.diag(adj), 0.0, atol=1e-12)
    assert info.get("method") == "visibility_nnk"


def test_visibility_graphs_e2e_smoke():
    signals = make_synthetic()
    # small number of iterations to keep smoke test fast
    reconstructed = interpolate_visibility_graphs(signals, adjacency=None, alpha=0.55, beta=0.2, n_iter=5)
    assert reconstructed.shape == signals.shape
    # TRSS should fill missing values
    assert not np.isnan(reconstructed).any()
import numpy as np
import pytest

try:
    from src.interpolation_methods import interpolate_visibility_graphs
except Exception:
    interpolate_visibility_graphs = None


@pytest.mark.skipif(interpolate_visibility_graphs is None, reason="interpolate_visibility_graphs not importable")
def test_visibility_smoke():
    n_t = 60
    n_ch = 8
    rng = np.random.default_rng(0)
    t = np.linspace(0, 1, n_t)
    signals = np.stack([
        np.sin(2 * np.pi * (5 + i * 0.5) * t) + 0.01 * rng.normal(size=n_t)
        for i in range(n_ch)
    ], axis=1)

    masked = signals.copy()
    masked[10:20, 2] = np.nan
    masked[30:40, 5] = np.nan

    rec = interpolate_visibility_graphs(masked, adjacency=np.eye(n_ch), n_iter=3)
    assert rec.shape == signals.shape
    assert np.isfinite(rec).all()
    assert int(np.isnan(rec).sum()) == 0
