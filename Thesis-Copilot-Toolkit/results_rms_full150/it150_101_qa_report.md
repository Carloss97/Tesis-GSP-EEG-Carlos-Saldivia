# QA Report: it150_101

## Status: NO-GO

## Summary
- Total rows: 42
- Methods tested: 7
- Graphs: 1
- Missing scenarios: 1
- Best method: nearest (MAE=6.0225e-02)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      1.8032e-01
- Instant median MAE: 6.7622e-02
- Gain:               -166.7%
- p-value:            9.8084e-01
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

Generated: 2026-04-15T00:40:19.770309+00:00