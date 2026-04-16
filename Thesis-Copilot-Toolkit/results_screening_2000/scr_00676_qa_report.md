# QA Report: scr_00676

## Status: NO-GO

## Summary
- Total rows: 14
- Methods tested: 7
- Graphs: 1
- Missing scenarios: 1
- Best method: trss (MAE=1.4933e-06)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      3.5101e-06
- Instant median MAE: 1.7740e-06
- Gain:               -97.9%
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

Generated: 2026-04-16T15:14:16.700846+00:00