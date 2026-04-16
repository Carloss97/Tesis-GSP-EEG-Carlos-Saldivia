# Integration Log: scr_01310
Started: 2026-04-16T08:32:31.921789+00:00
Description: Screening scr_01310 ds=physionet_real graph=knn miss=[0.3] mode=lambda

## Dataset: physionet_eegmmidb_real | rows=24
  Graph: knn__k5 built OK
    tv | MR=0.2 | seed=0 | MAE=7.6400e-02 | t=0.1461s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.1730e-01 | t=0.0081s
    trss | MR=0.2 | seed=0 | MAE=2.8596e-02 | t=0.0230s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=3.1174e-01 | t=1.3079s
    tv | MR=0.2 | seed=1 | MAE=7.5692e-02 | t=0.1468s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=1.1665e-01 | t=0.0081s
    trss | MR=0.2 | seed=1 | MAE=2.7727e-02 | t=0.0185s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=3.1226e-01 | t=1.3610s
    tv | MR=0.2 | seed=0 | MAE=7.7188e-02 | t=0.1464s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.4825e-01 | t=0.0081s
    trss | MR=0.2 | seed=0 | MAE=2.9356e-02 | t=0.0191s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=3.9584e-01 | t=1.2460s

Completed: 2026-04-16T08:32:31.922496+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.