# QA Report: it142_confidence_bootstrap_real

## Status: NO-GO

## Summary
- Total rows: 210
- Methods tested: 7
- Graphs: 1
- Missing scenarios: 1
- Best method: trss (MAE=1.1415e+01)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      1.2710e-05
- Instant median MAE: 5.4059e-06
- Gain:               -135.1%
- p-value:            7.4969e-01
- Decision:           **NO-GO**

## Dataset availability snapshot
- bci_iv2a_real_s1: OK
- bci_iv2a_real_s2: OK
- bci_iv2a_real_s3: OK
- iris_graph_signal: OK
- iv100hz_mat: OK
- movielens_graph_signal: OK
- physionet_real: OK

Generated: 2026-04-13T18:34:16.701961+00:00