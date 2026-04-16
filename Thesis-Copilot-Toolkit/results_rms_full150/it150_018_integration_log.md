# Integration Log: it150_018
Started: 2026-04-15T00:25:23.929190+00:00
Description: Bulk normalized run it150_018 dataset=iv100hz_mat graph=knn miss=[0.1] mode=base

## Dataset: iv100hz_mat | rows=42
  Graph: knn__k5 built OK
    mean | MR=0.1 | seed=0 | MAE=8.1185e-03 | t=0.0030s
    nearest | MR=0.1 | seed=0 | MAE=1.2947e-02 | t=0.0042s
    tikhonov | MR=0.1 | seed=0 | MAE=4.2692e-02 | t=0.0082s
    tv | MR=0.1 | seed=0 | MAE=5.9865e-03 | t=0.1915s
    trss | MR=0.1 | seed=0 | MAE=6.1407e-03 | t=0.0182s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=7.4281e-02 | t=0.0122s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=8.6073e-02 | t=1.6863s
    mean | MR=0.1 | seed=1 | MAE=8.3274e-03 | t=0.0022s
    nearest | MR=0.1 | seed=1 | MAE=1.3348e-02 | t=0.0030s
    tikhonov | MR=0.1 | seed=1 | MAE=4.2938e-02 | t=0.0072s
    tv | MR=0.1 | seed=1 | MAE=6.4382e-03 | t=0.2011s
    trss | MR=0.1 | seed=1 | MAE=6.3725e-03 | t=0.0179s

Completed: 2026-04-15T00:25:23.930096+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.