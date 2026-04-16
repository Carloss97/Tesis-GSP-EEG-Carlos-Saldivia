# Integration Log: scr_01232
Started: 2026-04-16T08:23:19.611326+00:00
Description: Screening scr_01232 ds=movielens_graph_signal graph=gaussian miss=[0.2] mode=lambda

## Dataset: movielens_graph_signal | rows=24
  Graph: gaussian__sigma1.0 built OK
    tv | MR=0.2 | seed=0 | MAE=3.6522e-02 | t=0.1892s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.1698e-01 | t=0.0082s
    trss | MR=0.2 | seed=0 | MAE=6.2495e-02 | t=0.0185s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.2855e-01 | t=1.2494s
    tv | MR=0.2 | seed=1 | MAE=4.0222e-02 | t=0.1868s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=1.1722e-01 | t=0.0081s
    trss | MR=0.2 | seed=1 | MAE=6.8301e-02 | t=0.0279s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.2569e-01 | t=1.3120s
    tv | MR=0.2 | seed=0 | MAE=3.6526e-02 | t=0.1862s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.4254e-01 | t=0.0089s
    trss | MR=0.2 | seed=0 | MAE=5.9131e-02 | t=0.0180s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.3863e-01 | t=1.2869s

Completed: 2026-04-16T08:23:19.612227+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.