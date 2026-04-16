# QA Report: it150_103

## Status: NO-GO

## Summary
- Total rows: 42
- Methods tested: 7
- Graphs: 1
- Missing scenarios: 1
- Best method: trss (MAE=1.1227e-01)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      2.7642e-01
- Instant median MAE: 1.5582e-01
- Gain:               -77.4%
- p-value:            6.9883e-01
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

Generated: 2026-04-15T00:40:43.479303+00:00