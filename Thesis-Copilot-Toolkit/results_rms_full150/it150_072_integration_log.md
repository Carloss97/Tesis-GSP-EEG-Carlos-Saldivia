# Integration Log: it150_072
Started: 2026-04-15T00:51:33.154163+00:00
Description: Bulk normalized run it150_072 dataset=synthetic_16ch graph=knng miss=[0.1] mode=base

## Dataset: synthetic_16ch | rows=14
  Graph: knng built OK
    mean | MR=0.1 | seed=0 | MAE=4.3607e-02 | t=0.0139s
    nearest | MR=0.1 | seed=0 | MAE=5.6541e-02 | t=0.0037s
    tikhonov | MR=0.1 | seed=0 | MAE=2.1342e-01 | t=0.0125s
    tv | MR=0.1 | seed=0 | MAE=4.5175e-02 | t=0.1879s
    trss | MR=0.1 | seed=0 | MAE=3.3546e-02 | t=0.0177s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=4.2916e-01 | t=0.0110s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=6.5087e-01 | t=1.1999s
    mean | MR=0.1 | seed=1 | MAE=4.3636e-02 | t=0.0031s
    nearest | MR=0.1 | seed=1 | MAE=5.7009e-02 | t=0.0029s
    tikhonov | MR=0.1 | seed=1 | MAE=2.1230e-01 | t=0.0107s
    tv | MR=0.1 | seed=1 | MAE=4.4798e-02 | t=0.1953s
    trss | MR=0.1 | seed=1 | MAE=3.2584e-02 | t=0.0179s

Completed: 2026-04-15T00:51:33.154925+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.