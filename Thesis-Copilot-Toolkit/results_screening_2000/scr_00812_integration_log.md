# Integration Log: scr_00812
Started: 2026-04-16T12:00:16.890154+00:00
Description: Screening scr_00812 ds=movielens_graph_signal graph=gaussian miss=1ch mode=lambda

## Dataset: movielens_graph_signal | rows=24
  Graph: gaussian__sigma0.6 built OK
    tv | MR=0.2 | seed=0 | MAE=4.3963e-02 | t=0.1855s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=9.5267e-02 | t=0.0078s
    trss | MR=0.2 | seed=0 | MAE=7.5986e-02 | t=0.0187s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.1700e-01 | t=1.2707s
    tv | MR=0.2 | seed=1 | MAE=4.2861e-02 | t=0.1851s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=9.9565e-02 | t=0.0080s
    trss | MR=0.2 | seed=1 | MAE=8.3364e-02 | t=0.0195s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.2111e-01 | t=1.3202s
    tv | MR=0.2 | seed=0 | MAE=4.4034e-02 | t=0.1893s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.1222e-01 | t=0.0080s
    trss | MR=0.2 | seed=0 | MAE=7.1425e-02 | t=0.0197s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.2440e-01 | t=1.3131s

Completed: 2026-04-16T12:00:16.891040+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.