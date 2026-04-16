# Integration Log: scr_00628
Started: 2026-04-16T14:49:23.871485+00:00
Description: Screening scr_00628 ds=bci_iv2a_real_s2 graph=vknng miss=[0.3] mode=base

## Dataset: bci_iv2a_real_s2 | rows=14
  Graph: vknng built OK
    mean | MR=0.3 | seed=0 | MAE=1.2424e-06 | t=0.0031s
    nearest | MR=0.3 | seed=0 | MAE=1.2061e-06 | t=0.0552s
    tikhonov | MR=0.3 | seed=0 | MAE=1.8588e-06 | t=0.0086s
    tv | MR=0.3 | seed=0 | MAE=1.2424e-06 | t=0.4125s
    trss | MR=0.3 | seed=0 | MAE=1.1609e-06 | t=0.2137s
    graph_time_tikhonov | MR=0.3 | seed=0 | MAE=4.6395e-06 | t=0.0126s
    temporal_laplacian | MR=0.3 | seed=0 | MAE=1.2122e-05 | t=21.4668s
    mean | MR=0.3 | seed=1 | MAE=1.2418e-06 | t=0.0058s
    nearest | MR=0.3 | seed=1 | MAE=1.1920e-06 | t=0.0247s
    tikhonov | MR=0.3 | seed=1 | MAE=1.8550e-06 | t=0.0405s
    tv | MR=0.3 | seed=1 | MAE=1.2418e-06 | t=0.3957s
    trss | MR=0.3 | seed=1 | MAE=1.1376e-06 | t=0.4133s

Completed: 2026-04-16T14:49:23.872345+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.