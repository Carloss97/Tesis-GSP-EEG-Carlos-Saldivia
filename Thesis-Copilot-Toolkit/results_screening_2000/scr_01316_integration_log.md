# Integration Log: scr_01316
Started: 2026-04-16T08:33:49.765839+00:00
Description: Screening scr_01316 ds=movielens_graph_signal graph=knn miss=[0.3] mode=lambda

## Dataset: movielens_graph_signal | rows=24
  Graph: knn__k5 built OK
    tv | MR=0.2 | seed=0 | MAE=3.6355e-02 | t=0.1646s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=9.5091e-02 | t=0.0082s
    trss | MR=0.2 | seed=0 | MAE=6.3666e-02 | t=0.0190s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.2785e-01 | t=2.5808s
    tv | MR=0.2 | seed=1 | MAE=4.0311e-02 | t=0.1769s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=9.8531e-02 | t=0.0082s
    trss | MR=0.2 | seed=1 | MAE=7.2110e-02 | t=0.0201s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.2619e-01 | t=2.6792s
    tv | MR=0.2 | seed=0 | MAE=3.6440e-02 | t=0.1459s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.1541e-01 | t=0.0081s
    trss | MR=0.2 | seed=0 | MAE=6.0019e-02 | t=0.0187s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.3669e-01 | t=1.3613s

Completed: 2026-04-16T08:33:49.766712+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.