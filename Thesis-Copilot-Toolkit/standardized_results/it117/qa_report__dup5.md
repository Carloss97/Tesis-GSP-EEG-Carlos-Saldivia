# QA Report: it117_graph_sensitivity_multidomain

## Status: NO-GO

## Summary
- Total rows: 840
- Methods tested: 7
- Graphs: 3
- Missing scenarios: 2
- Best method: trss (MAE=1.1776e+01)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      1.4064e-01
- Instant median MAE: 1.2070e-01
- Gain:               -16.5%
- p-value:            9.5214e-01
- Decision:           **NO-GO**

## Dataset availability snapshot
- bci_iv2a_real_s1: OK
- bci_iv2a_real_s2: OK
- bci_iv2a_real_s3: OK
- iris_graph_signal: OK
- iv100hz_mat: OK
- movielens_graph_signal: OK
- physionet_real: OK

Generated: 2026-04-07T03:16:19.240150+00:00