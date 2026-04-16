# Integration Log: scr_01218
Started: 2026-04-16T08:21:36.070450+00:00
Description: Screening scr_01218 ds=iv100hz_mat graph=knn miss=[0.2] mode=lambda

## Dataset: iv100hz_mat | rows=24
  Graph: knn__k7 built OK
    tv | MR=0.2 | seed=0 | MAE=1.2426e-02 | t=0.1669s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=4.1432e-02 | t=0.0080s
    trss | MR=0.2 | seed=0 | MAE=3.7143e-03 | t=0.0190s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=6.4913e-02 | t=2.7680s
    tv | MR=0.2 | seed=1 | MAE=1.2948e-02 | t=0.1529s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=4.1615e-02 | t=0.0085s
    trss | MR=0.2 | seed=1 | MAE=3.7279e-03 | t=0.0188s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=6.4910e-02 | t=2.6503s
    tv | MR=0.2 | seed=0 | MAE=1.3051e-02 | t=0.1567s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=5.3657e-02 | t=0.0092s
    trss | MR=0.2 | seed=0 | MAE=5.2306e-03 | t=0.0182s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=7.1531e-02 | t=2.7610s

Completed: 2026-04-16T08:21:36.071150+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.