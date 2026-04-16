# QA Report: scr_00283

## Status: NO-GO

## Summary
- Total rows: 14
- Methods tested: 7
- Graphs: 1
- Missing scenarios: 1
- Best method: trss (MAE=3.6503e-01)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      4.9491e-01
- Instant median MAE: 5.2211e-01
- Gain:               5.2%
- p-value:            4.2591e-01
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

Generated: 2026-04-16T15:11:06.089860+00:00