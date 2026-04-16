# Integration Log: scr_00521
Started: 2026-04-16T14:00:12.411080+00:00
Description: Screening scr_00521 ds=bci_iv2a_real_s3 graph=vknng miss=[0.2] mode=base

## Dataset: bci_iv2a_real_s3 | rows=14
  Graph: vknng built OK
    mean | MR=0.2 | seed=0 | MAE=7.3135e-07 | t=0.0033s
    nearest | MR=0.2 | seed=0 | MAE=6.4516e-07 | t=0.0080s
    tikhonov | MR=0.2 | seed=0 | MAE=1.3471e-06 | t=0.0098s
    tv | MR=0.2 | seed=0 | MAE=7.3139e-07 | t=0.3056s
    trss | MR=0.2 | seed=0 | MAE=6.9474e-07 | t=0.0184s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.3100e-06 | t=0.0081s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=4.4452e-06 | t=23.4249s
    mean | MR=0.2 | seed=1 | MAE=7.3458e-07 | t=0.0020s
    nearest | MR=0.2 | seed=1 | MAE=6.4235e-07 | t=0.0050s
    tikhonov | MR=0.2 | seed=1 | MAE=1.3430e-06 | t=0.0059s
    tv | MR=0.2 | seed=1 | MAE=7.3462e-07 | t=0.1723s
    trss | MR=0.2 | seed=1 | MAE=6.9781e-07 | t=0.0179s

Completed: 2026-04-16T14:00:12.411944+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.