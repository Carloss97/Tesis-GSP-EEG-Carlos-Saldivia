# Integration Log: scr_01328
Started: 2026-04-16T08:35:20.362237+00:00
Description: Screening scr_01328 ds=movielens_graph_signal graph=knn miss=[0.3] mode=lambda

## Dataset: movielens_graph_signal | rows=24
  Graph: knn__k7 built OK
    tv | MR=0.2 | seed=0 | MAE=3.6459e-02 | t=0.1495s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.0616e-01 | t=0.0080s
    trss | MR=0.2 | seed=0 | MAE=6.4772e-02 | t=0.0190s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.3017e-01 | t=1.4523s
    tv | MR=0.2 | seed=1 | MAE=4.0244e-02 | t=0.1489s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=1.0694e-01 | t=0.0081s
    trss | MR=0.2 | seed=1 | MAE=7.2065e-02 | t=0.0192s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.2726e-01 | t=1.2692s
    tv | MR=0.2 | seed=0 | MAE=3.6494e-02 | t=0.1506s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.2899e-01 | t=0.0080s
    trss | MR=0.2 | seed=0 | MAE=6.1204e-02 | t=0.0189s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.3969e-01 | t=1.3479s

Completed: 2026-04-16T08:35:20.362947+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.