# QA Report: scr_00629

## Status: NO-GO

## Summary
- Total rows: 14
- Methods tested: 7
- Graphs: 1
- Missing scenarios: 1
- Best method: nearest (MAE=9.1175e-07)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      1.7446e-06
- Instant median MAE: 1.0384e-06
- Gain:               -68.0%
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

Generated: 2026-04-16T14:50:19.294851+00:00