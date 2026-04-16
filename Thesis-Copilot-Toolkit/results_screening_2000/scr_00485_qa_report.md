# QA Report: scr_00485

## Status: NO-GO

## Summary
- Total rows: 14
- Methods tested: 7
- Graphs: 1
- Missing scenarios: 1
- Best method: trss (MAE=5.5457e-07)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      1.9933e-06
- Instant median MAE: 7.3297e-07
- Gain:               -172.0%
- p-value:            7.5458e-01
- Decision:           **NO-GO**

## Dataset availability snapshot
- bci_iv2a_real_s1: OK
- bci_iv2a_real_s2: OK
- bci_iv2a_real_s3: OK
- iris_graph_signal: OK
- iv100hz_mat: OK
- mne_sample: BLOCKED
- movielens_graph_signal: OK
- physionet_real: OK

Generated: 2026-04-16T13:46:53.666008+00:00