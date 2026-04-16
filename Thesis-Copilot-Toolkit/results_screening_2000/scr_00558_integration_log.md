# Integration Log: scr_00558
Started: 2026-04-16T14:15:12.840075+00:00
Description: Screening scr_00558 ds=iv100hz_mat graph=knn miss=[0.3] mode=base

## Dataset: iv100hz_mat | rows=14
  Graph: knn__k5 built OK
    mean | MR=0.3 | seed=0 | MAE=7.3919e+01 | t=0.0032s
    nearest | MR=0.3 | seed=0 | MAE=1.1253e+02 | t=0.0100s
    tikhonov | MR=0.3 | seed=0 | MAE=1.4188e+02 | t=0.0069s
    tv | MR=0.3 | seed=0 | MAE=6.5186e+01 | t=0.2616s
    trss | MR=0.3 | seed=0 | MAE=6.3607e+01 | t=0.2402s
    graph_time_tikhonov | MR=0.3 | seed=0 | MAE=1.9725e+02 | t=0.0092s
    temporal_laplacian | MR=0.3 | seed=0 | MAE=2.3312e+02 | t=33.3627s
    mean | MR=0.3 | seed=1 | MAE=7.2756e+01 | t=0.0263s
    nearest | MR=0.3 | seed=1 | MAE=1.1224e+02 | t=0.0120s
    tikhonov | MR=0.3 | seed=1 | MAE=1.4171e+02 | t=0.0060s
    tv | MR=0.3 | seed=1 | MAE=6.6648e+01 | t=0.2756s
    trss | MR=0.3 | seed=1 | MAE=6.2621e+01 | t=0.3378s

Completed: 2026-04-16T14:15:12.840993+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.