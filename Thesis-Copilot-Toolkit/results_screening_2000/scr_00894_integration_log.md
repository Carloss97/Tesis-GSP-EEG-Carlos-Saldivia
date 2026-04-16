# Integration Log: scr_00894
Started: 2026-04-16T12:11:46.965966+00:00
Description: Screening scr_00894 ds=iv100hz_mat graph=knn miss=2ch mode=lambda

## Dataset: iv100hz_mat | rows=24
  Graph: knn__k7 built OK
    tv | MR=0.2 | seed=0 | MAE=3.9045e+01 | t=0.2266s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.1018e+02 | t=0.0081s
    trss | MR=0.2 | seed=0 | MAE=1.2509e+01 | t=0.0191s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.6536e+02 | t=2.0416s
    tv | MR=0.2 | seed=1 | MAE=4.0518e+01 | t=0.1540s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=1.1005e+02 | t=0.0085s
    trss | MR=0.2 | seed=1 | MAE=1.2666e+01 | t=0.0185s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.6527e+02 | t=14.4833s
    tv | MR=0.2 | seed=0 | MAE=3.8955e+01 | t=0.1511s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.3821e+02 | t=0.0079s
    trss | MR=0.2 | seed=0 | MAE=1.7509e+01 | t=0.0181s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.8200e+02 | t=10.9385s

Completed: 2026-04-16T12:11:46.966795+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.