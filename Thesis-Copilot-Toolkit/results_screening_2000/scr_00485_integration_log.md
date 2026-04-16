# Integration Log: scr_00485
Started: 2026-04-16T13:46:53.666916+00:00
Description: Screening scr_00485 ds=bci_iv2a_real_s3 graph=gaussian miss=[0.2] mode=base

## Dataset: bci_iv2a_real_s3 | rows=14
  Graph: gaussian__sigma0.6 built OK
    mean | MR=0.2 | seed=0 | MAE=7.3135e-07 | t=0.0030s
    nearest | MR=0.2 | seed=0 | MAE=6.4516e-07 | t=0.0089s
    tikhonov | MR=0.2 | seed=0 | MAE=2.6050e-06 | t=0.0215s
    tv | MR=0.2 | seed=0 | MAE=7.3135e-07 | t=0.5479s
    trss | MR=0.2 | seed=0 | MAE=5.4944e-07 | t=0.1423s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=3.2558e-06 | t=0.0151s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=6.5405e-06 | t=18.4375s
    mean | MR=0.2 | seed=1 | MAE=7.3458e-07 | t=0.0489s
    nearest | MR=0.2 | seed=1 | MAE=6.4235e-07 | t=0.0078s
    tikhonov | MR=0.2 | seed=1 | MAE=2.6022e-06 | t=0.0126s
    tv | MR=0.2 | seed=1 | MAE=7.3458e-07 | t=0.6098s
    trss | MR=0.2 | seed=1 | MAE=5.5970e-07 | t=0.2278s

Completed: 2026-04-16T13:46:53.667717+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.