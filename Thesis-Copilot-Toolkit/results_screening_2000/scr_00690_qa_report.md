# QA Report: scr_00690

## Status: NO-GO

## Summary
- Total rows: 14
- Methods tested: 7
- Graphs: 1
- Missing scenarios: 1
- Best method: tv (MAE=7.9970e+01)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      1.5222e+02
- Instant median MAE: 1.5757e+02
- Gain:               3.4%
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

Generated: 2026-04-16T15:24:19.212471+00:00