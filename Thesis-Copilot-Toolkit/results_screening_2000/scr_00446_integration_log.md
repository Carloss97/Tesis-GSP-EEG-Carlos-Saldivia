# Integration Log: scr_00446
Started: 2026-04-16T13:33:05.388044+00:00
Description: Screening scr_00446 ds=physionet_real graph=knn miss=[0.2] mode=base

## Dataset: physionet_eegmmidb_real | rows=14
  Graph: knn__k5 built OK
    mean | MR=0.2 | seed=0 | MAE=5.2059e-06 | t=0.0036s
    nearest | MR=0.2 | seed=0 | MAE=5.7680e-06 | t=0.0050s
    tikhonov | MR=0.2 | seed=0 | MAE=7.6971e-06 | t=0.0057s
    tv | MR=0.2 | seed=0 | MAE=5.1792e-06 | t=0.1679s
    trss | MR=0.2 | seed=0 | MAE=2.6057e-06 | t=0.0186s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.4098e-05 | t=0.0079s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=3.2916e-05 | t=22.2119s
    mean | MR=0.2 | seed=1 | MAE=5.2168e-06 | t=0.0039s
    nearest | MR=0.2 | seed=1 | MAE=5.8832e-06 | t=0.0050s
    tikhonov | MR=0.2 | seed=1 | MAE=7.6181e-06 | t=0.0070s
    tv | MR=0.2 | seed=1 | MAE=5.1896e-06 | t=0.1638s
    trss | MR=0.2 | seed=1 | MAE=2.5281e-06 | t=0.0184s

Completed: 2026-04-16T13:33:05.388883+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.