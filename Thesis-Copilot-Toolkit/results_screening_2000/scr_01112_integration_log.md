# Integration Log: scr_01112
Started: 2026-04-16T13:55:54.144861+00:00
Description: Screening scr_01112 ds=movielens_graph_signal graph=knn miss=[0.1] mode=lambda

## Dataset: movielens_graph_signal | rows=24
  Graph: knn__k7 built OK
    tv | MR=0.2 | seed=0 | MAE=4.3965e-02 | t=0.1538s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.0307e-01 | t=0.0080s
    trss | MR=0.2 | seed=0 | MAE=7.6926e-02 | t=0.0200s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.2147e-01 | t=15.8499s
    tv | MR=0.2 | seed=1 | MAE=4.2862e-02 | t=0.3019s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=1.0805e-01 | t=0.0166s
    trss | MR=0.2 | seed=1 | MAE=8.4769e-02 | t=0.0248s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.2523e-01 | t=14.3892s
    tv | MR=0.2 | seed=0 | MAE=4.4035e-02 | t=0.2001s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.2243e-01 | t=0.0081s
    trss | MR=0.2 | seed=0 | MAE=7.1984e-02 | t=0.0203s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.3049e-01 | t=20.6794s

Completed: 2026-04-16T13:55:54.145551+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.