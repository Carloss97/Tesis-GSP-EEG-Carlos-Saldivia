# PR Draft: Add `visibility_nnk` graph constructor + tests and docs

## Title
feat(visibility): add visibility_nnk constructor, HVG/NVG, tests and fixtures generator

## Summary
This PR introduces a paper-aligned graph constructor based on Bozkurt & Ortega (EUSIPCO 2022):

- `visibility_nnk`: builds visibility graph features (HVG/NVG), computes an RBF kernel over node features, generates NNK adjacency using PyNNK when available (internal NNLS fallback otherwise) and returns adjacency + metadata.
- Adds `hvg_adjacency`, `nvg_adjacency`, and `prune_delay` utilities.
- Integrates `interpolate_visibility_graphs()` to build adjacency if not provided and then call existing `interpolate_trss()` reconstructor.
- Adds unit tests and a synthetic fixture generator for reproducibility.
- Updates `REFERENCES.md` and `README_VISIBILITY.md` with usage and validation notes.

## Files changed (high level)
- `Thesis-Copilot-Toolkit/src/graph_construction/graph_constructors.py` — `visibility_nnk`, HVG/NVG, prune_delay, kernel pipeline.
- `Thesis-Copilot-Toolkit/src/interpolation_methods.py` — `interpolate_visibility_graphs()` wrapper.
- `Thesis-Copilot-Toolkit/tests/test_visibility_graphs.py` — unit + e2e smoke tests.
- `Thesis-Copilot-Toolkit/tests/test_visibility_fixtures.py` — fixture comparison scaffold (skipped if fixtures absent).
- `Thesis-Copilot-Toolkit/tools/generate_visibility_fixtures.py` — CLI to build synthetic fixtures (F.npy, G.npy, adjacency.npy, recon.npy).
- `Thesis-Copilot-Toolkit/README_VISIBILITY.md` — usage & reproducibility notes.

## Testing
1. Run unit + smoke tests for the visibility implementation:
```bash
python -m pytest Thesis-Copilot-Toolkit/tests/test_visibility_graphs.py -q
```

2. (Optional, strict validation) Place MATLAB-produced fixtures into `tests/fixtures/visibility/` with names: `input_signals.npy`, `F.npy`, `G.npy`, `adjacency.npy`, `recon.npy`. Then run:
```bash
python -m pytest Thesis-Copilot-Toolkit/tests/test_visibility_fixtures.py -q
```

3. The repo-level `pytest` may collect unrelated third-party tests (faiss, pyflann, mne). Run only the visibility tests to avoid environment/dependency noise.

## Notes for reviewers
- The NNK backend is optional: if `PyNNK_graph_construction` is available on `sys.path`, it will be used; otherwise an internal NNLS-based fallback will produce an adjacency matrix with comparable behavior. Numerical tolerances are documented in the README.
- For paper-faithful numeric comparisons, MATLAB fixtures produced by the original implementation are required; the included generator produces synthetic fixtures useful for CI and smoke checks.

## Checklist
- [ ] Code compiles and tests pass locally for visibility tests
- [ ] Documentation updated (`REFERENCES.md`, `README_VISIBILITY.md`)
- [ ] Add MATLAB-produced fixtures to `tests/fixtures/visibility/` (if available) or mark follow-up task
- [ ] Request reviewers: @OrtegaLab, @YourTeam

## Suggested PR Body
See the summary and testing sections above. Please review the `Thesis-Copilot-Toolkit/PR_DRAFT.md` for step-by-step testing instructions and the notes about numeric validation.
