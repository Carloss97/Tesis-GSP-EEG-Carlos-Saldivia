# Integration Log: scr_00752
Started: 2026-04-16T11:52:35.896883+00:00
Description: Screening scr_00752 ds=movielens_graph_signal graph=aew miss=[0.4] mode=base

## Dataset: movielens_graph_signal | rows=14
  Graph: aew built OK
    mean | MR=0.4 | seed=0 | MAE=9.1473e-02 | t=0.0022s
    nearest | MR=0.4 | seed=0 | MAE=1.0507e-01 | t=0.0086s
    tikhonov | MR=0.4 | seed=0 | MAE=1.0287e-01 | t=0.0058s
    tv | MR=0.4 | seed=0 | MAE=9.2435e-02 | t=0.1437s
    trss | MR=0.4 | seed=0 | MAE=1.0029e-01 | t=0.0200s
    graph_time_tikhonov | MR=0.4 | seed=0 | MAE=1.2851e-01 | t=0.0082s
    temporal_laplacian | MR=0.4 | seed=0 | MAE=1.3657e-01 | t=1.3211s
    mean | MR=0.4 | seed=1 | MAE=8.7528e-02 | t=0.0020s
    nearest | MR=0.4 | seed=1 | MAE=9.3427e-02 | t=0.0087s
    tikhonov | MR=0.4 | seed=1 | MAE=9.3093e-02 | t=0.0058s
    tv | MR=0.4 | seed=1 | MAE=8.7386e-02 | t=0.1436s
    trss | MR=0.4 | seed=1 | MAE=9.1979e-02 | t=0.0204s

Completed: 2026-04-16T11:52:35.897733+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.