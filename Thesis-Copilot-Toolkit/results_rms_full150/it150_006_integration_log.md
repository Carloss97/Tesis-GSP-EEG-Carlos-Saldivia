# Integration Log: it150_006
Started: 2026-04-15T00:23:11.635649+00:00
Description: Bulk normalized run it150_006 dataset=iv100hz_mat graph=knn miss=[0.1] mode=base

## Dataset: iv100hz_mat | rows=42
  Graph: knn__k3 built OK
    mean | MR=0.1 | seed=0 | MAE=8.1185e-03 | t=0.0027s
    nearest | MR=0.1 | seed=0 | MAE=1.2947e-02 | t=0.0039s
    tikhonov | MR=0.1 | seed=0 | MAE=3.3710e-02 | t=0.0099s
    tv | MR=0.1 | seed=0 | MAE=6.5351e-03 | t=0.1962s
    trss | MR=0.1 | seed=0 | MAE=6.2655e-03 | t=0.0206s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=6.4607e-02 | t=0.0106s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=7.8369e-02 | t=3.1124s
    mean | MR=0.1 | seed=1 | MAE=8.3274e-03 | t=0.0024s
    nearest | MR=0.1 | seed=1 | MAE=1.3348e-02 | t=0.0033s
    tikhonov | MR=0.1 | seed=1 | MAE=3.4063e-02 | t=0.0080s
    tv | MR=0.1 | seed=1 | MAE=7.5834e-03 | t=0.1961s
    trss | MR=0.1 | seed=1 | MAE=6.6430e-03 | t=0.0190s

Completed: 2026-04-15T00:23:11.636485+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.