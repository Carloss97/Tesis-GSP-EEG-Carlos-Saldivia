# Integration Log: scr_00679
Started: 2026-04-16T15:17:32.981254+00:00
Description: Screening scr_00679 ds=iris_graph_signal graph=knn miss=[0.4] mode=base

## Dataset: iris_graph_signal | rows=14
  Graph: knn__k7 built OK
    mean | MR=0.4 | seed=0 | MAE=2.7644e-01 | t=0.0014s
    nearest | MR=0.4 | seed=0 | MAE=3.5475e-01 | t=0.0020s
    tikhonov | MR=0.4 | seed=0 | MAE=3.6513e-01 | t=0.0363s
    tv | MR=0.4 | seed=0 | MAE=2.7676e-01 | t=0.1458s
    trss | MR=0.4 | seed=0 | MAE=2.3848e-01 | t=0.0037s
    graph_time_tikhonov | MR=0.4 | seed=0 | MAE=4.5934e-01 | t=0.0037s
    temporal_laplacian | MR=0.4 | seed=0 | MAE=7.0364e-01 | t=7.4645s
    mean | MR=0.4 | seed=1 | MAE=2.5974e-01 | t=0.0016s
    nearest | MR=0.4 | seed=1 | MAE=3.7471e-01 | t=0.0020s
    tikhonov | MR=0.4 | seed=1 | MAE=3.6275e-01 | t=0.0034s
    tv | MR=0.4 | seed=1 | MAE=2.5927e-01 | t=0.2528s
    trss | MR=0.4 | seed=1 | MAE=2.1786e-01 | t=0.0066s

Completed: 2026-04-16T15:17:32.983745+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.