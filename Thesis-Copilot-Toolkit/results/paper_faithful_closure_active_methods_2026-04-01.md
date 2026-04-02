# Paper-Faithful Closure Audit (Active Methods)

Date: 2026-04-01
Scope: Active interpolation methods in paper-faithful batch

## Executions used as evidence

- Full active batch coverage: results/paper_faithful_results.csv (210/210 combinations)
- Unit tests: python -m unittest tests.test_paper_faithful tests.test_graph_methods_paper_faithful (11/11 OK)
- BGSRP check: experiments/verify_bgsrp_vs_narang.py
- BGSRP exfig4-like frozen replication: experiments/replicate_bgsrp_exfig4_frozen.py
- TRSS replication figure: experiments/reproduce_graphtrss_figure.py
- Narang frozen replication: experiments/reproduce_narang_2013_frozen.py
- Puy frozen replication: experiments/reproduce_puy_2018_frozen.py
- Technical per-method audit (execution/NaN/warnings): ad-hoc run on synthetic EEG

## Active methods audited

- linear
- idw
- rbfi_tps
- rbfi_mq
- spline_surface
- spherical_spline
- gsp
- tikhonov
- bgsrp
- gsmooth
- graph_time_tikhonov
- trss
- tv
- puy
- sobolev

## Classification requested

### 1) Achieved (replication achieved in this repo)

- trss
  - Evidence: results/graphtrss_main_figure.png and CSV summaries.
  - Result: expected qualitative behavior reproduced (TRSS curve consistently below graph_time_tikhonov/tikhonov in MAE vs missing ratio).

- gsp, tikhonov, gsmooth
  - Evidence: results/narang_2013_frozen_raw.csv and results/narang_2013_frozen_summary.csv.
  - Result: frozen Narang-style protocol added and reproducible.

- puy
  - Evidence: results/puy_2018_frozen_raw.csv and results/puy_2018_frozen_summary.csv.
  - Result: frozen Puy-style protocol added and reproducible.

- nnk, aew (graph construction)
  - Evidence: tests/test_graph_methods_paper_faithful.py.
  - Result: dedicated paper-faithful property tests added (symmetry, non-negativity, zero diagonal, signal sensitivity for AEW).

- tv/tiempo activos (`graph_time_tikhonov`, `trss`, `tv`, `sobolev`)
  - Evidence: tests/test_paper_faithful.py.
  - Result: dedicated execution/finite-output tests added and passing.

### 2) Not possible to replicate exactly (with current environment/data)

- bgsrp
  - Why: exact 1:1 with GSPBox sensor generator and MATLAB runtime stack is not available in this Python-only environment.
  - What was possible: exfig4-like frozen timing replication + BGSRP-vs-Narang benchmark executed.

- tv
  - Why: exact Mortaheb et al. hdEEG conditions/dataset are not packaged in current repo.
  - What was possible: robust execution in full batch and GraphTRSS-style comparison.

- sobolev
  - Why: exact reproduction target for this specific static sobolev variant is not codified as a paper-specific script.
  - What was possible: stable execution in full batch.

- graph_time_tikhonov
  - Why: this is an in-repo temporal extension baseline, not tied to one exact canonical figure/script in repo.
  - What was possible: stable execution and comparative curve generation.

- spherical_spline, rbfi_tps, rbfi_mq, idw, linear
  - Why: no exact paper-locked replication script/dataset pair currently implemented in repo for each.
  - What was possible: stable execution in full batch with quantitative rankings.

### 3) Failing (need correction)

- No active interpolation method failing in current audit.
- `spline_surface` was stabilized with adaptive smoothing + controlled fallback (RBF/mean).
- Post-fix check: 0 fitpack warnings, finite outputs, no NaNs.

## Technical audit summary

- Execution failures: 0/15 methods
- Non-finite outputs: 0/15 methods
- NaN outputs: 0/15 methods
- Warning-heavy methods: none after spline_surface fix

## Priority fixes to continue closure

1. bgsrp exactness closure
   - Build a Python experiment mirroring MATLAB gsp_BGSRP_recon_exfig4.m conditions as close as possible.
   - Compare error/time order of magnitude and document mismatch if any.

2. Expand method-specific paper tests further (beyond invariants) for numerical target ranges.
3. Run full exfig4-like BGSRP sweep with larger N/runs and archive long-run profile.
