# QA Report: scr_00209

## Status: NO-GO

## Summary
- Total rows: 14
- Methods tested: 7
- Graphs: 1
- Missing scenarios: 1
- Best method: nearest (MAE=2.5053e-07)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      1.2802e-06
- Instant median MAE: 2.9446e-07
- Gain:               -334.8%
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

Generated: 2026-04-16T14:32:48.053303+00:00