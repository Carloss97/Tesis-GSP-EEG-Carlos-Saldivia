# Integration Log: scr_00774
Started: 2026-04-16T11:55:24.451700+00:00
Description: Screening scr_00774 ds=iv100hz_mat graph=knn miss=1ch mode=lambda

## Dataset: iv100hz_mat | rows=24
  Graph: knn__k5 built OK
    tv | MR=0.2 | seed=0 | MAE=4.2133e+01 | t=0.1459s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.0243e+02 | t=0.0080s
    trss | MR=0.2 | seed=0 | MAE=1.2822e+01 | t=0.0188s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.6094e+02 | t=1.4295s
    tv | MR=0.2 | seed=1 | MAE=4.2421e+01 | t=0.1452s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=1.0275e+02 | t=0.0079s
    trss | MR=0.2 | seed=1 | MAE=1.2982e+01 | t=0.0184s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.6121e+02 | t=1.2799s
    tv | MR=0.2 | seed=0 | MAE=4.2161e+01 | t=0.1499s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.2748e+02 | t=0.0080s
    trss | MR=0.2 | seed=0 | MAE=1.8183e+01 | t=0.0184s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.7262e+02 | t=1.3359s

Completed: 2026-04-16T11:55:24.452455+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.