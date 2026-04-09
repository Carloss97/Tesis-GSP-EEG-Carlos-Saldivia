# QA Report: it102_compute_time_tv_vs_instant

## Status: NO-GO

## Summary
- Total rows: 42
- Methods tested: 7
- Graphs: 1
- Missing scenarios: 1
- Best method: trss (MAE=2.6711e-06)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      8.6698e-06
- Instant median MAE: 4.6538e-06
- Gain:               -86.3%
- p-value:            5.6561e-01
- Decision:           **NO-GO**

## Real-data availability
- physionet: OK
- mne_real: BLOCKED
- bci_iv2a_real: BLOCKED

Generated: 2026-04-09T15:25:36.065373+00:00