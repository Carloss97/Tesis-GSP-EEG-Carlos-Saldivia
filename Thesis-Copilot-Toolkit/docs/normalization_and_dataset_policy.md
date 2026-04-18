# Normalization and Dataset Availability Policy

This document records the repository convention introduced to avoid mixing normalized and non-normalized outputs and to prefer local real datasets when available.

## Why

Mixing normalized and non-normalized runs leads to non-comparable metrics (MAE, RMSE, SNR). A small preprocessing difference can change absolute error scales and invalidate statistical comparisons.

## Conventions

- Storage:
  - Originals: keep in `results/`.
  - Normalized experiments: place in `results_normalized_<timestamp>/` or append `_norm` to the `iteration_tag` (example: `it123_norm`).

- Metadata:
  - Every `*_run_metadata.json` produced by the Runner must include the field:

```json
{
  "iteration_tag": "it123_norm",
  "normalization": "rms",   // or null
  "missing_mode": "nearby" // "random" or "nearby"
}
```

- Execution flags (convention):
  - Request normalization by setting environment variables:

    - `NORMALIZE_DATASETS=1`
    - `NORM_METHOD=rms`

  - The orchestrator/runner must write normalized outputs to the normalized folder so that `results/` remains the truth for unmodified (raw) runs.

- Dataset availability:
  - Prefer local keys when available: `physionet_real`, `bci_iv2a_real_s1`, `bci_iv2a_real_s2`, `bci_iv2a_real_s3`, `mne_sample`.
  - Proxies and synthetic datasets are fallback only.
  - Configure local dataset paths via environment variables as required by the data loader (e.g., `EEGBCI_LOCAL_PATH`, `PHYSIONET_LOCAL_PATH`).

## Missing-channel scenarios

- Supported scenario formats:
  - Fractional: `0.1`, `0.2` (representing percentage of channels removed)
  - Absolute: `1ch`, `2ch`, `3ch` (exact N channels removed)
  - Mode qualifiers: suffix `_random` or `_nearby` (example: `2ch_random`, `3ch_nearby`). If omitted, default is `random`.

- Runner MUST record `missing_mode` in `run_metadata.json`.

## Aggregation rules

- Postprocessing scripts must filter runs by `normalization` before aggregating or computing pairwise statistics.
- Comparisons, rankings and Wilcoxon/Wald tests must be executed only on homogeneous groups (same `normalization` and same `missing_mode`).

## Quick checklist before publishing results

- [ ] All aggregated CSVs were built from runs sharing the same `normalization` value.
- [ ] `*_run_metadata.json` files include `normalization` and `missing_mode` fields.
- [ ] Normalized runs are stored separately and not mixed into `results/` used for raw runs.
- [ ] Orchestrator used local datasets when available; proxies used only when local availability check failed.

## Example (advisory)

PowerShell example to request a normalized run (adapt to your orchestrator invocation):

```powershell
$env:NORMALIZE_DATASETS='1'
$env:NORM_METHOD='rms'
# Then invoke the orchestrator/runner with the desired inputs
# Example (pseudo):
# .\.venv\Scripts\python.exe -m experiments.orchestrator --dataset physionet_real --scenarios '["2ch_nearby"]' --seeds 0-19 --iteration_tag it123_norm
```

Keep this file updated if new normalization methods are implemented or if the Runner changes how it records metadata.

## Recommended TV Methods

- `temporal_laplacian`: recommended for time-varying reconstruction tasks. Implements a product-graph spatio-temporal Laplacian regularizer (spatial Laplacian ⊗ I + I ⊗ temporal Laplacian) and complements existing TV-family methods (`trss`, `graph_time_tikhonov`). See Jiang et al., 2021 and Giraldo et al., 2022 for product-graph and Sobolev/time-varying smoothness formulations.

When adding TV methods to an iteration, ensure the Runner records `methods` in `*_run_metadata.json` and that temporal methods are compared as a family (see `AGENT_ITERATION_GUIDE.md`).
