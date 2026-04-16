# Integration Log: scr_00374
Started: 2026-04-16T13:10:17.670404+00:00
Description: Screening scr_00374 ds=physionet_real graph=gaussian miss=[0.1] mode=base

## Dataset: physionet_eegmmidb_real | rows=14
  Graph: gaussian__sigma0.6 built OK
    mean | MR=0.1 | seed=0 | MAE=2.0892e-06 | t=0.0020s
    nearest | MR=0.1 | seed=0 | MAE=2.3639e-06 | t=0.0038s
    tikhonov | MR=0.1 | seed=0 | MAE=1.7107e-05 | t=0.0057s
    tv | MR=0.1 | seed=0 | MAE=2.0892e-06 | t=0.1893s
    trss | MR=0.1 | seed=0 | MAE=1.5039e-06 | t=0.0170s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=2.1933e-05 | t=0.0079s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=3.8732e-05 | t=6.0677s
    mean | MR=0.1 | seed=1 | MAE=2.0496e-06 | t=0.0020s
    nearest | MR=0.1 | seed=1 | MAE=2.3187e-06 | t=0.0027s
    tikhonov | MR=0.1 | seed=1 | MAE=1.7122e-05 | t=0.0057s
    tv | MR=0.1 | seed=1 | MAE=2.0495e-06 | t=0.2012s
    trss | MR=0.1 | seed=1 | MAE=1.4767e-06 | t=0.0185s

Completed: 2026-04-16T13:10:17.671171+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.