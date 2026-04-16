# QA Report: pilot_0033

## Status: NO-GO

## Summary
- Total rows: 8
- Methods tested: 4
- Graphs: 1
- Missing scenarios: 1
- Best method: trss (MAE=3.5530e-02)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      4.3539e-02
- Instant median MAE: 5.0812e-02
- Gain:               14.3%
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

Generated: 2026-04-16T06:30:01.133608+00:00