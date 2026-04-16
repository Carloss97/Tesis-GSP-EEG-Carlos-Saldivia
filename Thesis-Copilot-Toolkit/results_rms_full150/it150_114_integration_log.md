# Integration Log: it150_114
Started: 2026-04-15T00:43:16.557530+00:00
Description: Bulk normalized run it150_114 dataset=iv100hz_mat graph=knn miss=[0.2] mode=base

## Dataset: iv100hz_mat | rows=42
  Graph: knn__k5 built OK
    mean | MR=0.2 | seed=0 | MAE=1.6829e-02 | t=0.0020s
    nearest | MR=0.2 | seed=0 | MAE=2.5741e-02 | t=0.0050s
    tikhonov | MR=0.2 | seed=0 | MAE=4.8417e-02 | t=0.0081s
    tv | MR=0.2 | seed=0 | MAE=1.3571e-02 | t=0.2182s
    trss | MR=0.2 | seed=0 | MAE=1.3145e-02 | t=0.0213s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=7.6598e-02 | t=0.0110s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=8.9000e-02 | t=2.5263s
    mean | MR=0.2 | seed=1 | MAE=1.6767e-02 | t=0.0025s
    nearest | MR=0.2 | seed=1 | MAE=2.5796e-02 | t=0.0063s
    tikhonov | MR=0.2 | seed=1 | MAE=4.8597e-02 | t=0.0088s
    tv | MR=0.2 | seed=1 | MAE=1.3162e-02 | t=0.2182s
    trss | MR=0.2 | seed=1 | MAE=1.3378e-02 | t=0.0222s

Completed: 2026-04-15T00:43:16.558905+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.