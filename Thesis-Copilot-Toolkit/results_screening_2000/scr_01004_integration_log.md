# Integration Log: scr_01004
Started: 2026-04-16T12:51:56.705608+00:00
Description: Screening scr_01004 ds=movielens_graph_signal graph=knn miss=3ch mode=lambda

## Dataset: movielens_graph_signal | rows=24
  Graph: knn__k7 built OK
    tv | MR=0.2 | seed=0 | MAE=4.3965e-02 | t=0.5443s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.0307e-01 | t=0.0344s
    trss | MR=0.2 | seed=0 | MAE=7.6926e-02 | t=0.1303s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.2147e-01 | t=5.0767s
    tv | MR=0.2 | seed=1 | MAE=4.2862e-02 | t=0.1706s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=1.0805e-01 | t=0.0083s
    trss | MR=0.2 | seed=1 | MAE=8.4769e-02 | t=0.0187s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.2523e-01 | t=9.5276s
    tv | MR=0.2 | seed=0 | MAE=4.4035e-02 | t=0.1503s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.2243e-01 | t=0.0078s
    trss | MR=0.2 | seed=0 | MAE=7.1984e-02 | t=0.0197s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.3049e-01 | t=5.4593s

Completed: 2026-04-16T12:51:56.706445+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.