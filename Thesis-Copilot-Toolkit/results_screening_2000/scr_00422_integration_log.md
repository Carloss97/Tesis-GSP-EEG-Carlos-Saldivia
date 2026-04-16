# Integration Log: scr_00422
Started: 2026-04-16T13:24:40.386022+00:00
Description: Screening scr_00422 ds=physionet_real graph=aew miss=[0.1] mode=base

## Dataset: physionet_eegmmidb_real | rows=14
  Graph: aew built OK
    mean | MR=0.1 | seed=0 | MAE=2.0892e-06 | t=0.0021s
    nearest | MR=0.1 | seed=0 | MAE=2.3639e-06 | t=0.0030s
    tikhonov | MR=0.1 | seed=0 | MAE=4.8416e-06 | t=0.0108s
    tv | MR=0.1 | seed=0 | MAE=2.0630e-06 | t=0.1447s
    trss | MR=0.1 | seed=0 | MAE=9.8550e-07 | t=0.0163s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=1.0920e-05 | t=0.0079s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=2.8114e-05 | t=16.6871s
    mean | MR=0.1 | seed=1 | MAE=2.0496e-06 | t=0.0031s
    nearest | MR=0.1 | seed=1 | MAE=2.3187e-06 | t=0.0043s
    tikhonov | MR=0.1 | seed=1 | MAE=4.8236e-06 | t=0.0088s
    tv | MR=0.1 | seed=1 | MAE=2.0248e-06 | t=0.8060s
    trss | MR=0.1 | seed=1 | MAE=9.6475e-07 | t=0.3877s

Completed: 2026-04-16T13:24:40.387112+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.