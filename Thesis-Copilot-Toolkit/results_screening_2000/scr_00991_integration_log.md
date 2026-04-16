# Integration Log: scr_00991
Started: 2026-04-16T12:46:57.243996+00:00
Description: Screening scr_00991 ds=iris_graph_signal graph=knn miss=3ch mode=lambda

## Dataset: iris_graph_signal | rows=24
  Graph: knn__k5 built OK
    tv | MR=0.2 | seed=0 | MAE=1.1964e-01 | t=0.1056s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.2859e-01 | t=0.0031s
    trss | MR=0.2 | seed=0 | MAE=7.5322e-02 | t=0.0048s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=4.1579e-01 | t=3.9522s
    tv | MR=0.2 | seed=1 | MAE=1.3691e-01 | t=0.1098s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=2.3484e-01 | t=0.0035s
    trss | MR=0.2 | seed=1 | MAE=8.3789e-02 | t=0.0026s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=4.1664e-01 | t=0.4191s
    tv | MR=0.2 | seed=0 | MAE=1.2279e-01 | t=0.0533s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.7710e-01 | t=0.0026s
    trss | MR=0.2 | seed=0 | MAE=7.6621e-02 | t=0.0026s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=4.7619e-01 | t=0.3965s

Completed: 2026-04-16T12:46:57.244955+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.