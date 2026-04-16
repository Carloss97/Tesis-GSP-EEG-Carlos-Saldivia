# Integration Log: scr_00666
Started: 2026-04-16T15:09:42.269505+00:00
Description: Screening scr_00666 ds=iv100hz_mat graph=knn miss=[0.4] mode=base

## Dataset: iv100hz_mat | rows=14
  Graph: knn__k5 built OK
    mean | MR=0.4 | seed=0 | MAE=1.0557e+02 | t=0.0031s
    nearest | MR=0.4 | seed=0 | MAE=1.5725e+02 | t=0.0137s
    tikhonov | MR=0.4 | seed=0 | MAE=1.6401e+02 | t=0.0115s
    tv | MR=0.4 | seed=0 | MAE=1.1187e+02 | t=0.3553s
    trss | MR=0.4 | seed=0 | MAE=9.5676e+01 | t=0.3936s
    graph_time_tikhonov | MR=0.4 | seed=0 | MAE=2.0672e+02 | t=0.0124s
    temporal_laplacian | MR=0.4 | seed=0 | MAE=2.4326e+02 | t=30.4393s
    mean | MR=0.4 | seed=1 | MAE=1.0515e+02 | t=0.0356s
    nearest | MR=0.4 | seed=1 | MAE=1.5788e+02 | t=0.0437s
    tikhonov | MR=0.4 | seed=1 | MAE=1.6490e+02 | t=0.0088s
    tv | MR=0.4 | seed=1 | MAE=1.0481e+02 | t=0.5421s
    trss | MR=0.4 | seed=1 | MAE=9.5980e+01 | t=0.1224s

Completed: 2026-04-16T15:09:42.270684+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.