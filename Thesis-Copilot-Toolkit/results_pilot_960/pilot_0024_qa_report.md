# QA Report: pilot_0024

## Status: GO

## Summary
- Total rows: 8
- Methods tested: 4
- Graphs: 1
- Missing scenarios: 1
- Best method: trss (MAE=1.0700e-01)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      1.2164e-01
- Instant median MAE: 1.4677e-01
- Gain:               17.1%
- p-value:            2.8571e-02
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

Generated: 2026-04-16T06:29:36.648476+00:00