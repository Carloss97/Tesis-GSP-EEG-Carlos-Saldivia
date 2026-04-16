# Integration Log: scr_00509
Started: 2026-04-16T13:55:25.281018+00:00
Description: Screening scr_00509 ds=bci_iv2a_real_s3 graph=knng miss=[0.2] mode=base

## Dataset: bci_iv2a_real_s3 | rows=14
  Graph: knng built OK
    mean | MR=0.2 | seed=0 | MAE=7.3135e-07 | t=0.0577s
    nearest | MR=0.2 | seed=0 | MAE=6.4516e-07 | t=0.0085s
    tikhonov | MR=0.2 | seed=0 | MAE=1.7176e-06 | t=0.0086s
    tv | MR=0.2 | seed=0 | MAE=7.3140e-07 | t=0.3374s
    trss | MR=0.2 | seed=0 | MAE=6.6338e-07 | t=0.6215s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.7323e-06 | t=0.0124s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=5.5557e-06 | t=15.9501s
    mean | MR=0.2 | seed=1 | MAE=7.3458e-07 | t=0.0035s
    nearest | MR=0.2 | seed=1 | MAE=6.4235e-07 | t=0.0055s
    tikhonov | MR=0.2 | seed=1 | MAE=1.7124e-06 | t=0.0058s
    tv | MR=0.2 | seed=1 | MAE=7.3462e-07 | t=0.1723s
    trss | MR=0.2 | seed=1 | MAE=6.7054e-07 | t=0.0194s

Completed: 2026-04-16T13:55:25.281875+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.