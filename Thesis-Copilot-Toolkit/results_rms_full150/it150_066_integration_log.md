# Integration Log: it150_066
Started: 2026-04-15T00:34:33.585220+00:00
Description: Bulk normalized run it150_066 dataset=iv100hz_mat graph=knng miss=[0.1] mode=base

## Dataset: iv100hz_mat | rows=42
  Graph: knng built OK
    mean | MR=0.1 | seed=0 | MAE=8.1185e-03 | t=0.0024s
    nearest | MR=0.1 | seed=0 | MAE=1.2947e-02 | t=0.0035s
    tikhonov | MR=0.1 | seed=0 | MAE=3.3684e-02 | t=0.0079s
    tv | MR=0.1 | seed=0 | MAE=5.7140e-03 | t=0.1908s
    trss | MR=0.1 | seed=0 | MAE=5.7406e-03 | t=0.0198s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=6.5629e-02 | t=0.0112s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=7.9960e-02 | t=2.2021s
    mean | MR=0.1 | seed=1 | MAE=8.3274e-03 | t=0.0022s
    nearest | MR=0.1 | seed=1 | MAE=1.3348e-02 | t=0.0034s
    tikhonov | MR=0.1 | seed=1 | MAE=3.4015e-02 | t=0.0072s
    tv | MR=0.1 | seed=1 | MAE=6.3765e-03 | t=0.2074s
    trss | MR=0.1 | seed=1 | MAE=6.1068e-03 | t=0.0188s

Completed: 2026-04-15T00:34:33.586559+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.