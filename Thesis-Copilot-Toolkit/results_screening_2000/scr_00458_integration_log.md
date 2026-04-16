# Integration Log: scr_00458
Started: 2026-04-16T13:36:58.946229+00:00
Description: Screening scr_00458 ds=physionet_real graph=knn miss=[0.2] mode=base

## Dataset: physionet_eegmmidb_real | rows=14
  Graph: knn__k7 built OK
    mean | MR=0.2 | seed=0 | MAE=5.2059e-06 | t=0.0030s
    nearest | MR=0.2 | seed=0 | MAE=5.7680e-06 | t=0.0084s
    tikhonov | MR=0.2 | seed=0 | MAE=9.6854e-06 | t=0.0087s
    tv | MR=0.2 | seed=0 | MAE=5.1933e-06 | t=0.6073s
    trss | MR=0.2 | seed=0 | MAE=2.7316e-06 | t=0.1196s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.6790e-05 | t=0.0492s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=3.5127e-05 | t=11.0008s
    mean | MR=0.2 | seed=1 | MAE=5.2168e-06 | t=0.0037s
    nearest | MR=0.2 | seed=1 | MAE=5.8832e-06 | t=0.0087s
    tikhonov | MR=0.2 | seed=1 | MAE=9.6646e-06 | t=0.0088s
    tv | MR=0.2 | seed=1 | MAE=5.2041e-06 | t=0.2657s
    trss | MR=0.2 | seed=1 | MAE=2.6982e-06 | t=0.0199s

Completed: 2026-04-16T13:36:58.947337+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.