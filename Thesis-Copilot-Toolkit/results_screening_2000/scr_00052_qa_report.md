# QA Report: scr_00052

## Status: NO-GO

## Summary
- Total rows: 14
- Methods tested: 7
- Graphs: 1
- Missing scenarios: 1
- Best method: trss (MAE=1.1993e-07)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      2.7260e-06
- Instant median MAE: 1.7224e-07
- Gain:               -1482.7%
- p-value:            7.5458e-01
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

Generated: 2026-04-16T15:42:57.618049+00:00