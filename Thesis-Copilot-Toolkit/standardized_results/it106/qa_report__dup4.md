# QA Report: it106_bci_iv2a_multisubject

## Status: NO-GO

## Summary
- Total rows: 378
- Methods tested: 7
- Graphs: 1
- Missing scenarios: 3
- Best method: trss (MAE=1.0446e-06)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      2.5724e-06
- Instant median MAE: 1.2433e-06
- Gain:               -106.9%
- p-value:            1.0000e+00
- Decision:           **NO-GO**

## Dataset availability snapshot
- bci_iv2a_real_s1: OK
- bci_iv2a_real_s2: OK
- bci_iv2a_real_s3: OK
- iris_graph_signal: OK
- iv100hz_mat: OK
- movielens_graph_signal: OK
- physionet_real: OK

Generated: 2026-04-06T18:55:25.723882+00:00