# Integration Log: scr_01388
Started: 2026-04-16T08:42:45.729250+00:00
Description: Screening scr_01388 ds=movielens_graph_signal graph=vknng miss=[0.3] mode=lambda

## Dataset: movielens_graph_signal | rows=24
  Graph: vknng built OK
    tv | MR=0.2 | seed=0 | MAE=3.6198e-02 | t=0.1426s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=8.7391e-02 | t=0.0091s
    trss | MR=0.2 | seed=0 | MAE=6.2012e-02 | t=0.0195s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.2582e-01 | t=1.3114s
    tv | MR=0.2 | seed=1 | MAE=4.0343e-02 | t=0.1433s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=9.3729e-02 | t=0.0080s
    trss | MR=0.2 | seed=1 | MAE=7.3845e-02 | t=0.0196s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.2500e-01 | t=1.3179s
    tv | MR=0.2 | seed=0 | MAE=3.6353e-02 | t=0.1431s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.0518e-01 | t=0.0080s
    trss | MR=0.2 | seed=0 | MAE=5.8520e-02 | t=0.0200s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.3379e-01 | t=1.3890s

Completed: 2026-04-16T08:42:45.729950+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.