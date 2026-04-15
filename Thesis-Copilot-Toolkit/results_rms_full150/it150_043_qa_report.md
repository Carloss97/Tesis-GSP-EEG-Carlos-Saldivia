# QA Report: it150_043

## Status: NO-GO

## Summary
- Total rows: 42
- Methods tested: 7
- Graphs: 1
- Missing scenarios: 1
- Best method: tv (MAE=1.1271e-01)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      1.6744e-01
- Instant median MAE: 1.4254e-01
- Gain:               -17.5%
- p-value:            6.4376e-01
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

Generated: 2026-04-15T00:29:57.171432+00:00