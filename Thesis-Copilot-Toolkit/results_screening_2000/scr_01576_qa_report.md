# QA Report: scr_01576

## Status: NO-GO

## Summary
- Total rows: 42
- Methods tested: 7
- Graphs: 1
- Missing scenarios: 1
- Best method: trss (MAE=4.3354e-02)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      1.4322e-01
- Instant median MAE: 7.5033e-02
- Gain:               -90.9%
- p-value:            8.9582e-01
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

Generated: 2026-04-16T09:07:07.913802+00:00