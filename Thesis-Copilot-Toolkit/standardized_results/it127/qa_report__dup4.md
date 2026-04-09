# QA Report: it127_noise_profile_non_gaussian

## Status: NO-GO

## Summary
- Total rows: 72
- Methods tested: 4
- Graphs: 1
- Missing scenarios: 1
- Best method: trss (MAE=1.3406e+01)

## Statistical Test (Mann-Whitney U: TV < Instant)
- TV median MAE:      1.3619e-01
- Instant median MAE: 2.1954e-01
- Gain:               38.0%
- p-value:            5.5511e-02
- Decision:           **NO-GO**

## Dataset availability snapshot
- bci_iv2a_real_s1: OK
- bci_iv2a_real_s2: OK
- bci_iv2a_real_s3: OK
- iris_graph_signal: OK
- iv100hz_mat: OK
- movielens_graph_signal: OK
- physionet_real: OK

Generated: 2026-04-07T17:41:49.060188+00:00