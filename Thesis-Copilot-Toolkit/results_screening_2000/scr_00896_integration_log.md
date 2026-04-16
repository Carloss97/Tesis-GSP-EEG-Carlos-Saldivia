# Integration Log: scr_00896
Started: 2026-04-16T12:12:32.138098+00:00
Description: Screening scr_00896 ds=movielens_graph_signal graph=knn miss=2ch mode=lambda

## Dataset: movielens_graph_signal | rows=24
  Graph: knn__k7 built OK
    tv | MR=0.2 | seed=0 | MAE=4.3965e-02 | t=0.1507s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.0307e-01 | t=0.0098s
    trss | MR=0.2 | seed=0 | MAE=7.6926e-02 | t=0.0189s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.2147e-01 | t=3.1280s
    tv | MR=0.2 | seed=1 | MAE=4.2862e-02 | t=0.1671s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=1.0805e-01 | t=0.0154s
    trss | MR=0.2 | seed=1 | MAE=8.4769e-02 | t=0.3407s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.2523e-01 | t=9.8659s
    tv | MR=0.2 | seed=0 | MAE=4.4035e-02 | t=0.1543s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.2243e-01 | t=0.0079s
    trss | MR=0.2 | seed=0 | MAE=7.1984e-02 | t=0.0200s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.3049e-01 | t=8.8812s

Completed: 2026-04-16T12:12:32.139046+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.