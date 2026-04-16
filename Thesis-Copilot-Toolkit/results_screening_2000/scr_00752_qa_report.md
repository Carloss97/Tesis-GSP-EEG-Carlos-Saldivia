# QA Report: scr_00752

## Status: NO-GO

## Summary
- Total rows: 14
- Methods tested: 7
- Graphs: 1
- Missing scenarios: 1
- Best method: mean (MAE=8.9501e-02)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      1.1289e-01
- Instant median MAE: 9.3260e-02
- Gain:               -21.0%
- p-value:            8.5881e-01
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

Generated: 2026-04-16T11:52:35.896105+00:00