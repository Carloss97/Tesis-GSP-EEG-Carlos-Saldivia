# Integration Log: scr_00425
Started: 2026-04-16T13:26:22.382117+00:00
Description: Screening scr_00425 ds=bci_iv2a_real_s3 graph=aew miss=[0.1] mode=base

## Dataset: bci_iv2a_real_s3 | rows=14
  Graph: aew built OK
    mean | MR=0.1 | seed=0 | MAE=3.0419e-07 | t=0.0030s
    nearest | MR=0.1 | seed=0 | MAE=2.4876e-07 | t=0.0044s
    tikhonov | MR=0.1 | seed=0 | MAE=1.1395e-06 | t=0.0337s
    tv | MR=0.1 | seed=0 | MAE=3.0419e-07 | t=0.5278s
    trss | MR=0.1 | seed=0 | MAE=2.6581e-07 | t=0.0173s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=2.2714e-06 | t=0.0080s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=4.7802e-06 | t=16.9274s
    mean | MR=0.1 | seed=1 | MAE=2.8472e-07 | t=0.0031s
    nearest | MR=0.1 | seed=1 | MAE=2.5230e-07 | t=0.0045s
    tikhonov | MR=0.1 | seed=1 | MAE=1.1171e-06 | t=0.0153s
    tv | MR=0.1 | seed=1 | MAE=2.8470e-07 | t=0.3211s
    trss | MR=0.1 | seed=1 | MAE=2.5203e-07 | t=0.3575s

Completed: 2026-04-16T13:26:22.383215+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.