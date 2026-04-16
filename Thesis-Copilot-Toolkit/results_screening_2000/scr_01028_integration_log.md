# Integration Log: scr_01028
Started: 2026-04-16T13:00:34.555412+00:00
Description: Screening scr_01028 ds=movielens_graph_signal graph=gaussian miss=3ch mode=lambda

## Dataset: movielens_graph_signal | rows=24
  Graph: gaussian__sigma0.6 built OK
    tv | MR=0.2 | seed=0 | MAE=4.3963e-02 | t=0.2026s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=9.5267e-02 | t=0.0121s
    trss | MR=0.2 | seed=0 | MAE=7.5986e-02 | t=0.1317s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.1700e-01 | t=2.4445s
    tv | MR=0.2 | seed=1 | MAE=4.2861e-02 | t=0.1927s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=9.9565e-02 | t=0.0081s
    trss | MR=0.2 | seed=1 | MAE=8.3364e-02 | t=0.0200s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.2111e-01 | t=7.6695s
    tv | MR=0.2 | seed=0 | MAE=4.4034e-02 | t=0.3338s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.1222e-01 | t=0.0126s
    trss | MR=0.2 | seed=0 | MAE=7.1425e-02 | t=0.5141s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.2440e-01 | t=9.8219s

Completed: 2026-04-16T13:00:34.556445+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.