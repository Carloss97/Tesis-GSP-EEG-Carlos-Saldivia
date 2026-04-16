# Integration Log: scr_00788
Started: 2026-04-16T11:57:11.328514+00:00
Description: Screening scr_00788 ds=movielens_graph_signal graph=knn miss=1ch mode=lambda

## Dataset: movielens_graph_signal | rows=24
  Graph: knn__k7 built OK
    tv | MR=0.2 | seed=0 | MAE=4.3965e-02 | t=0.1483s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.0307e-01 | t=0.0078s
    trss | MR=0.2 | seed=0 | MAE=7.6926e-02 | t=0.0190s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.2147e-01 | t=1.3175s
    tv | MR=0.2 | seed=1 | MAE=4.2862e-02 | t=0.1496s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=1.0805e-01 | t=0.0078s
    trss | MR=0.2 | seed=1 | MAE=8.4769e-02 | t=0.0186s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.2523e-01 | t=1.3830s
    tv | MR=0.2 | seed=0 | MAE=4.4035e-02 | t=0.1512s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.2243e-01 | t=0.0078s
    trss | MR=0.2 | seed=0 | MAE=7.1984e-02 | t=0.0184s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.3049e-01 | t=1.8780s

Completed: 2026-04-16T11:57:11.329380+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.