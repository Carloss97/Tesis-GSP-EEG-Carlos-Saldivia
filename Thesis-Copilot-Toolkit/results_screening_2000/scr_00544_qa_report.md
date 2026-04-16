# QA Report: scr_00544

## Status: NO-GO

## Summary
- Total rows: 14
- Methods tested: 7
- Graphs: 1
- Missing scenarios: 1
- Best method: trss (MAE=1.0769e-06)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      3.0207e-06
- Instant median MAE: 1.2421e-06
- Gain:               -143.2%
- p-value:            7.9321e-01
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

Generated: 2026-04-16T14:08:29.212843+00:00