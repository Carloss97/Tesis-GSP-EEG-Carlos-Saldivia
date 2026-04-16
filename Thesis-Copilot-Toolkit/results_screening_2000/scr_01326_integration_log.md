# Integration Log: scr_01326
Started: 2026-04-16T08:35:00.670637+00:00
Description: Screening scr_01326 ds=iv100hz_mat graph=knn miss=[0.3] mode=lambda

## Dataset: iv100hz_mat | rows=24
  Graph: knn__k7 built OK
    tv | MR=0.2 | seed=0 | MAE=1.2426e-02 | t=0.1501s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=4.1432e-02 | t=0.0080s
    trss | MR=0.2 | seed=0 | MAE=3.7143e-03 | t=0.0185s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=6.4913e-02 | t=1.6647s
    tv | MR=0.2 | seed=1 | MAE=1.2948e-02 | t=0.1711s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=4.1615e-02 | t=0.0082s
    trss | MR=0.2 | seed=1 | MAE=3.7279e-03 | t=0.0190s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=6.4910e-02 | t=1.3966s
    tv | MR=0.2 | seed=0 | MAE=1.3051e-02 | t=0.1497s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=5.3657e-02 | t=0.0081s
    trss | MR=0.2 | seed=0 | MAE=5.2306e-03 | t=0.0188s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=7.1531e-02 | t=1.2652s

Completed: 2026-04-16T08:35:00.671412+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.