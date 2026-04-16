# Integration Log: it150_116
Started: 2026-04-15T00:43:55.610001+00:00
Description: Bulk normalized run it150_116 dataset=movielens_graph_signal graph=knn miss=[0.2] mode=base

## Dataset: movielens_graph_signal | rows=42
  Graph: knn__k5 built OK
    mean | MR=0.2 | seed=0 | MAE=3.6531e-02 | t=0.0031s
    nearest | MR=0.2 | seed=0 | MAE=3.6765e-02 | t=0.0057s
    tikhonov | MR=0.2 | seed=0 | MAE=9.6884e-02 | t=0.0098s
    tv | MR=0.2 | seed=0 | MAE=3.6484e-02 | t=0.2192s
    trss | MR=0.2 | seed=0 | MAE=4.4493e-02 | t=0.0207s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.7009e-01 | t=0.0109s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.6279e-01 | t=4.5513s
    mean | MR=0.2 | seed=1 | MAE=4.0219e-02 | t=0.0021s
    nearest | MR=0.2 | seed=1 | MAE=4.7049e-02 | t=0.0075s
    tikhonov | MR=0.2 | seed=1 | MAE=9.9800e-02 | t=0.0081s
    tv | MR=0.2 | seed=1 | MAE=4.0243e-02 | t=0.2252s
    trss | MR=0.2 | seed=1 | MAE=5.1553e-02 | t=0.0228s

Completed: 2026-04-15T00:43:55.611229+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.