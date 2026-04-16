# QA Report: scr_00272

## Status: NO-GO

## Summary
- Total rows: 14
- Methods tested: 7
- Graphs: 1
- Missing scenarios: 1
- Best method: nearest (MAE=1.8727e-02)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      8.8044e-02
- Instant median MAE: 2.2590e-02
- Gain:               -289.7%
- p-value:            9.7036e-01
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

Generated: 2026-04-16T15:06:02.139639+00:00