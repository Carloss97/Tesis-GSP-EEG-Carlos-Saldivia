# QA Report: pilot_0015

## Status: GO

## Summary
- Total rows: 8
- Methods tested: 4
- Graphs: 1
- Missing scenarios: 1
- Best method: trss (MAE=2.9322e-02)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      4.3506e-02
- Instant median MAE: 6.3368e-02
- Gain:               31.3%
- p-value:            1.4286e-02
- Decision:           **GO**

## Dataset availability snapshot
- bci_iv2a_real_s1: OK
- bci_iv2a_real_s2: OK
- bci_iv2a_real_s3: OK
- iris_graph_signal: OK
- iv100hz_mat: OK
- mne_sample: BLOCKED
- movielens_graph_signal: OK
- physionet_real: OK

Generated: 2026-04-16T06:29:10.061681+00:00