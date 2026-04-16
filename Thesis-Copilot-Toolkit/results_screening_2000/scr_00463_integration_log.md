# Integration Log: scr_00463
Started: 2026-04-16T13:39:47.093665+00:00
Description: Screening scr_00463 ds=iris_graph_signal graph=knn miss=[0.2] mode=base

## Dataset: iris_graph_signal | rows=14
  Graph: knn__k7 built OK
    mean | MR=0.2 | seed=0 | MAE=1.2881e-01 | t=0.0054s
    nearest | MR=0.2 | seed=0 | MAE=1.6484e-01 | t=0.0015s
    tikhonov | MR=0.2 | seed=0 | MAE=2.6554e-01 | t=0.0036s
    tv | MR=0.2 | seed=0 | MAE=1.2451e-01 | t=0.1206s
    trss | MR=0.2 | seed=0 | MAE=1.0078e-01 | t=0.0038s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=4.2277e-01 | t=0.0403s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=6.6155e-01 | t=6.3367s
    mean | MR=0.2 | seed=1 | MAE=1.3930e-01 | t=0.0017s
    nearest | MR=0.2 | seed=1 | MAE=1.5346e-01 | t=0.0015s
    tikhonov | MR=0.2 | seed=1 | MAE=2.7035e-01 | t=0.0048s
    tv | MR=0.2 | seed=1 | MAE=1.3724e-01 | t=0.2022s
    trss | MR=0.2 | seed=1 | MAE=1.1048e-01 | t=0.0037s

Completed: 2026-04-16T13:39:47.094794+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.