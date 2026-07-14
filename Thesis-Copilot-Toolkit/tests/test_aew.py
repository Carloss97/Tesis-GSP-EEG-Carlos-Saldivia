import os
import sys
import numpy as np

# Ensure the package `src` inside Thesis-Copilot-Toolkit is importable when running pytest
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from src.graph_construction.graph_constructors import build_graph


def test_aew_smoke():
    rng = np.random.default_rng(0)
    n_t = 12
    n_ch = 6
    signals = rng.standard_normal(size=(n_t, n_ch))

    res = build_graph("aew", signals=signals, k=3, sigma="median", max_iter=3)
    adj = np.asarray(res["adjacency"])

    assert adj.shape == (n_ch, n_ch)
    assert adj.min() >= -1e-12
    assert np.allclose(adj, adj.T, atol=1e-8)
    assert np.allclose(np.diag(adj), 0.0, atol=1e-12)
