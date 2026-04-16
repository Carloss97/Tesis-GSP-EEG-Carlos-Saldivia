# Integration Log: scr_01418
Started: 2026-04-16T08:46:02.004114+00:00
Description: Screening scr_01418 ds=physionet_real graph=knn miss=[0.4] mode=lambda

## Dataset: physionet_eegmmidb_real | rows=24
  Graph: knn__k5 built OK
    tv | MR=0.2 | seed=0 | MAE=7.6400e-02 | t=0.1498s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.1730e-01 | t=0.0083s
    trss | MR=0.2 | seed=0 | MAE=2.8596e-02 | t=0.0191s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=3.1174e-01 | t=2.6727s
    tv | MR=0.2 | seed=1 | MAE=7.5692e-02 | t=0.1454s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=1.1665e-01 | t=0.0090s
    trss | MR=0.2 | seed=1 | MAE=2.7727e-02 | t=0.0191s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=3.1226e-01 | t=2.6525s
    tv | MR=0.2 | seed=0 | MAE=7.7188e-02 | t=0.1465s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.4825e-01 | t=0.0081s
    trss | MR=0.2 | seed=0 | MAE=2.9356e-02 | t=0.0194s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=3.9584e-01 | t=1.3715s

Completed: 2026-04-16T08:46:02.004982+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.