# QA Report: it150_091

## Status: NO-GO

## Summary
- Total rows: 42
- Methods tested: 7
- Graphs: 1
- Missing scenarios: 1
- Best method: trss (MAE=8.8189e-02)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      1.7011e-01
- Instant median MAE: 1.4080e-01
- Gain:               -20.8%
- p-value:            5.9540e-01
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

Generated: 2026-04-15T00:38:42.312926+00:00