# QA Report: it116_all_new_datasets_comprehensive

## Status: NO-GO

## Summary
- Total rows: 1260
- Methods tested: 7
- Graphs: 2
- Missing scenarios: 3
- Best method: trss (MAE=7.2482e+00)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      8.8056e-02
- Instant median MAE: 5.9719e-02
- Gain:               -47.5%
- p-value:            9.8352e-01
- Decision:           **NO-GO**

## Dataset availability snapshot
- bci_iv2a_real_s1: OK
- bci_iv2a_real_s2: OK
- bci_iv2a_real_s3: OK
- iris_graph_signal: OK
- iv100hz_mat: OK
- movielens_graph_signal: OK
- physionet_real: OK

Generated: 2026-04-07T03:02:34.442196+00:00