# QA Report: pilot_0006

## Status: GO

## Summary
- Total rows: 20
- Methods tested: 4
- Graphs: 1
- Missing scenarios: 1
- Best method: trss (MAE=1.5225e-01)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      1.6518e-01
- Instant median MAE: 1.9760e-01
- Gain:               16.4%
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
- synthetic_for_pilot_0004: OK
- synthetic_for_pilot_0005: OK
- synthetic_for_pilot_0006: OK

Generated: 2026-04-16T06:33:44.067119+00:00