# Integration Log: scr_00473
Started: 2026-04-16T13:42:47.936553+00:00
Description: Screening scr_00473 ds=bci_iv2a_real_s3 graph=gaussian miss=[0.2] mode=base

## Dataset: bci_iv2a_real_s3 | rows=14
  Graph: gaussian__sigma1.0 built OK
    mean | MR=0.2 | seed=0 | MAE=7.3135e-07 | t=0.0031s
    nearest | MR=0.2 | seed=0 | MAE=6.4516e-07 | t=0.0079s
    tikhonov | MR=0.2 | seed=0 | MAE=2.6050e-06 | t=0.0087s
    tv | MR=0.2 | seed=0 | MAE=7.3135e-07 | t=0.3938s
    trss | MR=0.2 | seed=0 | MAE=5.4944e-07 | t=0.3053s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=3.2558e-06 | t=0.0680s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=6.5405e-06 | t=15.7177s
    mean | MR=0.2 | seed=1 | MAE=7.3458e-07 | t=0.0039s
    nearest | MR=0.2 | seed=1 | MAE=6.4235e-07 | t=0.0079s
    tikhonov | MR=0.2 | seed=1 | MAE=2.6022e-06 | t=0.0326s
    tv | MR=0.2 | seed=1 | MAE=7.3458e-07 | t=1.2604s
    trss | MR=0.2 | seed=1 | MAE=5.5970e-07 | t=0.6930s

Completed: 2026-04-16T13:42:47.937691+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.