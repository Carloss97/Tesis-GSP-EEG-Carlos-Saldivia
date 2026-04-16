# Integration Log: scr_00338
Started: 2026-04-16T15:40:53.260227+00:00
Description: Screening scr_00338 ds=physionet_real graph=knn miss=[0.1] mode=base

## Dataset: physionet_eegmmidb_real | rows=14
  Graph: knn__k5 built OK
    mean | MR=0.1 | seed=0 | MAE=2.0892e-06 | t=0.0049s
    nearest | MR=0.1 | seed=0 | MAE=2.3639e-06 | t=0.0058s
    tikhonov | MR=0.1 | seed=0 | MAE=6.1981e-06 | t=0.0094s
    tv | MR=0.1 | seed=0 | MAE=2.0760e-06 | t=0.5572s
    trss | MR=0.1 | seed=0 | MAE=9.9346e-07 | t=0.7580s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=1.3073e-05 | t=0.0126s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=3.1644e-05 | t=33.7240s
    mean | MR=0.1 | seed=1 | MAE=2.0496e-06 | t=0.0033s
    nearest | MR=0.1 | seed=1 | MAE=2.3187e-06 | t=0.0058s
    tikhonov | MR=0.1 | seed=1 | MAE=6.1834e-06 | t=0.0561s
    tv | MR=0.1 | seed=1 | MAE=2.0371e-06 | t=0.5476s
    trss | MR=0.1 | seed=1 | MAE=9.6487e-07 | t=0.0968s

Completed: 2026-04-16T15:40:53.261503+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.