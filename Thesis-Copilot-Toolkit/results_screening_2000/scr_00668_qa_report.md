# QA Report: scr_00668

## Status: NO-GO

## Summary
- Total rows: 14
- Methods tested: 7
- Graphs: 1
- Missing scenarios: 1
- Best method: mean (MAE=8.9501e-02)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      1.3368e-01
- Instant median MAE: 9.9249e-02
- Gain:               -34.7%
- p-value:            9.0942e-01
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

Generated: 2026-04-16T15:11:06.081764+00:00