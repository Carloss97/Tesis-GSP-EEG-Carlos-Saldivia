# QA Report: scr_00699

## Status: NO-GO

## Summary
- Total rows: 14
- Methods tested: 7
- Graphs: 1
- Missing scenarios: 1
- Best method: trss (MAE=4.8994e-06)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      1.0200e-05
- Instant median MAE: 6.6944e-06
- Gain:               -52.4%
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

Generated: 2026-04-16T15:28:05.539592+00:00