# Integration Log: scr_01280
Started: 2026-04-16T08:29:21.176334+00:00
Description: Screening scr_01280 ds=movielens_graph_signal graph=vknng miss=[0.2] mode=lambda

## Dataset: movielens_graph_signal | rows=24
  Graph: vknng built OK
    tv | MR=0.2 | seed=0 | MAE=3.6198e-02 | t=0.1425s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=8.7391e-02 | t=0.0081s
    trss | MR=0.2 | seed=0 | MAE=6.2012e-02 | t=0.0187s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.2582e-01 | t=1.3028s
    tv | MR=0.2 | seed=1 | MAE=4.0343e-02 | t=0.1427s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=9.3729e-02 | t=0.0081s
    trss | MR=0.2 | seed=1 | MAE=7.3845e-02 | t=0.0190s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.2500e-01 | t=1.3814s
    tv | MR=0.2 | seed=0 | MAE=3.6353e-02 | t=0.1435s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.0518e-01 | t=0.0084s
    trss | MR=0.2 | seed=0 | MAE=5.8520e-02 | t=0.0186s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.3379e-01 | t=1.9184s

Completed: 2026-04-16T08:29:21.177184+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.