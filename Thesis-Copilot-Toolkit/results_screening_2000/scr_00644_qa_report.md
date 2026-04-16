# QA Report: scr_00644

## Status: NO-GO

## Summary
- Total rows: 14
- Methods tested: 7
- Graphs: 1
- Missing scenarios: 1
- Best method: tv (MAE=6.3993e-02)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      8.9798e-02
- Instant median MAE: 6.6164e-02
- Gain:               -35.7%
- p-value:            9.5937e-01
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

Generated: 2026-04-16T14:58:57.884041+00:00