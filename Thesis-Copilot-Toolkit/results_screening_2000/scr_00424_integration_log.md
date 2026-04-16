# Integration Log: scr_00424
Started: 2026-04-16T13:25:38.478271+00:00
Description: Screening scr_00424 ds=bci_iv2a_real_s2 graph=aew miss=[0.1] mode=base

## Dataset: bci_iv2a_real_s2 | rows=14
  Graph: aew built OK
    mean | MR=0.1 | seed=0 | MAE=3.3429e-07 | t=0.0237s
    nearest | MR=0.1 | seed=0 | MAE=3.2237e-07 | t=0.0044s
    tikhonov | MR=0.1 | seed=0 | MAE=1.4771e-06 | t=0.0104s
    tv | MR=0.1 | seed=0 | MAE=3.3427e-07 | t=0.3953s
    trss | MR=0.1 | seed=0 | MAE=2.7577e-07 | t=0.3109s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=4.5895e-06 | t=0.0154s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=1.3238e-05 | t=16.1140s
    mean | MR=0.1 | seed=1 | MAE=3.4821e-07 | t=0.0031s
    nearest | MR=0.1 | seed=1 | MAE=3.1417e-07 | t=0.0043s
    tikhonov | MR=0.1 | seed=1 | MAE=1.4825e-06 | t=0.0090s
    tv | MR=0.1 | seed=1 | MAE=3.4817e-07 | t=0.3148s
    trss | MR=0.1 | seed=1 | MAE=2.8207e-07 | t=0.0285s

Completed: 2026-04-16T13:25:38.479346+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.