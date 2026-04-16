# Integration Log: scr_00342
Started: 2026-04-16T13:05:41.321208+00:00
Description: Screening scr_00342 ds=iv100hz_mat graph=knn miss=[0.1] mode=base

## Dataset: iv100hz_mat | rows=14
  Graph: knn__k5 built OK
    mean | MR=0.1 | seed=0 | MAE=2.0300e+01 | t=0.0020s
    nearest | MR=0.1 | seed=0 | MAE=3.2925e+01 | t=0.0028s
    tikhonov | MR=0.1 | seed=0 | MAE=1.0542e+02 | t=0.0062s
    tv | MR=0.1 | seed=0 | MAE=1.4325e+01 | t=0.1687s
    trss | MR=0.1 | seed=0 | MAE=1.5424e+01 | t=0.0171s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=1.8283e+02 | t=0.0079s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=2.1417e+02 | t=6.7561s
    mean | MR=0.1 | seed=1 | MAE=2.0537e+01 | t=0.0021s
    nearest | MR=0.1 | seed=1 | MAE=3.3573e+01 | t=0.0027s
    tikhonov | MR=0.1 | seed=1 | MAE=1.0576e+02 | t=0.0056s
    tv | MR=0.1 | seed=1 | MAE=1.5275e+01 | t=0.1458s
    trss | MR=0.1 | seed=1 | MAE=1.5785e+01 | t=0.0180s

Completed: 2026-04-16T13:05:41.321968+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.