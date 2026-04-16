# QA Report: pilot_0008

## Status: GO

## Summary
- Total rows: 20
- Methods tested: 4
- Graphs: 1
- Missing scenarios: 1
- Best method: trss (MAE=6.1395e-02)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      7.1471e-02
- Instant median MAE: 9.6688e-02
- Gain:               26.1%
- p-value:            6.5747e-04
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
- synthetic_for_pilot_0007: OK
- synthetic_for_pilot_0008: OK

Generated: 2026-04-16T06:33:52.853263+00:00