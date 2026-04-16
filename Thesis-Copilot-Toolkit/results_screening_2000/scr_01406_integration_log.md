# Integration Log: scr_01406
Started: 2026-04-16T08:44:33.232705+00:00
Description: Screening scr_01406 ds=physionet_real graph=knn miss=[0.4] mode=lambda

## Dataset: physionet_eegmmidb_real | rows=24
  Graph: knn__k3 built OK
    tv | MR=0.2 | seed=0 | MAE=7.2169e-02 | t=0.1488s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.0060e-01 | t=0.0079s
    trss | MR=0.2 | seed=0 | MAE=2.9443e-02 | t=0.0199s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.7492e-01 | t=2.3507s
    tv | MR=0.2 | seed=1 | MAE=7.1211e-02 | t=0.1544s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=1.0060e-01 | t=0.0090s
    trss | MR=0.2 | seed=1 | MAE=2.8577e-02 | t=0.0199s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=2.7513e-01 | t=2.8651s
    tv | MR=0.2 | seed=0 | MAE=7.4659e-02 | t=0.1472s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.2108e-01 | t=0.0080s
    trss | MR=0.2 | seed=0 | MAE=2.9805e-02 | t=0.0189s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=3.3742e-01 | t=2.4587s

Completed: 2026-04-16T08:44:33.233717+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.