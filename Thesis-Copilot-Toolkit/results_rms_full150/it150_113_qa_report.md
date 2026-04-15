# QA Report: it150_113

## Status: NO-GO

## Summary
- Total rows: 42
- Methods tested: 7
- Graphs: 1
- Missing scenarios: 1
- Best method: trss (MAE=5.8367e-02)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      1.9891e-01
- Instant median MAE: 6.7622e-02
- Gain:               -194.1%
- p-value:            9.4943e-01
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

Generated: 2026-04-15T00:42:52.973966+00:00