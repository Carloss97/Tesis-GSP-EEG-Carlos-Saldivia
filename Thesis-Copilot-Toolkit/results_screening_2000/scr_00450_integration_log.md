# Integration Log: scr_00450
Started: 2026-04-16T13:35:33.309244+00:00
Description: Screening scr_00450 ds=iv100hz_mat graph=knn miss=[0.2] mode=base

## Dataset: iv100hz_mat | rows=14
  Graph: knn__k5 built OK
    mean | MR=0.2 | seed=0 | MAE=5.2754e+01 | t=0.0020s
    nearest | MR=0.2 | seed=0 | MAE=8.0647e+01 | t=0.0058s
    tikhonov | MR=0.2 | seed=0 | MAE=1.2687e+02 | t=0.0060s
    tv | MR=0.2 | seed=0 | MAE=4.3341e+01 | t=0.1451s
    trss | MR=0.2 | seed=0 | MAE=4.2070e+01 | t=0.0185s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.9149e+02 | t=0.0090s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.2475e+02 | t=24.4619s
    mean | MR=0.2 | seed=1 | MAE=5.2652e+01 | t=0.0020s
    nearest | MR=0.2 | seed=1 | MAE=8.0770e+01 | t=0.0059s
    tikhonov | MR=0.2 | seed=1 | MAE=1.2722e+02 | t=0.0057s
    tv | MR=0.2 | seed=1 | MAE=4.8602e+01 | t=0.1562s
    trss | MR=0.2 | seed=1 | MAE=4.2891e+01 | t=0.0190s

Completed: 2026-04-16T13:35:33.310110+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.