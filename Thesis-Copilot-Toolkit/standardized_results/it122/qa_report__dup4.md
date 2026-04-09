# QA Report: it122_subjectwise_bci_holdout

## Status: NO-GO

## Summary
- Total rows: 210
- Methods tested: 7
- Graphs: 1
- Missing scenarios: 2
- Best method: trss (MAE=1.3396e-06)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      2.9045e-06
- Instant median MAE: 1.5335e-06
- Gain:               -89.4%
- p-value:            9.9989e-01
- Decision:           **NO-GO**

## Dataset availability snapshot
- bci_iv2a_real_s1: OK
- bci_iv2a_real_s2: OK
- bci_iv2a_real_s3: OK
- iris_graph_signal: OK
- iv100hz_mat: OK
- movielens_graph_signal: OK
- physionet_real: OK

Generated: 2026-04-07T17:08:26.086085+00:00