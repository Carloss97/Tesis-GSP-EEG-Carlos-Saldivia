# Integration Log: scr_00355
Started: 2026-04-16T13:07:44.510623+00:00
Description: Screening scr_00355 ds=iris_graph_signal graph=knn miss=[0.1] mode=base

## Dataset: iris_graph_signal | rows=14
  Graph: knn__k7 built OK
    mean | MR=0.1 | seed=0 | MAE=1.2881e-01 | t=0.0015s
    nearest | MR=0.1 | seed=0 | MAE=1.6484e-01 | t=0.0015s
    tikhonov | MR=0.1 | seed=0 | MAE=2.6554e-01 | t=0.0035s
    tv | MR=0.1 | seed=0 | MAE=1.2451e-01 | t=0.1231s
    trss | MR=0.1 | seed=0 | MAE=1.0078e-01 | t=0.0093s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=4.2277e-01 | t=0.0042s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=6.6155e-01 | t=4.1465s
    mean | MR=0.1 | seed=1 | MAE=1.3930e-01 | t=0.0010s
    nearest | MR=0.1 | seed=1 | MAE=1.5346e-01 | t=0.0010s
    tikhonov | MR=0.1 | seed=1 | MAE=2.7035e-01 | t=0.0026s
    tv | MR=0.1 | seed=1 | MAE=1.3724e-01 | t=0.0523s
    trss | MR=0.1 | seed=1 | MAE=1.1048e-01 | t=0.0026s

Completed: 2026-04-16T13:07:44.511349+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.