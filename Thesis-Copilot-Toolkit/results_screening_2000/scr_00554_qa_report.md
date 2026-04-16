# QA Report: scr_00554

## Status: NO-GO

## Summary
- Total rows: 14
- Methods tested: 7
- Graphs: 1
- Missing scenarios: 1
- Best method: trss (MAE=3.7325e-06)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      1.1004e-05
- Instant median MAE: 8.1000e-06
- Gain:               -35.8%
- p-value:            5.7409e-01
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

Generated: 2026-04-16T14:11:30.674495+00:00