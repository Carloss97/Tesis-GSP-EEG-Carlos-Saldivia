# Integration Log: it150_078
Started: 2026-04-15T00:36:36.814656+00:00
Description: Bulk normalized run it150_078 dataset=iv100hz_mat graph=vknng miss=[0.1] mode=base

## Dataset: iv100hz_mat | rows=42
  Graph: vknng built OK
    mean | MR=0.1 | seed=0 | MAE=8.1185e-03 | t=0.0023s
    nearest | MR=0.1 | seed=0 | MAE=1.2947e-02 | t=0.0036s
    tikhonov | MR=0.1 | seed=0 | MAE=3.4738e-02 | t=0.0068s
    tv | MR=0.1 | seed=0 | MAE=5.8910e-03 | t=0.1792s
    trss | MR=0.1 | seed=0 | MAE=5.6581e-03 | t=0.0191s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=6.6778e-02 | t=0.0103s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=8.0973e-02 | t=1.7617s
    mean | MR=0.1 | seed=1 | MAE=8.3274e-03 | t=0.0023s
    nearest | MR=0.1 | seed=1 | MAE=1.3348e-02 | t=0.0030s
    tikhonov | MR=0.1 | seed=1 | MAE=3.5053e-02 | t=0.0076s
    tv | MR=0.1 | seed=1 | MAE=6.5774e-03 | t=0.1822s
    trss | MR=0.1 | seed=1 | MAE=6.0150e-03 | t=0.0183s

Completed: 2026-04-15T00:36:36.815866+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.