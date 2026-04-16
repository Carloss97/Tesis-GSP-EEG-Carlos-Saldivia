# QA Report: scr_00606

## Status: NO-GO

## Summary
- Total rows: 14
- Methods tested: 7
- Graphs: 1
- Missing scenarios: 1
- Best method: trss (MAE=2.9875e+01)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      1.0556e+02
- Instant median MAE: 1.1238e+02
- Gain:               6.1%
- p-value:            5.2514e-01
- Decision:           **NO-GO**

## Dataset availability snapshot
- bci_iv2a_real_s1: OK
- bci_iv2a_real_s2: OK
- bci_iv2a_real_s3: OK
- iris_graph_signal: OK
- iv100hz_mat: OK
- mne_sample: BLOCKED
- movielens_graph_signal: OK
- physionet_real: OK

Generated: 2026-04-16T14:39:05.332112+00:00