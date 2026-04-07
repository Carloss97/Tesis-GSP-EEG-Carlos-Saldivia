# QA Report: it124_missing_pattern_realistic_v2

## Status: GO

## Summary
- Total rows: 24
- Methods tested: 4
- Graphs: 1
- Missing scenarios: 1
- Best method: trss (MAE=1.4232e-06)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      1.8479e-06
- Instant median MAE: 3.2726e-06
- Gain:               43.5%
- p-value:            2.6549e-02
- Decision:           **GO**

## Dataset availability snapshot
- bci_iv2a_real_s1: OK
- bci_iv2a_real_s2: OK
- bci_iv2a_real_s3: OK
- iris_graph_signal: OK
- iv100hz_mat: OK
- movielens_graph_signal: OK
- physionet_real: OK

Generated: 2026-04-07T17:41:22.918968+00:00