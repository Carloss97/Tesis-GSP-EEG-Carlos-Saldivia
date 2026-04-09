# QA Report: it118_runtime_family_multidomain

## Status: NO-GO

## Summary
- Total rows: 140
- Methods tested: 7
- Graphs: 1
- Missing scenarios: 1
- Best method: trss (MAE=6.8511e+00)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      7.2860e-02
- Instant median MAE: 3.8553e-02
- Gain:               -89.0%
- p-value:            6.9701e-01
- Decision:           **NO-GO**

## Dataset availability snapshot
- bci_iv2a_real_s1: OK
- bci_iv2a_real_s2: OK
- bci_iv2a_real_s3: OK
- iris_graph_signal: OK
- iv100hz_mat: OK
- movielens_graph_signal: OK
- physionet_real: OK

Generated: 2026-04-07T03:18:46.615026+00:00