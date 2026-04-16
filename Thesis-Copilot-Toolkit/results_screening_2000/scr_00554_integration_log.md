# Integration Log: scr_00554
Started: 2026-04-16T14:11:30.675398+00:00
Description: Screening scr_00554 ds=physionet_real graph=knn miss=[0.3] mode=base

## Dataset: physionet_eegmmidb_real | rows=14
  Graph: knn__k5 built OK
    mean | MR=0.3 | seed=0 | MAE=7.1409e-06 | t=0.0031s
    nearest | MR=0.3 | seed=0 | MAE=8.1341e-06 | t=0.0106s
    tikhonov | MR=0.3 | seed=0 | MAE=8.6623e-06 | t=0.0088s
    tv | MR=0.3 | seed=0 | MAE=7.1084e-06 | t=0.1495s
    trss | MR=0.3 | seed=0 | MAE=3.7035e-06 | t=0.0187s
    graph_time_tikhonov | MR=0.3 | seed=0 | MAE=1.4741e-05 | t=0.0086s
    temporal_laplacian | MR=0.3 | seed=0 | MAE=3.3832e-05 | t=16.3324s
    mean | MR=0.3 | seed=1 | MAE=7.3000e-06 | t=0.0020s
    nearest | MR=0.3 | seed=1 | MAE=8.0659e-06 | t=0.0073s
    tikhonov | MR=0.3 | seed=1 | MAE=8.7340e-06 | t=0.0057s
    tv | MR=0.3 | seed=1 | MAE=7.2668e-06 | t=0.1941s
    trss | MR=0.3 | seed=1 | MAE=3.7616e-06 | t=0.0190s

Completed: 2026-04-16T14:11:30.676181+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.