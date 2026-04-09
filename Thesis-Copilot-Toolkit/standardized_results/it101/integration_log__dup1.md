# Integration Log: it101_real_data_validation
Started: 2026-04-09T06:59:54.618670+00:00
Description: Real-data validation using available downloaded datasets

## Dataset: physionet_eegmmidb_real | rows=105
  Graph: knn__k3 built OK
    mean | MR=0.1 | seed=0 | MAE=2.0892e-06 | t=0.0020s
    nearest | MR=0.1 | seed=0 | MAE=2.3639e-06 | t=0.0026s
    tikhonov | MR=0.1 | seed=0 | MAE=6.2867e-06 | t=0.0058s
    tv | MR=0.1 | seed=0 | MAE=2.0441e-06 | t=0.2325s
    trss | MR=0.1 | seed=0 | MAE=1.3130e-06 | t=0.2488s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=1.2560e-05 | t=0.0121s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=2.4364e-05 | t=12.9241s
    mean | MR=0.1 | seed=1 | MAE=2.0496e-06 | t=0.0356s
    nearest | MR=0.1 | seed=1 | MAE=2.3187e-06 | t=0.0534s
    tikhonov | MR=0.1 | seed=1 | MAE=6.2676e-06 | t=0.0085s
    tv | MR=0.1 | seed=1 | MAE=2.0113e-06 | t=0.4064s
    trss | MR=0.1 | seed=1 | MAE=1.3151e-06 | t=0.0725s

Completed: 2026-04-09T06:59:54.619616+00:00
Total rows: 105
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.