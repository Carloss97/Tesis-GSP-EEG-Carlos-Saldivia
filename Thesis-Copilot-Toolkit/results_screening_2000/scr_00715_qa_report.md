# QA Report: scr_00715

## Status: NO-GO

## Summary
- Total rows: 14
- Methods tested: 7
- Graphs: 1
- Missing scenarios: 1
- Best method: trss (MAE=2.1394e-01)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      4.0320e-01
- Instant median MAE: 3.6473e-01
- Gain:               -10.5%
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

Generated: 2026-04-16T15:37:49.445899+00:00