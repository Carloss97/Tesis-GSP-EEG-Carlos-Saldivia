# QA Report: it110_iris_graph_baseline

## Status: NO-GO

## Summary
- Total rows: 168
- Methods tested: 7
- Graphs: 1
- Missing scenarios: 2
- Best method: trss (MAE=1.0529e-01)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      2.7728e-01
- Instant median MAE: 1.6252e-01
- Gain:               -70.6%
- p-value:            7.8713e-01
- Decision:           **NO-GO**

## Dataset availability snapshot
- bci_iv2a_real_s1: OK
- bci_iv2a_real_s2: OK
- bci_iv2a_real_s3: OK
- iris_graph_signal: OK
- iv100hz_mat: OK
- movielens_graph_signal: OK
- physionet_real: OK

Generated: 2026-04-06T19:16:23.740488+00:00