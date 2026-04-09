# QA Report: it121_domain_stratified_gate

## Status: NO-GO

## Summary
- Total rows: 1008
- Methods tested: 7
- Graphs: 2
- Missing scenarios: 3
- Best method: trss (MAE=6.0022e+00)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      7.3046e-03
- Instant median MAE: 6.6051e-03
- Gain:               -10.6%
- p-value:            9.9230e-01
- Decision:           **NO-GO**

## Dataset availability snapshot
- bci_iv2a_real_s1: OK
- bci_iv2a_real_s2: OK
- bci_iv2a_real_s3: OK
- iris_graph_signal: OK
- iv100hz_mat: OK
- movielens_graph_signal: OK
- physionet_real: OK

Generated: 2026-04-07T17:03:38.782317+00:00