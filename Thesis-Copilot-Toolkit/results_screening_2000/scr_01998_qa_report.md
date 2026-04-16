# QA Report: scr_01998

## Status: NO-GO

## Summary
- Total rows: 42
- Methods tested: 7
- Graphs: 1
- Missing scenarios: 1
- Best method: trss (MAE=1.4868e-02)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      4.9833e-02
- Instant median MAE: 2.6111e-02
- Gain:               -90.9%
- p-value:            6.9883e-01
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

Generated: 2026-04-16T10:07:18.703114+00:00