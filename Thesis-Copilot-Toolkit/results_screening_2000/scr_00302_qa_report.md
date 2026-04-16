# QA Report: scr_00302

## Status: NO-GO

## Summary
- Total rows: 14
- Methods tested: 7
- Graphs: 1
- Missing scenarios: 1
- Best method: trss (MAE=1.5438e-06)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      7.6460e-06
- Instant median MAE: 3.5242e-06
- Gain:               -117.0%
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

Generated: 2026-04-16T15:20:39.098738+00:00