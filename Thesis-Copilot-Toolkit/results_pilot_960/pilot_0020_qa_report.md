# QA Report: pilot_0020

## Status: GO

## Summary
- Total rows: 8
- Methods tested: 4
- Graphs: 1
- Missing scenarios: 1
- Best method: trss (MAE=2.8517e-02)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      3.3744e-02
- Instant median MAE: 4.1593e-02
- Gain:               18.9%
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

Generated: 2026-04-16T06:29:23.227258+00:00