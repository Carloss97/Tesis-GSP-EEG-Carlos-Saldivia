# QA Report: scr_00725

## Status: NO-GO

## Summary
- Total rows: 14
- Methods tested: 7
- Graphs: 1
- Missing scenarios: 1
- Best method: nearest (MAE=1.3529e-06)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      2.1994e-06
- Instant median MAE: 1.4593e-06
- Gain:               -50.7%
- p-value:            8.8578e-01
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

Generated: 2026-04-16T11:50:58.688658+00:00