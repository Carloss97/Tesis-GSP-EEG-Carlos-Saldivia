# QA Report: it150_042

## Status: NO-GO

## Summary
- Total rows: 42
- Methods tested: 7
- Graphs: 1
- Missing scenarios: 1
- Best method: tv (MAE=5.4323e-03)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      4.0376e-02
- Instant median MAE: 1.3287e-02
- Gain:               -203.9%
- p-value:            5.0507e-01
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

Generated: 2026-04-15T00:29:53.783575+00:00