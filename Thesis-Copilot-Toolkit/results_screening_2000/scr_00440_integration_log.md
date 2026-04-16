# Integration Log: scr_00440
Started: 2026-04-16T13:32:23.678046+00:00
Description: Screening scr_00440 ds=movielens_graph_signal graph=knn miss=[0.2] mode=base

## Dataset: movielens_graph_signal | rows=14
  Graph: knn__k3 built OK
    mean | MR=0.2 | seed=0 | MAE=4.4107e-02 | t=0.0029s
    nearest | MR=0.2 | seed=0 | MAE=4.5789e-02 | t=0.0077s
    tikhonov | MR=0.2 | seed=0 | MAE=7.9729e-02 | t=0.0087s
    tv | MR=0.2 | seed=0 | MAE=4.3873e-02 | t=0.3487s
    trss | MR=0.2 | seed=0 | MAE=5.6190e-02 | t=0.0952s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.4231e-01 | t=0.0125s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.4762e-01 | t=9.7616s
    mean | MR=0.2 | seed=1 | MAE=4.2780e-02 | t=0.0031s
    nearest | MR=0.2 | seed=1 | MAE=4.0779e-02 | t=0.0430s
    tikhonov | MR=0.2 | seed=1 | MAE=8.4193e-02 | t=0.0088s
    tv | MR=0.2 | seed=1 | MAE=4.2955e-02 | t=0.4460s
    trss | MR=0.2 | seed=1 | MAE=5.9201e-02 | t=0.0914s

Completed: 2026-04-16T13:32:23.679230+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.