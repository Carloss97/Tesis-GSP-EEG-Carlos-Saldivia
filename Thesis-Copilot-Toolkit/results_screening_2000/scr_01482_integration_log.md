# Integration Log: scr_01482
Started: 2026-04-16T08:54:37.161757+00:00
Description: Screening scr_01482 ds=iv100hz_mat graph=knng miss=[0.4] mode=lambda

## Dataset: iv100hz_mat | rows=24
  Graph: knng built OK
    tv | MR=0.2 | seed=0 | MAE=1.4059e-02 | t=0.1407s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=3.1896e-02 | t=0.0080s
    trss | MR=0.2 | seed=0 | MAE=3.6038e-03 | t=0.0210s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=6.2414e-02 | t=2.9849s
    tv | MR=0.2 | seed=1 | MAE=1.2798e-02 | t=0.1453s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=3.2007e-02 | t=0.0080s
    trss | MR=0.2 | seed=1 | MAE=3.6282e-03 | t=0.0204s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=6.2380e-02 | t=2.7467s
    tv | MR=0.2 | seed=0 | MAE=1.4486e-02 | t=0.1427s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=4.0759e-02 | t=0.0092s
    trss | MR=0.2 | seed=0 | MAE=5.1729e-03 | t=0.0192s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=6.5910e-02 | t=2.5156s

Completed: 2026-04-16T08:54:37.162617+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.