# Integration Log: scr_01435
Started: 2026-04-16T08:48:29.824087+00:00
Description: Screening scr_01435 ds=iris_graph_signal graph=knn miss=[0.4] mode=lambda

## Dataset: iris_graph_signal | rows=24
  Graph: knn__k7 built OK
    tv | MR=0.2 | seed=0 | MAE=1.1964e-01 | t=0.0516s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.2859e-01 | t=0.0025s
    trss | MR=0.2 | seed=0 | MAE=7.5322e-02 | t=0.0026s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=4.1579e-01 | t=0.0182s
    tv | MR=0.2 | seed=1 | MAE=1.3691e-01 | t=0.0535s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=2.3484e-01 | t=0.0025s
    trss | MR=0.2 | seed=1 | MAE=8.3789e-02 | t=0.0026s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=4.1664e-01 | t=0.0182s
    tv | MR=0.2 | seed=0 | MAE=1.2279e-01 | t=0.0518s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.7710e-01 | t=0.0025s
    trss | MR=0.2 | seed=0 | MAE=7.6621e-02 | t=0.0032s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=4.7619e-01 | t=0.0476s

Completed: 2026-04-16T08:48:29.824946+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.