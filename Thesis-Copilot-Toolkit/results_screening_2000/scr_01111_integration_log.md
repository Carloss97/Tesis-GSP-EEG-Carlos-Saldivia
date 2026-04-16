# Integration Log: scr_01111
Started: 2026-04-16T13:54:10.618992+00:00
Description: Screening scr_01111 ds=iris_graph_signal graph=knn miss=[0.1] mode=lambda

## Dataset: iris_graph_signal | rows=24
  Graph: knn__k7 built OK
    tv | MR=0.2 | seed=0 | MAE=1.1964e-01 | t=0.1649s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.2859e-01 | t=0.0049s
    trss | MR=0.2 | seed=0 | MAE=7.5322e-02 | t=0.0037s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=4.1579e-01 | t=9.3138s
    tv | MR=0.2 | seed=1 | MAE=1.3691e-01 | t=0.0612s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=2.3484e-01 | t=0.0025s
    trss | MR=0.2 | seed=1 | MAE=8.3789e-02 | t=0.0026s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=4.1664e-01 | t=0.7337s
    tv | MR=0.2 | seed=0 | MAE=1.2279e-01 | t=0.0549s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.7710e-01 | t=0.0025s
    trss | MR=0.2 | seed=0 | MAE=7.6621e-02 | t=0.0029s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=4.7619e-01 | t=0.4838s

Completed: 2026-04-16T13:54:10.619713+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.