# QA Report: it107_mat100hz_baseline

## Status: NO-GO

## Summary
- Total rows: 420
- Methods tested: 7
- Graphs: 2
- Missing scenarios: 3
- Best method: trss (MAE=3.5942e+01)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      1.2187e+02
- Instant median MAE: 7.2889e+01
- Gain:               -67.2%
- p-value:            9.9949e-01
- Decision:           **NO-GO**

## Dataset availability snapshot
- bci_iv2a_real_s1: OK
- bci_iv2a_real_s2: OK
- bci_iv2a_real_s3: OK
- iris_graph_signal: OK
- iv100hz_mat: OK
- movielens_graph_signal: OK
- physionet_real: OK

Generated: 2026-04-06T19:04:27.687015+00:00