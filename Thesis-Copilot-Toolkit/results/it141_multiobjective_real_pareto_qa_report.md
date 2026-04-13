# QA Report: it141_multiobjective_real_pareto

## Status: GO

## Summary
- Total rows: 160
- Methods tested: 4
- Graphs: 2
- Missing scenarios: 2
- Best method: trss (MAE=1.5608e-06)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      1.8090e-06
- Instant median MAE: 2.2584e-06
- Gain:               19.9%
- p-value:            2.4447e-03
- Decision:           **GO**

## Dataset availability snapshot
- bci_iv2a_real_s1: OK
- bci_iv2a_real_s2: OK
- bci_iv2a_real_s3: OK
- iris_graph_signal: OK
- iv100hz_mat: OK
- movielens_graph_signal: OK
- physionet_real: OK

Generated: 2026-04-13T18:33:01.502074+00:00