# QA Report: pilot_0003

## Status: GO

## Summary
- Total rows: 20
- Methods tested: 4
- Graphs: 1
- Missing scenarios: 1
- Best method: trss (MAE=1.0941e-01)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      1.2189e-01
- Instant median MAE: 1.4647e-01
- Gain:               16.8%
- p-value:            3.2011e-02
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
- synthetic_for_pilot_0001: OK
- synthetic_for_pilot_0002: OK
- synthetic_for_pilot_0003: OK

Generated: 2026-04-16T06:33:31.255478+00:00