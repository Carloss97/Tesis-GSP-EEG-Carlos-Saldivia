# Integration Log: scr_00992
Started: 2026-04-16T12:47:36.560321+00:00
Description: Screening scr_00992 ds=movielens_graph_signal graph=knn miss=3ch mode=lambda

## Dataset: movielens_graph_signal | rows=24
  Graph: knn__k5 built OK
    tv | MR=0.2 | seed=0 | MAE=4.3804e-02 | t=0.1490s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=9.5350e-02 | t=0.0077s
    trss | MR=0.2 | seed=0 | MAE=7.6762e-02 | t=0.0187s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.1969e-01 | t=8.4038s
    tv | MR=0.2 | seed=1 | MAE=4.2969e-02 | t=0.3839s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=1.0041e-01 | t=0.0129s
    trss | MR=0.2 | seed=1 | MAE=8.4022e-02 | t=0.2474s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.2400e-01 | t=9.1448s
    tv | MR=0.2 | seed=0 | MAE=4.3948e-02 | t=0.3103s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.1189e-01 | t=0.0209s
    trss | MR=0.2 | seed=0 | MAE=7.2102e-02 | t=0.4538s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.2814e-01 | t=2.0059s

Completed: 2026-04-16T12:47:36.561049+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.