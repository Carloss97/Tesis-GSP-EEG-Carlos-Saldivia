# Integration Log: it150_024
Started: 2026-04-15T00:47:14.534234+00:00
Description: Bulk normalized run it150_024 dataset=synthetic_16ch graph=knn miss=[0.1] mode=base

## Dataset: synthetic_16ch | rows=14
  Graph: knn__k5 built OK
    mean | MR=0.1 | seed=0 | MAE=4.3607e-02 | t=0.0151s
    nearest | MR=0.1 | seed=0 | MAE=5.6541e-02 | t=0.0115s
    tikhonov | MR=0.1 | seed=0 | MAE=2.5503e-01 | t=0.0170s
    tv | MR=0.1 | seed=0 | MAE=4.3240e-02 | t=0.3877s
    trss | MR=0.1 | seed=0 | MAE=2.9867e-02 | t=0.1180s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=4.7271e-01 | t=0.0188s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=7.2205e-01 | t=5.1018s
    mean | MR=0.1 | seed=1 | MAE=4.3636e-02 | t=0.0030s
    nearest | MR=0.1 | seed=1 | MAE=5.7009e-02 | t=0.0034s
    tikhonov | MR=0.1 | seed=1 | MAE=2.5465e-01 | t=0.0087s
    tv | MR=0.1 | seed=1 | MAE=4.3395e-02 | t=0.1931s
    trss | MR=0.1 | seed=1 | MAE=3.0511e-02 | t=0.0157s

Completed: 2026-04-15T00:47:14.535595+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.