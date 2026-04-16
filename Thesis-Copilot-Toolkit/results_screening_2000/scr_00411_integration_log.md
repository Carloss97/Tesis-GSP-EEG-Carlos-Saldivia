# Integration Log: scr_00411
Started: 2026-04-16T13:21:06.779419+00:00
Description: Screening scr_00411 ds=bci_iv2a_real_s1 graph=vknng miss=[0.1] mode=base

## Dataset: bci_iv2a_real_s1 | rows=14
  Graph: vknng built OK
    mean | MR=0.1 | seed=0 | MAE=1.3025e-06 | t=0.0020s
    nearest | MR=0.1 | seed=0 | MAE=1.3708e-06 | t=0.0027s
    tikhonov | MR=0.1 | seed=0 | MAE=3.7983e-06 | t=0.0057s
    tv | MR=0.1 | seed=0 | MAE=1.3025e-06 | t=0.2492s
    trss | MR=0.1 | seed=0 | MAE=9.8827e-07 | t=0.2473s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=8.1459e-06 | t=0.0300s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=1.2740e-05 | t=11.0062s
    mean | MR=0.1 | seed=1 | MAE=1.2372e-06 | t=0.0020s
    nearest | MR=0.1 | seed=1 | MAE=1.2545e-06 | t=0.0029s
    tikhonov | MR=0.1 | seed=1 | MAE=3.7340e-06 | t=0.0057s
    tv | MR=0.1 | seed=1 | MAE=1.2371e-06 | t=0.1594s
    trss | MR=0.1 | seed=1 | MAE=9.0847e-07 | t=0.0172s

Completed: 2026-04-16T13:21:06.780347+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.