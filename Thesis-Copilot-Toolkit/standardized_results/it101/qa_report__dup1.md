# QA Report: it101_real_data_validation

## Status: NO-GO

## Summary
- Total rows: 105
- Methods tested: 7
- Graphs: 1
- Missing scenarios: 3
- Best method: trss (MAE=3.0046e-06)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      9.8613e-06
- Instant median MAE: 6.2803e-06
- Gain:               -57.0%
- p-value:            9.8671e-01
- Decision:           **NO-GO**

## Real-data availability
- physionet: OK
- mne_real: BLOCKED
- bci_iv2a_real: BLOCKED

Generated: 2026-04-09T06:59:54.617690+00:00