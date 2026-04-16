# QA Report: pilot_0028

## Status: NO-GO

## Summary
- Total rows: 8
- Methods tested: 4
- Graphs: 1
- Missing scenarios: 1
- Best method: trss (MAE=2.4657e-02)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      2.9742e-02
- Instant median MAE: 3.2535e-02
- Gain:               8.6%
- p-value:            2.4286e-01
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

Generated: 2026-04-16T06:29:47.369474+00:00