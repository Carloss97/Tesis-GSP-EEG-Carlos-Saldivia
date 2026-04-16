# QA Report: scr_00751

## Status: NO-GO

## Summary
- Total rows: 14
- Methods tested: 7
- Graphs: 1
- Missing scenarios: 1
- Best method: trss (MAE=1.8746e-01)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      2.7744e-01
- Instant median MAE: 2.6851e-01
- Gain:               -3.3%
- p-value:            4.2591e-01
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

Generated: 2026-04-16T11:52:30.206760+00:00