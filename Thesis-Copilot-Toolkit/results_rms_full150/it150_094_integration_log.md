# Integration Log: it150_094
Started: 2026-04-15T00:53:19.742468+00:00
Description: Bulk normalized run it150_094 dataset=synthetic_beta graph=aew miss=[0.1] mode=base

## Dataset: synthetic_beta | rows=14
  Graph: aew built OK
    mean | MR=0.1 | seed=0 | MAE=4.3607e-02 | t=0.0051s
    nearest | MR=0.1 | seed=0 | MAE=5.6541e-02 | t=0.0047s
    tikhonov | MR=0.1 | seed=0 | MAE=9.2359e-02 | t=0.0157s
    tv | MR=0.1 | seed=0 | MAE=4.1017e-02 | t=0.5272s
    trss | MR=0.1 | seed=0 | MAE=2.6438e-02 | t=0.0173s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=2.3313e-01 | t=0.0118s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=5.0661e-01 | t=2.2523s
    mean | MR=0.1 | seed=1 | MAE=4.3636e-02 | t=0.0029s
    nearest | MR=0.1 | seed=1 | MAE=5.7009e-02 | t=0.0030s
    tikhonov | MR=0.1 | seed=1 | MAE=9.3350e-02 | t=0.0098s
    tv | MR=0.1 | seed=1 | MAE=4.1426e-02 | t=0.3226s
    trss | MR=0.1 | seed=1 | MAE=2.7094e-02 | t=0.2502s

Completed: 2026-04-15T00:53:19.743365+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.