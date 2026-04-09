# QA Report: it104_noise_sensitivity_tv

## Status: NO-GO

## Summary
- Total rows: 112
- Methods tested: 7
- Graphs: 1
- Missing scenarios: 1
- Best method: trss (MAE=5.1245e-06)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      1.1142e-05
- Instant median MAE: 7.5750e-06
- Gain:               -47.1%
- p-value:            9.8034e-01
- Decision:           **NO-GO**

## Real-data availability
- physionet: OK
- mne_real: BLOCKED
- bci_iv2a_real: BLOCKED

Generated: 2026-04-09T07:23:23.297549+00:00