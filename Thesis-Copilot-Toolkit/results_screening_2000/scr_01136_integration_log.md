# Integration Log: scr_01136
Started: 2026-04-16T14:16:57.872293+00:00
Description: Screening scr_01136 ds=movielens_graph_signal graph=gaussian miss=[0.1] mode=lambda

## Dataset: movielens_graph_signal | rows=24
  Graph: gaussian__sigma0.6 built OK
    tv | MR=0.2 | seed=0 | MAE=4.3963e-02 | t=1.1385s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=9.5267e-02 | t=0.1245s
    trss | MR=0.2 | seed=0 | MAE=7.5986e-02 | t=0.1697s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.1700e-01 | t=14.5343s
    tv | MR=0.2 | seed=1 | MAE=4.2861e-02 | t=0.1958s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=9.9565e-02 | t=0.0079s
    trss | MR=0.2 | seed=1 | MAE=8.3364e-02 | t=0.0204s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.2111e-01 | t=29.4063s
    tv | MR=0.2 | seed=0 | MAE=4.4034e-02 | t=0.8339s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.1222e-01 | t=0.0364s
    trss | MR=0.2 | seed=0 | MAE=7.1425e-02 | t=0.7813s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.2440e-01 | t=6.1705s

Completed: 2026-04-16T14:16:57.873268+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.