# QA Report: it126_metric_robustness_multiobjective

## Status: NO-GO

## Summary
- Total rows: 40
- Methods tested: 4
- Graphs: 1
- Missing scenarios: 1
- Best method: trss (MAE=6.8325e+00)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      3.8327e-02
- Instant median MAE: 5.3430e-02
- Gain:               28.3%
- p-value:            1.1966e-01
- Decision:           **NO-GO**

## Dataset availability snapshot
- bci_iv2a_real_s1: OK
- bci_iv2a_real_s2: OK
- bci_iv2a_real_s3: OK
- iris_graph_signal: OK
- iv100hz_mat: OK
- movielens_graph_signal: OK
- physionet_real: OK

Generated: 2026-04-07T17:28:33.377614+00:00