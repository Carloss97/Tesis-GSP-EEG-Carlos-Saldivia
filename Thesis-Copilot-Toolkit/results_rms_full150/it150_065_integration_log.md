# Integration Log: it150_065
Started: 2026-04-15T00:34:07.962298+00:00
Description: Bulk normalized run it150_065 dataset=bci_iv2a_real_s3 graph=knng miss=[0.1] mode=base

## Dataset: bci_iv2a_real_s3 | rows=42
  Graph: knng built OK
    mean | MR=0.1 | seed=0 | MAE=3.5550e-02 | t=0.0027s
    nearest | MR=0.1 | seed=0 | MAE=2.9251e-02 | t=0.0044s
    tikhonov | MR=0.1 | seed=0 | MAE=1.6652e-01 | t=0.0101s
    tv | MR=0.1 | seed=0 | MAE=3.5554e-02 | t=0.2315s
    trss | MR=0.1 | seed=0 | MAE=3.1309e-02 | t=0.0204s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=3.0442e-01 | t=0.0108s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=6.0254e-01 | t=2.8233s
    mean | MR=0.1 | seed=1 | MAE=3.3104e-02 | t=0.0031s
    nearest | MR=0.1 | seed=1 | MAE=2.9433e-02 | t=0.0032s
    tikhonov | MR=0.1 | seed=1 | MAE=1.6425e-01 | t=0.0073s
    tv | MR=0.1 | seed=1 | MAE=3.3105e-02 | t=0.2212s
    trss | MR=0.1 | seed=1 | MAE=2.9796e-02 | t=0.0193s

Completed: 2026-04-15T00:34:07.963367+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.