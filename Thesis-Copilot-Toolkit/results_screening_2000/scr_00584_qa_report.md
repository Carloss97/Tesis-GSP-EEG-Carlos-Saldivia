# QA Report: scr_00584

## Status: NO-GO

## Summary
- Total rows: 14
- Methods tested: 7
- Graphs: 1
- Missing scenarios: 1
- Best method: tv (MAE=6.4191e-02)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      1.1795e-01
- Instant median MAE: 6.6164e-02
- Gain:               -78.3%
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

Generated: 2026-04-16T14:28:25.966666+00:00