# QA Report: it105_real_eeg_crossdataset

## Status: NO-GO

## Summary
- Total rows: 336
- Methods tested: 7
- Graphs: 1
- Missing scenarios: 3
- Best method: trss (MAE=2.0660e-06)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      8.2341e-06
- Instant median MAE: 4.5335e-06
- Gain:               -81.6%
- p-value:            9.9992e-01
- Decision:           **NO-GO**

## Dataset availability snapshot
- bci_iv2a_real_s1: OK
- bci_iv2a_real_s2: OK
- bci_iv2a_real_s3: OK
- iris_graph_signal: OK
- iv100hz_mat: OK
- movielens_graph_signal: OK
- physionet_real: OK

Generated: 2026-04-06T18:47:21.303717+00:00