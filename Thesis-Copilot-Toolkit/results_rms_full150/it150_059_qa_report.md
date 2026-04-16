# QA Report: it150_059

## Status: NO-GO

## Summary
- Total rows: 14
- Methods tested: 7
- Graphs: 1
- Missing scenarios: 1
- Best method: trss (MAE=4.8712e-02)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      3.3732e-01
- Instant median MAE: 7.4701e-02
- Gain:               -351.6%
- p-value:            6.2271e-01
- Decision:           **NO-GO**

## Dataset availability snapshot
- bci_iv2a_real_s1: OK
- bci_iv2a_real_s2: OK
- bci_iv2a_real_s3: OK
- iris_graph_signal: OK
- iv100hz_mat: OK
- mne_sample: OK
- movielens_graph_signal: OK
- physionet_real: OK
- synthetic_16ch: OK
- synthetic_alpha: OK
- synthetic_beta: OK
- synthetic_broad: OK

Generated: 2026-04-15T00:50:22.110406+00:00