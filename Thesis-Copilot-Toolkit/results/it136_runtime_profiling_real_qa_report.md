# QA Report: it136_runtime_profiling_real

## Status: NO-GO

## Summary
- Total rows: 60
- Methods tested: 4
- Graphs: 1
- Missing scenarios: 1
- Best method: trss (MAE=6.8546e+00)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      1.8065e-06
- Instant median MAE: 2.4466e-06
- Gain:               26.2%
- p-value:            1.7697e-01
- Decision:           **NO-GO**

## Dataset availability snapshot
- bci_iv2a_real_s1: OK
- bci_iv2a_real_s2: OK
- bci_iv2a_real_s3: OK
- iris_graph_signal: OK
- iv100hz_mat: OK
- movielens_graph_signal: OK
- physionet_real: OK

Generated: 2026-04-13T18:00:38.133029+00:00