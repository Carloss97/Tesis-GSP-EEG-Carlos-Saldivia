# Integration Log: it150_022
Started: 2026-04-15T00:46:47.882009+00:00
Description: Bulk normalized run it150_022 dataset=synthetic_beta graph=knn miss=[0.1] mode=base

## Dataset: synthetic_beta | rows=14
  Graph: knn__k5 built OK
    mean | MR=0.1 | seed=0 | MAE=4.3607e-02 | t=0.0033s
    nearest | MR=0.1 | seed=0 | MAE=5.6541e-02 | t=0.0025s
    tikhonov | MR=0.1 | seed=0 | MAE=2.5503e-01 | t=0.0114s
    tv | MR=0.1 | seed=0 | MAE=4.3240e-02 | t=0.2932s
    trss | MR=0.1 | seed=0 | MAE=2.9867e-02 | t=0.0348s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=4.7271e-01 | t=0.0164s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=7.2205e-01 | t=3.4463s
    mean | MR=0.1 | seed=1 | MAE=4.3636e-02 | t=0.0039s
    nearest | MR=0.1 | seed=1 | MAE=5.7009e-02 | t=0.0023s
    tikhonov | MR=0.1 | seed=1 | MAE=2.5465e-01 | t=0.0090s
    tv | MR=0.1 | seed=1 | MAE=4.3395e-02 | t=0.1947s
    trss | MR=0.1 | seed=1 | MAE=3.0511e-02 | t=0.0163s

Completed: 2026-04-15T00:46:47.883157+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.