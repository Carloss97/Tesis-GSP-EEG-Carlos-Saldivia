# Integration Log: scr_00434
Started: 2026-04-16T13:28:47.673856+00:00
Description: Screening scr_00434 ds=physionet_real graph=knn miss=[0.2] mode=base

## Dataset: physionet_eegmmidb_real | rows=14
  Graph: knn__k3 built OK
    mean | MR=0.2 | seed=0 | MAE=5.2059e-06 | t=0.0020s
    nearest | MR=0.2 | seed=0 | MAE=5.7680e-06 | t=0.0052s
    tikhonov | MR=0.2 | seed=0 | MAE=6.0818e-06 | t=0.0057s
    tv | MR=0.2 | seed=0 | MAE=5.0859e-06 | t=0.1539s
    trss | MR=0.2 | seed=0 | MAE=2.5500e-06 | t=0.0175s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.1035e-05 | t=0.0079s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.9366e-05 | t=15.2548s
    mean | MR=0.2 | seed=1 | MAE=5.2168e-06 | t=0.0050s
    nearest | MR=0.2 | seed=1 | MAE=5.8832e-06 | t=0.0094s
    tikhonov | MR=0.2 | seed=1 | MAE=5.9710e-06 | t=0.0062s
    tv | MR=0.2 | seed=1 | MAE=5.0972e-06 | t=0.1572s
    trss | MR=0.2 | seed=1 | MAE=2.4639e-06 | t=0.0171s

Completed: 2026-04-16T13:28:47.674582+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.