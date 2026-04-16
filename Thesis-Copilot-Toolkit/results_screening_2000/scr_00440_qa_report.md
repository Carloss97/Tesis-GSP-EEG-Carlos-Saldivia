# QA Report: scr_00440

## Status: NO-GO

## Summary
- Total rows: 14
- Methods tested: 7
- Graphs: 1
- Missing scenarios: 1
- Best method: nearest (MAE=4.3284e-02)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      1.0076e-01
- Instant median MAE: 4.4948e-02
- Gain:               -124.2%
- p-value:            9.4605e-01
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

Generated: 2026-04-16T13:32:23.653796+00:00