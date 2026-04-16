# Integration Log: it150_042
Started: 2026-04-15T00:29:53.784494+00:00
Description: Bulk normalized run it150_042 dataset=iv100hz_mat graph=gaussian miss=[0.1] mode=base

## Dataset: iv100hz_mat | rows=42
  Graph: gaussian__sigma0.6 built OK
    mean | MR=0.1 | seed=0 | MAE=8.1185e-03 | t=0.0023s
    nearest | MR=0.1 | seed=0 | MAE=1.2947e-02 | t=0.0028s
    tikhonov | MR=0.1 | seed=0 | MAE=4.1290e-02 | t=0.0068s
    tv | MR=0.1 | seed=0 | MAE=5.1550e-03 | t=0.2116s
    trss | MR=0.1 | seed=0 | MAE=5.9025e-03 | t=0.0181s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=7.4034e-02 | t=0.0089s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=9.0074e-02 | t=1.4707s
    mean | MR=0.1 | seed=1 | MAE=8.3274e-03 | t=0.0020s
    nearest | MR=0.1 | seed=1 | MAE=1.3348e-02 | t=0.0037s
    tikhonov | MR=0.1 | seed=1 | MAE=4.1503e-02 | t=0.0063s
    tv | MR=0.1 | seed=1 | MAE=5.4554e-03 | t=0.2006s
    trss | MR=0.1 | seed=1 | MAE=6.1331e-03 | t=0.0181s

Completed: 2026-04-15T00:29:53.785566+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.