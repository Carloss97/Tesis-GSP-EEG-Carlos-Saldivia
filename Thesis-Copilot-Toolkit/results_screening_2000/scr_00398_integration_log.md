# Integration Log: scr_00398
Started: 2026-04-16T13:16:36.833460+00:00
Description: Screening scr_00398 ds=physionet_real graph=knng miss=[0.1] mode=base

## Dataset: physionet_eegmmidb_real | rows=14
  Graph: knng built OK
    mean | MR=0.1 | seed=0 | MAE=2.0892e-06 | t=0.0037s
    nearest | MR=0.1 | seed=0 | MAE=2.3639e-06 | t=0.0044s
    tikhonov | MR=0.1 | seed=0 | MAE=5.6348e-06 | t=0.0087s
    tv | MR=0.1 | seed=0 | MAE=2.0688e-06 | t=0.4192s
    trss | MR=0.1 | seed=0 | MAE=1.0043e-06 | t=0.0616s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=1.2052e-05 | t=0.0126s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=3.0146e-05 | t=16.5208s
    mean | MR=0.1 | seed=1 | MAE=2.0496e-06 | t=0.0034s
    nearest | MR=0.1 | seed=1 | MAE=2.3187e-06 | t=0.0044s
    tikhonov | MR=0.1 | seed=1 | MAE=5.6214e-06 | t=0.0094s
    tv | MR=0.1 | seed=1 | MAE=2.0300e-06 | t=0.3148s
    trss | MR=0.1 | seed=1 | MAE=9.8924e-07 | t=0.0422s

Completed: 2026-04-16T13:16:36.834157+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.