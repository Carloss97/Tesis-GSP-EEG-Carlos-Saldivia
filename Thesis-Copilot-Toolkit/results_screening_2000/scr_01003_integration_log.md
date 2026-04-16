# Integration Log: scr_01003
Started: 2026-04-16T12:51:09.394366+00:00
Description: Screening scr_01003 ds=iris_graph_signal graph=knn miss=3ch mode=lambda

## Dataset: iris_graph_signal | rows=24
  Graph: knn__k7 built OK
    tv | MR=0.2 | seed=0 | MAE=1.1964e-01 | t=0.0531s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.2859e-01 | t=0.0025s
    trss | MR=0.2 | seed=0 | MAE=7.5322e-02 | t=0.0026s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=4.1579e-01 | t=0.3295s
    tv | MR=0.2 | seed=1 | MAE=1.3691e-01 | t=0.0564s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=2.3484e-01 | t=0.0030s
    trss | MR=0.2 | seed=1 | MAE=8.3789e-02 | t=0.0027s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=4.1664e-01 | t=0.4994s
    tv | MR=0.2 | seed=0 | MAE=1.2279e-01 | t=0.0520s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.7710e-01 | t=0.0025s
    trss | MR=0.2 | seed=0 | MAE=7.6621e-02 | t=0.0026s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=4.7619e-01 | t=0.4777s

Completed: 2026-04-16T12:51:09.395221+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.