# QA Report: scr_00044

## Status: NO-GO

## Summary
- Total rows: 14
- Methods tested: 7
- Graphs: 1
- Missing scenarios: 1
- Best method: mean (MAE=1.4221e-02)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      8.3744e-02
- Instant median MAE: 1.8224e-02
- Gain:               -359.5%
- p-value:            8.2751e-01
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

Generated: 2026-04-16T15:39:13.505720+00:00