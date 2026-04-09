# QA Report: it114_eeg_vs_iris_transfer

## Status: NO-GO

## Summary
- Total rows: 378
- Methods tested: 7
- Graphs: 1
- Missing scenarios: 3
- Best method: trss (MAE=3.4935e-02)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      1.3027e-05
- Instant median MAE: 5.5352e-06
- Gain:               -135.3%
- p-value:            9.7215e-01
- Decision:           **NO-GO**

## Dataset availability snapshot
- bci_iv2a_real_s1: OK
- bci_iv2a_real_s2: OK
- bci_iv2a_real_s3: OK
- iris_graph_signal: OK
- iv100hz_mat: OK
- movielens_graph_signal: OK
- physionet_real: OK

Generated: 2026-04-06T19:46:08.340980+00:00