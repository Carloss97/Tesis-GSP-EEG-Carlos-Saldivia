# Integration Log: scr_00354
Started: 2026-04-16T13:07:37.646320+00:00
Description: Screening scr_00354 ds=iv100hz_mat graph=knn miss=[0.1] mode=base

## Dataset: iv100hz_mat | rows=14
  Graph: knn__k7 built OK
    mean | MR=0.1 | seed=0 | MAE=2.0300e+01 | t=0.0031s
    nearest | MR=0.1 | seed=0 | MAE=3.2925e+01 | t=0.0028s
    tikhonov | MR=0.1 | seed=0 | MAE=1.1879e+02 | t=0.0060s
    tv | MR=0.1 | seed=0 | MAE=1.3851e+01 | t=0.1611s
    trss | MR=0.1 | seed=0 | MAE=1.4773e+01 | t=0.0167s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=1.9382e+02 | t=0.0097s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=2.3416e+02 | t=15.0682s
    mean | MR=0.1 | seed=1 | MAE=2.0537e+01 | t=0.0027s
    nearest | MR=0.1 | seed=1 | MAE=3.3573e+01 | t=0.0027s
    tikhonov | MR=0.1 | seed=1 | MAE=1.1899e+02 | t=0.0072s
    tv | MR=0.1 | seed=1 | MAE=1.4633e+01 | t=0.1516s
    trss | MR=0.1 | seed=1 | MAE=1.5067e+01 | t=0.0182s

Completed: 2026-04-16T13:07:37.647224+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.