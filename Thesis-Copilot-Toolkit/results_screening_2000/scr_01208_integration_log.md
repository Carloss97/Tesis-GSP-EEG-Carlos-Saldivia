# Integration Log: scr_01208
Started: 2026-04-16T08:20:22.726841+00:00
Description: Screening scr_01208 ds=movielens_graph_signal graph=knn miss=[0.2] mode=lambda

## Dataset: movielens_graph_signal | rows=24
  Graph: knn__k5 built OK
    tv | MR=0.2 | seed=0 | MAE=3.6355e-02 | t=0.1477s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=9.5091e-02 | t=0.0089s
    trss | MR=0.2 | seed=0 | MAE=6.3666e-02 | t=0.0187s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.2785e-01 | t=1.2755s
    tv | MR=0.2 | seed=1 | MAE=4.0311e-02 | t=0.1442s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=9.8531e-02 | t=0.0089s
    trss | MR=0.2 | seed=1 | MAE=7.2110e-02 | t=0.0195s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.2619e-01 | t=1.3381s
    tv | MR=0.2 | seed=0 | MAE=3.6440e-02 | t=0.1452s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.1541e-01 | t=0.0082s
    trss | MR=0.2 | seed=0 | MAE=6.0019e-02 | t=0.0187s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.3669e-01 | t=1.3083s

Completed: 2026-04-16T08:20:22.727560+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.