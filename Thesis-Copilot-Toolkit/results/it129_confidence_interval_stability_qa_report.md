# QA Report: it129_confidence_interval_stability

## Status: NO-GO

## Summary
- Total rows: 32
- Methods tested: 4
- Graphs: 1
- Missing scenarios: 1
- Best method: trss (MAE=8.5295e+00)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      5.1811e-02
- Instant median MAE: 6.4408e-02
- Gain:               19.6%
- p-value:            5.8898e-02
- Decision:           **NO-GO**

## Dataset availability snapshot
- bci_iv2a_real_s1: OK
- bci_iv2a_real_s2: OK
- bci_iv2a_real_s3: OK
- iris_graph_signal: OK
- iv100hz_mat: OK
- movielens_graph_signal: OK
- physionet_real: OK

Generated: 2026-04-07T17:44:34.994823+00:00