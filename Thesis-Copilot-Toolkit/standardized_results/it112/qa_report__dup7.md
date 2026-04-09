# QA Report: it112_movielens_graph_baseline

## Status: NO-GO

## Summary
- Total rows: 140
- Methods tested: 7
- Graphs: 1
- Missing scenarios: 2
- Best method: tv (MAE=2.6539e-02)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      9.3319e-02
- Instant median MAE: 3.6354e-02
- Gain:               -156.7%
- p-value:            9.9996e-01
- Decision:           **NO-GO**

## Dataset availability snapshot
- bci_iv2a_real_s1: OK
- bci_iv2a_real_s2: OK
- bci_iv2a_real_s3: OK
- iris_graph_signal: OK
- iv100hz_mat: OK
- movielens_graph_signal: OK
- physionet_real: OK

Generated: 2026-04-06T19:19:39.236550+00:00