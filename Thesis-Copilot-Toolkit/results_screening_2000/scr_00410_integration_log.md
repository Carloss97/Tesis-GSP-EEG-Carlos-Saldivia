# Integration Log: scr_00410
Started: 2026-04-16T13:20:36.039645+00:00
Description: Screening scr_00410 ds=physionet_real graph=vknng miss=[0.1] mode=base

## Dataset: physionet_eegmmidb_real | rows=14
  Graph: vknng built OK
    mean | MR=0.1 | seed=0 | MAE=2.0892e-06 | t=0.0030s
    nearest | MR=0.1 | seed=0 | MAE=2.3639e-06 | t=0.0044s
    tikhonov | MR=0.1 | seed=0 | MAE=5.5903e-06 | t=0.0086s
    tv | MR=0.1 | seed=0 | MAE=2.0662e-06 | t=0.4978s
    trss | MR=0.1 | seed=0 | MAE=1.0227e-06 | t=0.4920s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=1.1915e-05 | t=0.0520s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=2.9777e-05 | t=14.6424s
    mean | MR=0.1 | seed=1 | MAE=2.0496e-06 | t=0.0020s
    nearest | MR=0.1 | seed=1 | MAE=2.3187e-06 | t=0.0027s
    tikhonov | MR=0.1 | seed=1 | MAE=5.5672e-06 | t=0.0064s
    tv | MR=0.1 | seed=1 | MAE=2.0272e-06 | t=0.1695s
    trss | MR=0.1 | seed=1 | MAE=1.0059e-06 | t=0.2421s

Completed: 2026-04-16T13:20:36.040496+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.