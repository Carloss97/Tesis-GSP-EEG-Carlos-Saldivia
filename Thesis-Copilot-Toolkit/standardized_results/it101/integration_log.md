# Integration Log: it101_real_data_validation
Started: 2026-04-09T06:32:11.030043+00:00
Description: Real-data validation using available downloaded datasets

## Dataset: physionet_eegmmidb_real | rows=105
  Graph: knn__k3 built OK
    mean | MR=0.1 | seed=0 | MAE=2.0892e-06 | t=0.0020s
    nearest | MR=0.1 | seed=0 | MAE=2.3639e-06 | t=0.0029s
    tikhonov | MR=0.1 | seed=0 | MAE=6.2867e-06 | t=0.0070s
    tv | MR=0.1 | seed=0 | MAE=2.0441e-06 | t=0.1476s
    trss | MR=0.1 | seed=0 | MAE=1.3130e-06 | t=0.0195s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=1.2560e-05 | t=0.0087s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=2.4364e-05 | t=1.4669s
    mean | MR=0.1 | seed=1 | MAE=2.0496e-06 | t=0.0021s
    nearest | MR=0.1 | seed=1 | MAE=2.3187e-06 | t=0.0062s
    tikhonov | MR=0.1 | seed=1 | MAE=6.2676e-06 | t=0.0091s
    tv | MR=0.1 | seed=1 | MAE=2.0113e-06 | t=0.1461s
    trss | MR=0.1 | seed=1 | MAE=1.3151e-06 | t=0.0160s

Completed: 2026-04-09T06:32:11.030943+00:00
Total rows: 105
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.