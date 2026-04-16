# Integration Log: scr_00990
Started: 2026-04-16T12:46:40.752846+00:00
Description: Screening scr_00990 ds=iv100hz_mat graph=knn miss=3ch mode=lambda

## Dataset: iv100hz_mat | rows=24
  Graph: knn__k5 built OK
    tv | MR=0.2 | seed=0 | MAE=4.2133e+01 | t=0.2307s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.0243e+02 | t=0.0080s
    trss | MR=0.2 | seed=0 | MAE=1.2822e+01 | t=0.0192s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.6094e+02 | t=6.3858s
    tv | MR=0.2 | seed=1 | MAE=4.2421e+01 | t=0.2277s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=1.0275e+02 | t=0.0084s
    trss | MR=0.2 | seed=1 | MAE=1.2982e+01 | t=0.0199s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.6121e+02 | t=2.1440s
    tv | MR=0.2 | seed=0 | MAE=4.2161e+01 | t=0.1513s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.2748e+02 | t=0.0078s
    trss | MR=0.2 | seed=0 | MAE=1.8183e+01 | t=0.0189s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.7262e+02 | t=12.9569s

Completed: 2026-04-16T12:46:40.753649+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.