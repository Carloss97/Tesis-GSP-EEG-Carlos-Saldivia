# Integration Log: it150_090
Started: 2026-04-15T00:38:38.489396+00:00
Description: Bulk normalized run it150_090 dataset=iv100hz_mat graph=aew miss=[0.1] mode=base

## Dataset: iv100hz_mat | rows=42
  Graph: aew built OK
    mean | MR=0.1 | seed=0 | MAE=8.1185e-03 | t=0.0025s
    nearest | MR=0.1 | seed=0 | MAE=1.2947e-02 | t=0.0035s
    tikhonov | MR=0.1 | seed=0 | MAE=3.0183e-02 | t=0.0073s
    tv | MR=0.1 | seed=0 | MAE=5.7738e-03 | t=0.1911s
    trss | MR=0.1 | seed=0 | MAE=5.6551e-03 | t=0.0196s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=6.1035e-02 | t=0.0102s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=7.5602e-02 | t=1.6990s
    mean | MR=0.1 | seed=1 | MAE=8.3274e-03 | t=0.0024s
    nearest | MR=0.1 | seed=1 | MAE=1.3348e-02 | t=0.0034s
    tikhonov | MR=0.1 | seed=1 | MAE=3.0581e-02 | t=0.0069s
    tv | MR=0.1 | seed=1 | MAE=6.1379e-03 | t=0.1810s
    trss | MR=0.1 | seed=1 | MAE=6.0666e-03 | t=0.0183s

Completed: 2026-04-15T00:38:38.490214+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.