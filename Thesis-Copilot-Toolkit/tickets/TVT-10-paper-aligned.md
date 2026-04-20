# Ticket: TVT-10 — Paper-aligned implementation & validation

Objective: Complete a paper-faithful implementation and automated validation workflow for
Bozkurt & Ortega, 2022 (Visibility graphs + NNK + TRSS).

Checklist:

- [x] Implement `visibility_nnk` graph constructor (features → RBF → NNK). (code)
- [x] Add NVG and HVG implementations in Python (`nvg_adjacency`, `hvg_adjacency`). (code)
- [x] Add `prune_delay` helper to support delay-aware pruning of visibility edges. (code)
- [x] Add CLI runner to generate intermediate fixtures (`F.npy`, `G.npy`, `adjacency.npy`, `recon.npy`). (tools/generate_visibility_fixtures.py)
- [x] Add unit tests and E2E smoke tests. (tests/test_visibility_graphs.py)
- [x] Add fixtures comparison test scaffold (skips if fixtures not present). (tests/test_visibility_fixtures.py)
- [ ] Produce MATLAB fixtures (MATLAB run of original demos) and place under `tests/fixtures/visibility/`.
- [ ] Run numerical comparisons and close the ticket if tolerances acceptable.

Notes:
- Generating MATLAB fixtures requires executing the original MATLAB demos locally and saving `F.npy`, `G.npy`, `adjacency.npy`, `recon.npy` alongside `input_signals.npy`.
- Tolerances for numeric comparison may need adjustment depending on solver differences (NNK QP tolerances, numeric solvers).
