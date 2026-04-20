Smoke test and replication instructions for `visibility_graphs` / `visibility_nnk`

Prerequisites:
- Python 3.8+ with `numpy`, `scipy`, and `pytest` installed in your environment.
- Ensure the repository root is the current working directory.

Quick smoke test (from repo root):

```powershell
# Run the quick script (Windows):
python "Thesis-Copilot-Toolkit/tmp_test_visibility.py"
# or with the py launcher if needed:
py -3 "Thesis-Copilot-Toolkit/tmp_test_visibility.py"
```

Run the new unit + smoke tests for visibility methods:

```powershell
pip install -r "Code1201\PyNNK_graph_construction\requirements.txt"  # optional: PyNNK deps
pip install pytest
python -m pytest Thesis-Copilot-Toolkit/tests/test_visibility_graphs.py -q
```

Usage patterns (examples)

1) Explicit graph-construction (recommended for testing / fixtures):

```python
from src.graph_construction.graph_constructors import build_graph
from src.interpolation_methods import interpolate_trss

# signals: numpy array with shape (n_t, n_ch)
bg = build_graph("visibility_nnk", signals=signals, k=4, use_hvg=True, reg=1e-6)
adjacency = bg["adjacency"]
recon = interpolate_trss(signals, adjacency=adjacency, alpha=0.55, beta=0.2, n_iter=120)
```

2) Convenience wrapper (one-shot):

```python
from src.interpolation_methods import interpolate_visibility_graphs

# When adjacency is None, the wrapper calls build_graph('visibility_nnk') internally
recon = interpolate_visibility_graphs(signals, adjacency=None, alpha=0.55, beta=0.2, n_iter=100)
```

Notes:
- The implementation first attempts to call the local `Code1201/PyNNK_graph_construction/graph_construction.py` NNK solver. If that module is not available or import fails, it falls back to an internal NNLS-based local NNK implementation.
- For strict, paper-faithful replication you should provide MATLAB fixtures (features, kernel `G`, NNK adjacency, reconstruction) produced by the original MATLAB demos. The preferred workflow is to produce and store these fixtures under `tests/fixtures/` and add numeric comparison tests.

Reproducibility and next steps:
- I can add a minimal `requirements.txt` or `Dockerfile` to lock reproducible dependencies.
- I can add a small CLI runner that runs `visibility_nnk`→saves `F.npy`, `G.npy`, `adjacency.npy`→runs `TRSS` and saves `recon.npy` for cross-checking with MATLAB fixtures.
