# QA Report: it131_heatdiff_trss_directed_tv_real

## Status: GO

## Summary
- Total rows: 1350
- Methods tested: 5
- Graphs: 3
- Missing scenarios: 3
- Best method: trss (MAE=6.0203e+00)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      1.5128e-06
- Instant median MAE: 2.0817e-06
- Gain:               27.3%
- p-value:            2.6663e-02
- Decision:           **GO**

## Dataset availability snapshot
- bci_iv2a_real_s1: OK
- bci_iv2a_real_s2: OK
- bci_iv2a_real_s3: OK
- iris_graph_signal: OK
- iv100hz_mat: OK
- movielens_graph_signal: OK
- physionet_real: OK

Generated: 2026-04-13T17:55:16.294349+00:00