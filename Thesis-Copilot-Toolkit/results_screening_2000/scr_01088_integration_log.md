# Integration Log: scr_01088
Started: 2026-04-16T13:35:54.402211+00:00
Description: Screening scr_01088 ds=movielens_graph_signal graph=knn miss=[0.1] mode=lambda

## Dataset: movielens_graph_signal | rows=24
  Graph: knn__k3 built OK
    tv | MR=0.2 | seed=0 | MAE=4.3349e-02 | t=0.4026s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=8.8406e-02 | t=0.0190s
    trss | MR=0.2 | seed=0 | MAE=8.0976e-02 | t=0.1010s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.1653e-01 | t=8.9026s
    tv | MR=0.2 | seed=1 | MAE=4.3375e-02 | t=0.7605s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=9.2770e-02 | t=0.0134s
    trss | MR=0.2 | seed=1 | MAE=8.3600e-02 | t=0.4476s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.2095e-01 | t=4.2609s
    tv | MR=0.2 | seed=0 | MAE=4.3672e-02 | t=0.1479s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.0090e-01 | t=0.0080s
    trss | MR=0.2 | seed=0 | MAE=7.6456e-02 | t=0.0188s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.2361e-01 | t=24.8858s

Completed: 2026-04-16T13:35:54.403077+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.