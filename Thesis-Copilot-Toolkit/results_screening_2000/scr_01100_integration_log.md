# Integration Log: scr_01100
Started: 2026-04-16T13:45:41.783902+00:00
Description: Screening scr_01100 ds=movielens_graph_signal graph=knn miss=[0.1] mode=lambda

## Dataset: movielens_graph_signal | rows=24
  Graph: knn__k5 built OK
    tv | MR=0.2 | seed=0 | MAE=4.3804e-02 | t=0.1560s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=9.5350e-02 | t=0.0083s
    trss | MR=0.2 | seed=0 | MAE=7.6762e-02 | t=0.0191s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.1969e-01 | t=14.2877s
    tv | MR=0.2 | seed=1 | MAE=4.2969e-02 | t=0.5789s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=1.0041e-01 | t=0.0609s
    trss | MR=0.2 | seed=1 | MAE=8.4022e-02 | t=0.4338s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.2400e-01 | t=5.9376s
    tv | MR=0.2 | seed=0 | MAE=4.3948e-02 | t=0.5851s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.1189e-01 | t=0.1180s
    trss | MR=0.2 | seed=0 | MAE=7.2102e-02 | t=0.1410s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.2814e-01 | t=17.2458s

Completed: 2026-04-16T13:45:41.784687+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.