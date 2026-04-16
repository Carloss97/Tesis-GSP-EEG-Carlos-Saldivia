# QA Report: scr_00532

## Status: NO-GO

## Summary
- Total rows: 14
- Methods tested: 7
- Graphs: 1
- Missing scenarios: 1
- Best method: trss (MAE=7.7672e-07)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      2.8141e-06
- Instant median MAE: 8.9593e-07
- Gain:               -214.1%
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

Generated: 2026-04-16T14:03:55.283691+00:00