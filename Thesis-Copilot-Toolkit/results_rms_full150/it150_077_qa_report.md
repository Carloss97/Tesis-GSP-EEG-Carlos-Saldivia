# QA Report: it150_077

## Status: NO-GO

## Summary
- Total rows: 42
- Methods tested: 7
- Graphs: 1
- Missing scenarios: 1
- Best method: nearest (MAE=2.9768e-02)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      1.4062e-01
- Instant median MAE: 3.4986e-02
- Gain:               -301.9%
- p-value:            9.8854e-01
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

Generated: 2026-04-15T00:36:18.341635+00:00