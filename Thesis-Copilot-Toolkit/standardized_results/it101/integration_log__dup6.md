# Integration Log: it101_real_data_validation
Started: 2026-04-09T15:25:01.137372+00:00
Description: Real-data validation using available downloaded datasets

## Dataset: physionet_eegmmidb_real | rows=105
  Graph: knn__k3 built OK
    mean | MR=0.1 | seed=0 | MAE=2.0892e-06 | t=0.0020s
    nearest | MR=0.1 | seed=0 | MAE=2.3639e-06 | t=0.0031s
    tikhonov | MR=0.1 | seed=0 | MAE=6.2867e-06 | t=0.0064s
    tv | MR=0.1 | seed=0 | MAE=2.0441e-06 | t=0.1520s
    trss | MR=0.1 | seed=0 | MAE=1.3130e-06 | t=0.0180s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=1.2560e-05 | t=0.0083s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=2.4364e-05 | t=2.1399s
    mean | MR=0.1 | seed=1 | MAE=2.0496e-06 | t=0.0020s
    nearest | MR=0.1 | seed=1 | MAE=2.3187e-06 | t=0.0030s
    tikhonov | MR=0.1 | seed=1 | MAE=6.2676e-06 | t=0.0061s
    tv | MR=0.1 | seed=1 | MAE=2.0113e-06 | t=0.1538s
    trss | MR=0.1 | seed=1 | MAE=1.3151e-06 | t=0.0175s

Completed: 2026-04-09T15:25:01.138289+00:00
Total rows: 105
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.