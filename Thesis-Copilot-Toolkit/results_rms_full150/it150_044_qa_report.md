# QA Report: it150_044

## Status: NO-GO

## Summary
- Total rows: 42
- Methods tested: 7
- Graphs: 1
- Missing scenarios: 1
- Best method: mean (MAE=1.9209e-02)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      8.8256e-02
- Instant median MAE: 2.3699e-02
- Gain:               -272.4%
- p-value:            9.9126e-01
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

Generated: 2026-04-15T00:30:15.642370+00:00