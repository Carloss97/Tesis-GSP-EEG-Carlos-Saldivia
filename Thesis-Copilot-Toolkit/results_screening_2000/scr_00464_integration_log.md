# Integration Log: scr_00464
Started: 2026-04-16T13:40:24.435197+00:00
Description: Screening scr_00464 ds=movielens_graph_signal graph=knn miss=[0.2] mode=base

## Dataset: movielens_graph_signal | rows=14
  Graph: knn__k7 built OK
    mean | MR=0.2 | seed=0 | MAE=4.4107e-02 | t=0.0031s
    nearest | MR=0.2 | seed=0 | MAE=4.5789e-02 | t=0.0300s
    tikhonov | MR=0.2 | seed=0 | MAE=1.0720e-01 | t=0.0107s
    tv | MR=0.2 | seed=0 | MAE=4.4071e-02 | t=0.6098s
    trss | MR=0.2 | seed=0 | MAE=5.2328e-02 | t=0.2388s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.6768e-01 | t=0.0716s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.5419e-01 | t=17.9331s
    mean | MR=0.2 | seed=1 | MAE=4.2780e-02 | t=0.0020s
    nearest | MR=0.2 | seed=1 | MAE=4.0779e-02 | t=0.0050s
    tikhonov | MR=0.2 | seed=1 | MAE=1.1186e-01 | t=0.0058s
    tv | MR=0.2 | seed=1 | MAE=4.2801e-02 | t=0.1590s
    trss | MR=0.2 | seed=1 | MAE=5.8147e-02 | t=0.2221s

Completed: 2026-04-16T13:40:24.435912+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.