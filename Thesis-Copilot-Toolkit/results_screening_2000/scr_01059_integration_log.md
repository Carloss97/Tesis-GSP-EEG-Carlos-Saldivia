# Integration Log: scr_01059
Started: 2026-04-16T13:10:52.525792+00:00
Description: Screening scr_01059 ds=bci_iv2a_real_s1 graph=vknng miss=3ch mode=lambda

## Dataset: bci_iv2a_real_s1 | rows=24
  Graph: vknng built OK
    tv | MR=0.2 | seed=0 | MAE=3.0346e-06 | t=0.1440s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=4.7043e-06 | t=0.0080s
    trss | MR=0.2 | seed=0 | MAE=1.0104e-06 | t=0.0203s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=8.8888e-06 | t=2.3995s
    tv | MR=0.2 | seed=1 | MAE=3.3726e-06 | t=0.2552s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=5.0223e-06 | t=0.0151s
    trss | MR=0.2 | seed=1 | MAE=1.2847e-06 | t=0.0873s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=9.0921e-06 | t=2.4596s
    tv | MR=0.2 | seed=0 | MAE=3.0352e-06 | t=0.2474s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=5.5039e-06 | t=0.0126s
    trss | MR=0.2 | seed=0 | MAE=1.1873e-06 | t=0.2696s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=9.7292e-06 | t=9.3492s

Completed: 2026-04-16T13:10:52.526598+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.