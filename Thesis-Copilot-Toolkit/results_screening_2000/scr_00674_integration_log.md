# Integration Log: scr_00674
Started: 2026-04-16T15:12:02.882720+00:00
Description: Screening scr_00674 ds=physionet_real graph=knn miss=[0.4] mode=base

## Dataset: physionet_eegmmidb_real | rows=14
  Graph: knn__k7 built OK
    mean | MR=0.4 | seed=0 | MAE=1.0497e-05 | t=0.0031s
    nearest | MR=0.4 | seed=0 | MAE=1.1571e-05 | t=0.0506s
    tikhonov | MR=0.4 | seed=0 | MAE=1.2511e-05 | t=0.0099s
    tv | MR=0.4 | seed=0 | MAE=1.0479e-05 | t=0.3505s
    trss | MR=0.4 | seed=0 | MAE=6.2082e-06 | t=0.0475s
    graph_time_tikhonov | MR=0.4 | seed=0 | MAE=1.8415e-05 | t=0.0134s
    temporal_laplacian | MR=0.4 | seed=0 | MAE=3.6902e-05 | t=27.2873s
    mean | MR=0.4 | seed=1 | MAE=1.0467e-05 | t=0.0036s
    nearest | MR=0.4 | seed=1 | MAE=1.1385e-05 | t=0.0137s
    tikhonov | MR=0.4 | seed=1 | MAE=1.2472e-05 | t=0.0097s
    tv | MR=0.4 | seed=1 | MAE=1.0448e-05 | t=0.5544s
    trss | MR=0.4 | seed=1 | MAE=6.0637e-06 | t=0.2452s

Completed: 2026-04-16T15:12:02.883789+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.