# QA Report: scr_00605

## Status: NO-GO

## Summary
- Total rows: 14
- Methods tested: 7
- Graphs: 1
- Missing scenarios: 1
- Best method: trss (MAE=8.0874e-07)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      2.0043e-06
- Instant median MAE: 1.0384e-06
- Gain:               -93.0%
- p-value:            7.5458e-01
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

Generated: 2026-04-16T14:38:21.007781+00:00