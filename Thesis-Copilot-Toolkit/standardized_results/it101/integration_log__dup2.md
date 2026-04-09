# Integration Log: it101_real_data_validation
Started: 2026-04-09T07:18:35.495672+00:00
Description: Real-data validation using available downloaded datasets

## Dataset: physionet_eegmmidb_real | rows=105
  Graph: knn__k3 built OK
    mean | MR=0.1 | seed=0 | MAE=2.0892e-06 | t=0.0030s
    nearest | MR=0.1 | seed=0 | MAE=2.3639e-06 | t=0.0042s
    tikhonov | MR=0.1 | seed=0 | MAE=6.2867e-06 | t=0.0101s
    tv | MR=0.1 | seed=0 | MAE=2.0441e-06 | t=0.3119s
    trss | MR=0.1 | seed=0 | MAE=1.3130e-06 | t=0.0259s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=1.2560e-05 | t=0.0153s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=2.4364e-05 | t=5.1928s
    mean | MR=0.1 | seed=1 | MAE=2.0496e-06 | t=0.0029s
    nearest | MR=0.1 | seed=1 | MAE=2.3187e-06 | t=0.0042s
    tikhonov | MR=0.1 | seed=1 | MAE=6.2676e-06 | t=0.0115s
    tv | MR=0.1 | seed=1 | MAE=2.0113e-06 | t=0.2791s
    trss | MR=0.1 | seed=1 | MAE=1.3151e-06 | t=0.0285s

Completed: 2026-04-09T07:18:35.496561+00:00
Total rows: 105
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.