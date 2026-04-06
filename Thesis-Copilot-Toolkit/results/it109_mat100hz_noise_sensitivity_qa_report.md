# QA Report: it109_mat100hz_noise_sensitivity

## Status: NO-GO

## Summary
- Total rows: 168
- Methods tested: 7
- Graphs: 1
- Missing scenarios: 1
- Best method: trss (MAE=5.0307e+01)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      1.2634e+02
- Instant median MAE: 7.5352e+01
- Gain:               -67.7%
- p-value:            9.8962e-01
- Decision:           **NO-GO**

## Dataset availability snapshot
- bci_iv2a_real_s1: OK
- bci_iv2a_real_s2: OK
- bci_iv2a_real_s3: OK
- iris_graph_signal: OK
- iv100hz_mat: OK
- movielens_graph_signal: OK
- physionet_real: OK

Generated: 2026-04-06T19:16:10.497857+00:00