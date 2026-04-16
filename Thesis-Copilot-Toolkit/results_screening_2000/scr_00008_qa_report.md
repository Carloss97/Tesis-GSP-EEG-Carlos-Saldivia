# QA Report: scr_00008

## Status: NO-GO

## Summary
- Total rows: 14
- Methods tested: 7
- Graphs: 1
- Missing scenarios: 1
- Best method: mean (MAE=1.4221e-02)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      7.5454e-02
- Instant median MAE: 1.8224e-02
- Gain:               -314.0%
- p-value:            8.5881e-01
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

Generated: 2026-04-16T15:20:49.493949+00:00