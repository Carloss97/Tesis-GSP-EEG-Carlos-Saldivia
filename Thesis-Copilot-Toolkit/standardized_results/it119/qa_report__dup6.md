# QA Report: it119_noise_trend_multidomain

## Status: NO-GO

## Summary
- Total rows: 336
- Methods tested: 7
- Graphs: 1
- Missing scenarios: 1
- Best method: trss (MAE=1.6741e+01)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      3.3390e-01
- Instant median MAE: 2.2217e-01
- Gain:               -50.3%
- p-value:            8.7047e-01
- Decision:           **NO-GO**

## Dataset availability snapshot
- bci_iv2a_real_s1: OK
- bci_iv2a_real_s2: OK
- bci_iv2a_real_s3: OK
- iris_graph_signal: OK
- iv100hz_mat: OK
- movielens_graph_signal: OK
- physionet_real: OK

Generated: 2026-04-07T06:15:47.615606+00:00