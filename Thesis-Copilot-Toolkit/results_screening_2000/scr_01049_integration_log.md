# Integration Log: scr_01049
Started: 2026-04-16T13:07:57.160699+00:00
Description: Screening scr_01049 ds=bci_iv2a_real_s3 graph=knng miss=3ch mode=lambda

## Dataset: bci_iv2a_real_s3 | rows=24
  Graph: knng built OK
    tv | MR=0.2 | seed=0 | MAE=7.3155e-07 | t=0.3564s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.6455e-06 | t=0.0197s
    trss | MR=0.2 | seed=0 | MAE=3.6633e-07 | t=0.1013s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.9615e-06 | t=3.4621s
    tv | MR=0.2 | seed=1 | MAE=7.3475e-07 | t=0.1852s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=1.6365e-06 | t=0.0121s
    trss | MR=0.2 | seed=1 | MAE=3.7370e-07 | t=0.0186s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=2.9702e-06 | t=15.1116s
    tv | MR=0.2 | seed=0 | MAE=7.3145e-07 | t=0.1555s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.9046e-06 | t=0.0078s
    trss | MR=0.2 | seed=0 | MAE=4.0538e-07 | t=0.0195s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=3.7146e-06 | t=7.5694s

Completed: 2026-04-16T13:07:57.161606+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.