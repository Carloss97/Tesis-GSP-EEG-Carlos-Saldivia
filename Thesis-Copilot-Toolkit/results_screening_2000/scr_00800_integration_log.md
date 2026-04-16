# Integration Log: scr_00800
Started: 2026-04-16T11:58:43.246948+00:00
Description: Screening scr_00800 ds=movielens_graph_signal graph=gaussian miss=1ch mode=lambda

## Dataset: movielens_graph_signal | rows=24
  Graph: gaussian__sigma1.0 built OK
    tv | MR=0.2 | seed=0 | MAE=4.4089e-02 | t=0.1966s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.1401e-01 | t=0.0081s
    trss | MR=0.2 | seed=0 | MAE=7.5416e-02 | t=0.0192s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.2054e-01 | t=1.2873s
    tv | MR=0.2 | seed=1 | MAE=4.2790e-02 | t=0.1870s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=1.1568e-01 | t=0.0078s
    trss | MR=0.2 | seed=1 | MAE=8.1860e-02 | t=0.0193s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.2314e-01 | t=1.3779s
    tv | MR=0.2 | seed=0 | MAE=4.4098e-02 | t=0.1844s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.3553e-01 | t=0.0080s
    trss | MR=0.2 | seed=0 | MAE=7.0991e-02 | t=0.0192s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.3020e-01 | t=1.2377s

Completed: 2026-04-16T11:58:43.247809+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.