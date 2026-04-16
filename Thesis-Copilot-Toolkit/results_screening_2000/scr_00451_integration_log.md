# Integration Log: scr_00451
Started: 2026-04-16T13:35:43.662250+00:00
Description: Screening scr_00451 ds=iris_graph_signal graph=knn miss=[0.2] mode=base

## Dataset: iris_graph_signal | rows=14
  Graph: knn__k5 built OK
    mean | MR=0.2 | seed=0 | MAE=1.2881e-01 | t=0.0015s
    nearest | MR=0.2 | seed=0 | MAE=1.6484e-01 | t=0.0015s
    tikhonov | MR=0.2 | seed=0 | MAE=2.6554e-01 | t=0.0024s
    tv | MR=0.2 | seed=0 | MAE=1.2451e-01 | t=0.0529s
    trss | MR=0.2 | seed=0 | MAE=1.0078e-01 | t=0.0026s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=4.2277e-01 | t=0.0025s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=6.6155e-01 | t=0.6298s
    mean | MR=0.2 | seed=1 | MAE=1.3930e-01 | t=0.0009s
    nearest | MR=0.2 | seed=1 | MAE=1.5346e-01 | t=0.0016s
    tikhonov | MR=0.2 | seed=1 | MAE=2.7035e-01 | t=0.0030s
    tv | MR=0.2 | seed=1 | MAE=1.3724e-01 | t=0.0796s
    trss | MR=0.2 | seed=1 | MAE=1.1048e-01 | t=0.0035s

Completed: 2026-04-16T13:35:43.663108+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.