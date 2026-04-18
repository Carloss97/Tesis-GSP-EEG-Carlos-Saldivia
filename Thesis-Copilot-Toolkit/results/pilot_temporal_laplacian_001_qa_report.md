# QA Report: pilot_temporal_laplacian_001

## Status: NO-GO

## Summary
- Total rows: 48
- Methods tested: 6
- Graphs: 1
- Missing scenarios: 1
- Best method: trss (MAE=6.1469e-02)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      1.6506e-01
- Instant median MAE: 1.0463e-01
- Gain:               -57.8%
- p-value:            9.4498e-01
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

Generated: 2026-04-18T03:36:41.465573+00:00