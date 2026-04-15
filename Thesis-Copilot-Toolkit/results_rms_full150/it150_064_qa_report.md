# QA Report: it150_064

## Status: NO-GO

## Summary
- Total rows: 42
- Methods tested: 7
- Graphs: 1
- Missing scenarios: 1
- Best method: trss (MAE=1.1986e-02)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      1.0593e-01
- Instant median MAE: 1.4601e-02
- Gain:               -625.5%
- p-value:            8.7098e-01
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

Generated: 2026-04-15T00:33:44.056432+00:00