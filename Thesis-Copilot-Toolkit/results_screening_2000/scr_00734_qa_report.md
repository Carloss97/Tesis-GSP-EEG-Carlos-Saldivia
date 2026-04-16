# QA Report: scr_00734

## Status: NO-GO

## Summary
- Total rows: 14
- Methods tested: 7
- Graphs: 1
- Missing scenarios: 1
- Best method: trss (MAE=5.8945e-06)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      1.2654e-05
- Instant median MAE: 1.0482e-05
- Gain:               -20.7%
- p-value:            7.1362e-01
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

Generated: 2026-04-16T11:51:23.689995+00:00