# QA Report: pilot_0007

## Status: GO

## Summary
- Total rows: 20
- Methods tested: 4
- Graphs: 1
- Missing scenarios: 1
- Best method: trss (MAE=3.0444e-02)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      3.5943e-02
- Instant median MAE: 4.9429e-02
- Gain:               27.3%
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

Generated: 2026-04-16T06:33:48.349523+00:00