# QA Report: scr_00655

## Status: NO-GO

## Summary
- Total rows: 14
- Methods tested: 7
- Graphs: 1
- Missing scenarios: 1
- Best method: trss (MAE=2.5360e-01)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      3.6723e-01
- Instant median MAE: 3.6254e-01
- Gain:               -1.3%
- p-value:            6.6900e-01
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

Generated: 2026-04-16T15:04:15.952694+00:00