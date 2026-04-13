# QA Report: it150_decision_matrix_update

## Status: NO-GO

## Summary
- Total rows: 84
- Methods tested: 7
- Graphs: 1
- Missing scenarios: 1
- Best method: trss (MAE=1.4099e-06)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      4.3976e-06
- Instant median MAE: 2.5543e-06
- Gain:               -72.2%
- p-value:            9.7318e-01
- Decision:           **NO-GO**

## Dataset availability snapshot
- bci_iv2a_real_s1: OK
- bci_iv2a_real_s2: OK
- bci_iv2a_real_s3: OK
- iris_graph_signal: OK
- iv100hz_mat: OK
- movielens_graph_signal: OK
- physionet_real: OK

Generated: 2026-04-13T19:08:24.604991+00:00