# Integration Log: it150_034
Started: 2026-04-15T00:47:49.239266+00:00
Description: Bulk normalized run it150_034 dataset=synthetic_beta graph=gaussian miss=[0.1] mode=base

## Dataset: synthetic_beta | rows=14
  Graph: gaussian__sigma1.0 built OK
    mean | MR=0.1 | seed=0 | MAE=4.3607e-02 | t=0.0073s
    nearest | MR=0.1 | seed=0 | MAE=5.6541e-02 | t=0.0044s
    tikhonov | MR=0.1 | seed=0 | MAE=2.9126e-01 | t=0.0147s
    tv | MR=0.1 | seed=0 | MAE=4.2968e-02 | t=0.5127s
    trss | MR=0.1 | seed=0 | MAE=3.1082e-02 | t=0.2324s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=5.0594e-01 | t=0.0201s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=7.3147e-01 | t=2.7822s
    mean | MR=0.1 | seed=1 | MAE=4.3636e-02 | t=0.0031s
    nearest | MR=0.1 | seed=1 | MAE=5.7009e-02 | t=0.0025s
    tikhonov | MR=0.1 | seed=1 | MAE=2.9071e-01 | t=0.0080s
    tv | MR=0.1 | seed=1 | MAE=4.3066e-02 | t=0.2691s
    trss | MR=0.1 | seed=1 | MAE=3.0874e-02 | t=0.2191s

Completed: 2026-04-15T00:47:49.240159+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.