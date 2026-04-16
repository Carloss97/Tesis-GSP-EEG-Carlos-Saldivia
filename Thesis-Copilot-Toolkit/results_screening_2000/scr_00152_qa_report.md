# QA Report: scr_00152

## Status: NO-GO

## Summary
- Total rows: 14
- Methods tested: 7
- Graphs: 1
- Missing scenarios: 1
- Best method: mean (MAE=1.6812e-02)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      8.7512e-02
- Instant median MAE: 2.0160e-02
- Gain:               -334.1%
- p-value:            9.4605e-01
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

Generated: 2026-04-16T15:31:26.814737+00:00