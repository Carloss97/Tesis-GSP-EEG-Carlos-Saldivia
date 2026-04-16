# QA Report: scr_00147

## Status: NO-GO

## Summary
- Total rows: 14
- Methods tested: 7
- Graphs: 1
- Missing scenarios: 1
- Best method: trss (MAE=8.6160e-07)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      7.2107e-06
- Instant median MAE: 1.3367e-06
- Gain:               -439.4%
- p-value:            6.2271e-01
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

Generated: 2026-04-16T15:26:39.456722+00:00