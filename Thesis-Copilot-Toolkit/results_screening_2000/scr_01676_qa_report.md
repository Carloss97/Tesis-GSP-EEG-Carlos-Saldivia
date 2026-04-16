# QA Report: scr_01676

## Status: NO-GO

## Summary
- Total rows: 42
- Methods tested: 7
- Graphs: 1
- Missing scenarios: 1
- Best method: tv (MAE=7.4856e-02)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      1.7192e-01
- Instant median MAE: 9.6610e-02
- Gain:               -78.0%
- p-value:            9.3477e-01
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

Generated: 2026-04-16T09:21:32.980794+00:00