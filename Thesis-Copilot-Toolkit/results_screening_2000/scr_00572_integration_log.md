# Integration Log: scr_00572
Started: 2026-04-16T14:22:51.387793+00:00
Description: Screening scr_00572 ds=movielens_graph_signal graph=knn miss=[0.3] mode=base

## Dataset: movielens_graph_signal | rows=14
  Graph: knn__k7 built OK
    mean | MR=0.3 | seed=0 | MAE=6.3154e-02 | t=0.0041s
    nearest | MR=0.3 | seed=0 | MAE=6.7099e-02 | t=0.0072s
    tikhonov | MR=0.3 | seed=0 | MAE=1.1795e-01 | t=0.0058s
    tv | MR=0.3 | seed=0 | MAE=6.3138e-02 | t=0.1672s
    trss | MR=0.3 | seed=0 | MAE=7.4380e-02 | t=0.0188s
    graph_time_tikhonov | MR=0.3 | seed=0 | MAE=1.7034e-01 | t=0.0083s
    temporal_laplacian | MR=0.3 | seed=0 | MAE=1.5989e-01 | t=23.3950s
    mean | MR=0.3 | seed=1 | MAE=6.5229e-02 | t=0.0030s
    nearest | MR=0.3 | seed=1 | MAE=6.3035e-02 | t=0.0127s
    tikhonov | MR=0.3 | seed=1 | MAE=1.1929e-01 | t=0.0060s
    tv | MR=0.3 | seed=1 | MAE=6.5236e-02 | t=0.2069s
    trss | MR=0.3 | seed=1 | MAE=8.2920e-02 | t=0.0199s

Completed: 2026-04-16T14:22:51.388839+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.