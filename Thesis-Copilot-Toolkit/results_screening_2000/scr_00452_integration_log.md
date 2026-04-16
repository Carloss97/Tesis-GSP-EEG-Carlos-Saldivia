# Integration Log: scr_00452
Started: 2026-04-16T13:36:15.489628+00:00
Description: Screening scr_00452 ds=movielens_graph_signal graph=knn miss=[0.2] mode=base

## Dataset: movielens_graph_signal | rows=14
  Graph: knn__k5 built OK
    mean | MR=0.2 | seed=0 | MAE=4.4107e-02 | t=0.0030s
    nearest | MR=0.2 | seed=0 | MAE=4.5789e-02 | t=0.0254s
    tikhonov | MR=0.2 | seed=0 | MAE=9.3531e-02 | t=0.0092s
    tv | MR=0.2 | seed=0 | MAE=4.4026e-02 | t=0.5690s
    trss | MR=0.2 | seed=0 | MAE=5.3042e-02 | t=0.2771s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.5712e-01 | t=0.0982s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.5212e-01 | t=7.1566s
    mean | MR=0.2 | seed=1 | MAE=4.2780e-02 | t=0.0020s
    nearest | MR=0.2 | seed=1 | MAE=4.0779e-02 | t=0.0050s
    tikhonov | MR=0.2 | seed=1 | MAE=9.8467e-02 | t=0.0057s
    tv | MR=0.2 | seed=1 | MAE=4.2830e-02 | t=0.1803s
    trss | MR=0.2 | seed=1 | MAE=5.8726e-02 | t=0.2912s

Completed: 2026-04-16T13:36:15.490442+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.