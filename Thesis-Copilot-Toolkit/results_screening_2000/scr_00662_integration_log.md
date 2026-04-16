# Integration Log: scr_00662
Started: 2026-04-16T15:06:05.577082+00:00
Description: Screening scr_00662 ds=physionet_real graph=knn miss=[0.4] mode=base

## Dataset: physionet_eegmmidb_real | rows=14
  Graph: knn__k5 built OK
    mean | MR=0.4 | seed=0 | MAE=1.0497e-05 | t=0.0300s
    nearest | MR=0.4 | seed=0 | MAE=1.1571e-05 | t=0.0394s
    tikhonov | MR=0.4 | seed=0 | MAE=1.0542e-05 | t=0.0089s
    tv | MR=0.4 | seed=0 | MAE=1.0458e-05 | t=0.3966s
    trss | MR=0.4 | seed=0 | MAE=5.8260e-06 | t=0.0292s
    graph_time_tikhonov | MR=0.4 | seed=0 | MAE=1.6033e-05 | t=0.0083s
    temporal_laplacian | MR=0.4 | seed=0 | MAE=3.5228e-05 | t=17.4003s
    mean | MR=0.4 | seed=1 | MAE=1.0467e-05 | t=0.0375s
    nearest | MR=0.4 | seed=1 | MAE=1.1385e-05 | t=0.0145s
    tikhonov | MR=0.4 | seed=1 | MAE=1.0483e-05 | t=0.0088s
    tv | MR=0.4 | seed=1 | MAE=1.0427e-05 | t=0.5536s
    trss | MR=0.4 | seed=1 | MAE=5.6762e-06 | t=0.7079s

Completed: 2026-04-16T15:06:05.577953+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.