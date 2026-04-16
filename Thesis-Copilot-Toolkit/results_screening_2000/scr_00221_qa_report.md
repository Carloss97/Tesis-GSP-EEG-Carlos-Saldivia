# QA Report: scr_00221

## Status: NO-GO

## Summary
- Total rows: 14
- Methods tested: 7
- Graphs: 1
- Missing scenarios: 1
- Best method: nearest (MAE=3.8797e-07)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      1.4516e-06
- Instant median MAE: 4.4593e-07
- Gain:               -225.5%
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

Generated: 2026-04-16T14:38:59.318069+00:00