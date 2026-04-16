# Integration Log: scr_01196
Started: 2026-04-16T15:35:26.836815+00:00
Description: Screening scr_01196 ds=movielens_graph_signal graph=knn miss=[0.2] mode=lambda

## Dataset: movielens_graph_signal | rows=24
  Graph: knn__k3 built OK
    tv | MR=0.2 | seed=0 | MAE=4.3349e-02 | t=0.6235s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=8.8406e-02 | t=0.0214s
    trss | MR=0.2 | seed=0 | MAE=8.0976e-02 | t=0.1961s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.1653e-01 | t=21.4513s
    tv | MR=0.2 | seed=1 | MAE=4.3375e-02 | t=0.7103s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=9.2770e-02 | t=0.0283s
    trss | MR=0.2 | seed=1 | MAE=8.3600e-02 | t=0.2054s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.2095e-01 | t=12.8314s
    tv | MR=0.2 | seed=0 | MAE=4.3672e-02 | t=0.6393s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.0090e-01 | t=0.0375s
    trss | MR=0.2 | seed=0 | MAE=7.6456e-02 | t=0.5685s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.2361e-01 | t=14.6523s

Completed: 2026-04-16T15:35:26.838716+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.