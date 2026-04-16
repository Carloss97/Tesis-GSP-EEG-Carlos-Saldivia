# QA Report: scr_00632

## Status: NO-GO

## Summary
- Total rows: 14
- Methods tested: 7
- Graphs: 1
- Missing scenarios: 1
- Best method: tv (MAE=6.4158e-02)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      1.1505e-01
- Instant median MAE: 6.6164e-02
- Gain:               -73.9%
- p-value:            9.2907e-01
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

Generated: 2026-04-16T14:52:52.440835+00:00