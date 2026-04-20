import os
import numpy as np
import pytest


ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in __import__("sys").path:
    __import__("sys").path.insert(0, ROOT)

from src.graph_construction.graph_constructors import build_graph


@pytest.mark.skipif(
    not os.path.exists("tests/fixtures/visibility/adjacency.npy"),
    reason="MATLAB fixtures not found: place fixtures under tests/fixtures/visibility/",
)
def test_compare_with_matlab_fixtures():
    # Load fixtures produced by MATLAB (expected shape and numeric arrays)
    outdir = "tests/fixtures/visibility"
    F_m = np.load(os.path.join(outdir, "F.npy"))
    G_m = np.load(os.path.join(outdir, "G.npy"))
    adj_m = np.load(os.path.join(outdir, "adjacency.npy"))

    # Build from Python and compare shapes
    signals = np.load(os.path.join(outdir, "input_signals.npy")) if os.path.exists(os.path.join(outdir, "input_signals.npy")) else None
    assert signals is not None, "Provide input_signals.npy alongside fixtures for reproducibility"

    res = build_graph("visibility_nnk", signals=signals, k=F_m.shape[0])
    adj_py = res.get("adjacency")
    assert adj_py.shape == adj_m.shape

    # Numerical comparison with tolerance (paper-faithful may require relaxed tol)
    np.testing.assert_allclose(adj_py, adj_m, rtol=1e-6, atol=1e-6)
