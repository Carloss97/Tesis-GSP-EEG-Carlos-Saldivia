# Integration Log: scr_00560
Started: 2026-04-16T14:16:53.026535+00:00
Description: Screening scr_00560 ds=movielens_graph_signal graph=knn miss=[0.3] mode=base

## Dataset: movielens_graph_signal | rows=14
  Graph: knn__k5 built OK
    mean | MR=0.3 | seed=0 | MAE=6.3154e-02 | t=0.0031s
    nearest | MR=0.3 | seed=0 | MAE=6.7099e-02 | t=0.0420s
    tikhonov | MR=0.3 | seed=0 | MAE=1.0541e-01 | t=0.0088s
    tv | MR=0.3 | seed=0 | MAE=6.3110e-02 | t=0.3559s
    trss | MR=0.3 | seed=0 | MAE=7.3915e-02 | t=0.1239s
    graph_time_tikhonov | MR=0.3 | seed=0 | MAE=1.6091e-01 | t=0.0147s
    temporal_laplacian | MR=0.3 | seed=0 | MAE=1.5740e-01 | t=26.9709s
    mean | MR=0.3 | seed=1 | MAE=6.5229e-02 | t=0.0036s
    nearest | MR=0.3 | seed=1 | MAE=6.3035e-02 | t=0.0104s
    tikhonov | MR=0.3 | seed=1 | MAE=1.0847e-01 | t=0.0309s
    tv | MR=0.3 | seed=1 | MAE=6.5234e-02 | t=0.8218s
    trss | MR=0.3 | seed=1 | MAE=8.2243e-02 | t=0.2486s

Completed: 2026-04-16T14:16:53.027396+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.