# QA Report: scr_00028

## Status: NO-GO

## Summary
- Total rows: 14
- Methods tested: 7
- Graphs: 1
- Missing scenarios: 1
- Best method: trss (MAE=1.3387e-07)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      2.5696e-06
- Instant median MAE: 1.7224e-07
- Gain:               -1391.9%
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

Generated: 2026-04-16T15:30:01.418202+00:00