# Integration Log: scr_00548
Started: 2026-04-16T14:10:46.203819+00:00
Description: Screening scr_00548 ds=movielens_graph_signal graph=knn miss=[0.3] mode=base

## Dataset: movielens_graph_signal | rows=14
  Graph: knn__k3 built OK
    mean | MR=0.3 | seed=0 | MAE=6.3154e-02 | t=0.0037s
    nearest | MR=0.3 | seed=0 | MAE=6.7099e-02 | t=0.0223s
    tikhonov | MR=0.3 | seed=0 | MAE=9.3897e-02 | t=0.0087s
    tv | MR=0.3 | seed=0 | MAE=6.3026e-02 | t=0.4901s
    trss | MR=0.3 | seed=0 | MAE=7.7630e-02 | t=0.4748s
    graph_time_tikhonov | MR=0.3 | seed=0 | MAE=1.4807e-01 | t=0.0122s
    temporal_laplacian | MR=0.3 | seed=0 | MAE=1.5257e-01 | t=6.7163s
    mean | MR=0.3 | seed=1 | MAE=6.5229e-02 | t=0.0020s
    nearest | MR=0.3 | seed=1 | MAE=6.3035e-02 | t=0.0064s
    tikhonov | MR=0.3 | seed=1 | MAE=9.6437e-02 | t=0.0060s
    tv | MR=0.3 | seed=1 | MAE=6.5271e-02 | t=0.1448s
    trss | MR=0.3 | seed=1 | MAE=8.2012e-02 | t=0.0198s

Completed: 2026-04-16T14:10:46.204573+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.