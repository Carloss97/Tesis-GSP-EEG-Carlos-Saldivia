# Ticket: TRSS — Replication & Verification

Objective: Ensure `interpolate_trss` matches paper behavior and provide tests/fixtures to validate across implementations.

Checklist:

- [x] Keep `interpolate_trss` implementation documented and parameterized. (code)
- [x] Add short-run smoke tests that exercise TRSS with constructed adjacencies. (tests/test_visibility_graphs.py)
- [ ] Create MATLAB reference reconstructions (`recon.npy`) for a canonical input and store under `tests/fixtures/visibility/`.
- [ ] Add strict numeric comparison tests with adjustable tolerances and a CI job to run them.
- [ ] If differences exist, log a discrepancy report and investigate solver/reg parameterization.

Notes:
- TRSS relies on gradient-based optimization; numerical differences vs MATLAB may arise from different linear algebra/back-end settings and require parameter alignment (lr, n_iter, reg).
