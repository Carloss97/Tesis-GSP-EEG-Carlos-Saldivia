# Integration Log: scr_00870
Started: 2026-04-16T12:07:45.669543+00:00
Description: Screening scr_00870 ds=iv100hz_mat graph=knn miss=2ch mode=lambda

## Dataset: iv100hz_mat | rows=24
  Graph: knn__k3 built OK
    tv | MR=0.2 | seed=0 | MAE=5.1206e+01 | t=0.1442s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=8.9974e+01 | t=0.0080s
    trss | MR=0.2 | seed=0 | MAE=1.2847e+01 | t=0.0189s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.5872e+02 | t=1.3038s
    tv | MR=0.2 | seed=1 | MAE=5.1152e+01 | t=0.1425s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=9.1246e+01 | t=0.0078s
    trss | MR=0.2 | seed=1 | MAE=1.2922e+01 | t=0.0198s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.5936e+02 | t=1.3456s
    tv | MR=0.2 | seed=0 | MAE=4.9607e+01 | t=0.1429s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.0930e+02 | t=0.0080s
    trss | MR=0.2 | seed=0 | MAE=1.8138e+01 | t=0.0184s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.6636e+02 | t=1.2987s

Completed: 2026-04-16T12:07:45.670398+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.