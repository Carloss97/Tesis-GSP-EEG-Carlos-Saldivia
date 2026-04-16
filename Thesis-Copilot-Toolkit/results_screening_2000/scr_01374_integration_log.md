# Integration Log: scr_01374
Started: 2026-04-16T08:41:00.791194+00:00
Description: Screening scr_01374 ds=iv100hz_mat graph=knng miss=[0.3] mode=lambda

## Dataset: iv100hz_mat | rows=24
  Graph: knng built OK
    tv | MR=0.2 | seed=0 | MAE=1.4059e-02 | t=0.1451s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=3.1896e-02 | t=0.0080s
    trss | MR=0.2 | seed=0 | MAE=3.6038e-03 | t=0.0199s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=6.2414e-02 | t=2.6333s
    tv | MR=0.2 | seed=1 | MAE=1.2798e-02 | t=0.1433s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=3.2007e-02 | t=0.0081s
    trss | MR=0.2 | seed=1 | MAE=3.6282e-03 | t=0.0197s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=6.2380e-02 | t=1.3372s
    tv | MR=0.2 | seed=0 | MAE=1.4486e-02 | t=0.1412s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=4.0759e-02 | t=0.0092s
    trss | MR=0.2 | seed=0 | MAE=5.1729e-03 | t=0.0198s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=6.5910e-02 | t=1.3192s

Completed: 2026-04-16T08:41:00.792038+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.