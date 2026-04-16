# Integration Log: scr_00439
Started: 2026-04-16T13:31:54.031078+00:00
Description: Screening scr_00439 ds=iris_graph_signal graph=knn miss=[0.2] mode=base

## Dataset: iris_graph_signal | rows=14
  Graph: knn__k3 built OK
    mean | MR=0.2 | seed=0 | MAE=1.2881e-01 | t=0.0010s
    nearest | MR=0.2 | seed=0 | MAE=1.6484e-01 | t=0.0009s
    tikhonov | MR=0.2 | seed=0 | MAE=2.6763e-01 | t=0.0024s
    tv | MR=0.2 | seed=0 | MAE=1.2623e-01 | t=0.0511s
    trss | MR=0.2 | seed=0 | MAE=1.1223e-01 | t=0.0026s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=4.1809e-01 | t=0.0035s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=6.1214e-01 | t=1.6985s
    mean | MR=0.2 | seed=1 | MAE=1.3930e-01 | t=0.0014s
    nearest | MR=0.2 | seed=1 | MAE=1.5346e-01 | t=0.0071s
    tikhonov | MR=0.2 | seed=1 | MAE=2.7086e-01 | t=0.0034s
    tv | MR=0.2 | seed=1 | MAE=1.3868e-01 | t=0.1050s
    trss | MR=0.2 | seed=1 | MAE=1.2000e-01 | t=0.0036s

Completed: 2026-04-16T13:31:54.031964+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.