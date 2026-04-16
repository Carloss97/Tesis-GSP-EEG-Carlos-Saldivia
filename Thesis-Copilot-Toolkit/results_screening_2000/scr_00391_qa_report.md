# QA Report: scr_00391

## Status: NO-GO

## Summary
- Total rows: 14
- Methods tested: 7
- Graphs: 1
- Missing scenarios: 1
- Best method: trss (MAE=9.8145e-02)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      3.3283e-01
- Instant median MAE: 1.5915e-01
- Gain:               -109.1%
- p-value:            4.2591e-01
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

Generated: 2026-04-16T13:15:25.767460+00:00