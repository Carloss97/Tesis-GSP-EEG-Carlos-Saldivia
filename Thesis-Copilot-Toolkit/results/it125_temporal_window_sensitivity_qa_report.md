# QA Report: it125_temporal_window_sensitivity

## Status: GO

## Summary
- Total rows: 24
- Methods tested: 4
- Graphs: 1
- Missing scenarios: 1
- Best method: trss (MAE=1.1337e+01)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      3.2236e-06
- Instant median MAE: 5.4901e-06
- Gain:               41.3%
- p-value:            2.3193e-02
- Decision:           **GO**

## Dataset availability snapshot
- bci_iv2a_real_s1: OK
- bci_iv2a_real_s2: OK
- bci_iv2a_real_s3: OK
- iris_graph_signal: OK
- iv100hz_mat: OK
- movielens_graph_signal: OK
- physionet_real: OK

Generated: 2026-04-07T17:41:31.898993+00:00