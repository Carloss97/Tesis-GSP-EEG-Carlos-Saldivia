# Integration Log: it150_030
Started: 2026-04-15T00:27:48.787356+00:00
Description: Bulk normalized run it150_030 dataset=iv100hz_mat graph=gaussian miss=[0.1] mode=base

## Dataset: iv100hz_mat | rows=42
  Graph: gaussian__sigma1.0 built OK
    mean | MR=0.1 | seed=0 | MAE=8.1185e-03 | t=0.0032s
    nearest | MR=0.1 | seed=0 | MAE=1.2947e-02 | t=0.0034s
    tikhonov | MR=0.1 | seed=0 | MAE=5.4709e-02 | t=0.0074s
    tv | MR=0.1 | seed=0 | MAE=4.9860e-03 | t=0.2506s
    trss | MR=0.1 | seed=0 | MAE=5.5783e-03 | t=0.0184s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=8.3456e-02 | t=0.0083s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=1.0611e-01 | t=2.1660s
    mean | MR=0.1 | seed=1 | MAE=8.3274e-03 | t=0.0030s
    nearest | MR=0.1 | seed=1 | MAE=1.3348e-02 | t=0.0050s
    tikhonov | MR=0.1 | seed=1 | MAE=5.4832e-02 | t=0.0079s
    tv | MR=0.1 | seed=1 | MAE=5.4138e-03 | t=0.2444s
    trss | MR=0.1 | seed=1 | MAE=5.7586e-03 | t=0.0190s

Completed: 2026-04-15T00:27:48.788316+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.