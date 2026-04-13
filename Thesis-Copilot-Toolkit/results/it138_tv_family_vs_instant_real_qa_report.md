# QA Report: it138_tv_family_vs_instant_real

## Status: NO-GO

## Summary
- Total rows: 375
- Methods tested: 5
- Graphs: 1
- Missing scenarios: 3
- Best method: trss (MAE=7.7402e+00)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      3.2594e-06
- Instant median MAE: 2.2316e-06
- Gain:               -46.1%
- p-value:            9.7988e-01
- Decision:           **NO-GO**

## Dataset availability snapshot
- bci_iv2a_real_s1: OK
- bci_iv2a_real_s2: OK
- bci_iv2a_real_s3: OK
- iris_graph_signal: OK
- iv100hz_mat: OK
- movielens_graph_signal: OK
- physionet_real: OK

Generated: 2026-04-13T18:02:20.700013+00:00