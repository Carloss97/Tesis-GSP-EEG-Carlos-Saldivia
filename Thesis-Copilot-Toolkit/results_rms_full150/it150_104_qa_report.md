# QA Report: it150_104

## Status: NO-GO

## Summary
- Total rows: 42
- Methods tested: 7
- Graphs: 1
- Missing scenarios: 1
- Best method: tv (MAE=3.9660e-02)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      1.0251e-01
- Instant median MAE: 4.6058e-02
- Gain:               -122.6%
- p-value:            9.9428e-01
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

Generated: 2026-04-15T00:41:03.567909+00:00