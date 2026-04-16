# Integration Log: scr_01424
Started: 2026-04-16T08:47:18.600213+00:00
Description: Screening scr_01424 ds=movielens_graph_signal graph=knn miss=[0.4] mode=lambda

## Dataset: movielens_graph_signal | rows=24
  Graph: knn__k5 built OK
    tv | MR=0.2 | seed=0 | MAE=3.6355e-02 | t=0.1735s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=9.5091e-02 | t=0.0080s
    trss | MR=0.2 | seed=0 | MAE=6.3666e-02 | t=0.0194s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.2785e-01 | t=1.2893s
    tv | MR=0.2 | seed=1 | MAE=4.0311e-02 | t=0.1446s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=9.8531e-02 | t=0.0085s
    trss | MR=0.2 | seed=1 | MAE=7.2110e-02 | t=0.0195s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.2619e-01 | t=1.3070s
    tv | MR=0.2 | seed=0 | MAE=3.6440e-02 | t=0.1457s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.1541e-01 | t=0.0080s
    trss | MR=0.2 | seed=0 | MAE=6.0019e-02 | t=0.0195s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.3669e-01 | t=2.1130s

Completed: 2026-04-16T08:47:18.600901+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.