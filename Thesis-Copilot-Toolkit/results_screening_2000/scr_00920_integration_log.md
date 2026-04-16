# Integration Log: scr_00920
Started: 2026-04-16T12:21:27.569434+00:00
Description: Screening scr_00920 ds=movielens_graph_signal graph=gaussian miss=2ch mode=lambda

## Dataset: movielens_graph_signal | rows=24
  Graph: gaussian__sigma0.6 built OK
    tv | MR=0.2 | seed=0 | MAE=4.3963e-02 | t=0.3840s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=9.5267e-02 | t=0.0177s
    trss | MR=0.2 | seed=0 | MAE=7.5986e-02 | t=0.0525s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.1700e-01 | t=7.3827s
    tv | MR=0.2 | seed=1 | MAE=4.2861e-02 | t=0.1932s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=9.9565e-02 | t=0.0079s
    trss | MR=0.2 | seed=1 | MAE=8.3364e-02 | t=0.0189s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.2111e-01 | t=7.8711s
    tv | MR=0.2 | seed=0 | MAE=4.4034e-02 | t=0.1981s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.1222e-01 | t=0.0084s
    trss | MR=0.2 | seed=0 | MAE=7.1425e-02 | t=0.0186s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.2440e-01 | t=5.4182s

Completed: 2026-04-16T12:21:27.570289+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.