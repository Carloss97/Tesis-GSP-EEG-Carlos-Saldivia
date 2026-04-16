# Integration Log: scr_00326
Started: 2026-04-16T15:33:54.194021+00:00
Description: Screening scr_00326 ds=physionet_real graph=knn miss=[0.1] mode=base

## Dataset: physionet_eegmmidb_real | rows=14
  Graph: knn__k3 built OK
    mean | MR=0.1 | seed=0 | MAE=2.0892e-06 | t=0.0037s
    nearest | MR=0.1 | seed=0 | MAE=2.3639e-06 | t=0.0093s
    tikhonov | MR=0.1 | seed=0 | MAE=4.5685e-06 | t=0.0102s
    tv | MR=0.1 | seed=0 | MAE=2.0331e-06 | t=0.5510s
    trss | MR=0.1 | seed=0 | MAE=9.7034e-07 | t=0.2678s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=1.0050e-05 | t=0.0396s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=2.7778e-05 | t=3.9890s
    mean | MR=0.1 | seed=1 | MAE=2.0496e-06 | t=0.0031s
    nearest | MR=0.1 | seed=1 | MAE=2.3187e-06 | t=0.0211s
    tikhonov | MR=0.1 | seed=1 | MAE=4.5474e-06 | t=0.0290s
    tv | MR=0.1 | seed=1 | MAE=1.9934e-06 | t=0.5713s
    trss | MR=0.1 | seed=1 | MAE=9.4228e-07 | t=0.3614s

Completed: 2026-04-16T15:33:54.194978+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.