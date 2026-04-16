# Integration Log: scr_00882
Started: 2026-04-16T12:09:16.950325+00:00
Description: Screening scr_00882 ds=iv100hz_mat graph=knn miss=2ch mode=lambda

## Dataset: iv100hz_mat | rows=24
  Graph: knn__k5 built OK
    tv | MR=0.2 | seed=0 | MAE=4.2133e+01 | t=0.1469s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.0243e+02 | t=0.0078s
    trss | MR=0.2 | seed=0 | MAE=1.2822e+01 | t=0.0191s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.6094e+02 | t=1.3282s
    tv | MR=0.2 | seed=1 | MAE=4.2421e+01 | t=0.1450s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=1.0275e+02 | t=0.0081s
    trss | MR=0.2 | seed=1 | MAE=1.2982e+01 | t=0.0194s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.6121e+02 | t=1.3445s
    tv | MR=0.2 | seed=0 | MAE=4.2161e+01 | t=0.1487s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.2748e+02 | t=0.0079s
    trss | MR=0.2 | seed=0 | MAE=1.8183e+01 | t=0.0189s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.7262e+02 | t=1.3042s

Completed: 2026-04-16T12:09:16.951176+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.