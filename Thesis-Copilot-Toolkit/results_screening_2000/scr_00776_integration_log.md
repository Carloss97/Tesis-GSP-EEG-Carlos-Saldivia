# Integration Log: scr_00776
Started: 2026-04-16T11:55:39.225284+00:00
Description: Screening scr_00776 ds=movielens_graph_signal graph=knn miss=1ch mode=lambda

## Dataset: movielens_graph_signal | rows=24
  Graph: knn__k5 built OK
    tv | MR=0.2 | seed=0 | MAE=4.3804e-02 | t=0.1455s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=9.5350e-02 | t=0.0082s
    trss | MR=0.2 | seed=0 | MAE=7.6762e-02 | t=0.0189s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.1969e-01 | t=1.3754s
    tv | MR=0.2 | seed=1 | MAE=4.2969e-02 | t=0.1474s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=1.0041e-01 | t=0.0083s
    trss | MR=0.2 | seed=1 | MAE=8.4022e-02 | t=0.0193s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.2400e-01 | t=1.2851s
    tv | MR=0.2 | seed=0 | MAE=4.3948e-02 | t=0.1445s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.1189e-01 | t=0.0082s
    trss | MR=0.2 | seed=0 | MAE=7.2102e-02 | t=0.0182s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.2814e-01 | t=1.2895s

Completed: 2026-04-16T11:55:39.226165+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.