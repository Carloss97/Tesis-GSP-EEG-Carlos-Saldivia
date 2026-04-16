# Integration Log: scr_00747
Started: 2026-04-16T11:52:10.845029+00:00
Description: Screening scr_00747 ds=bci_iv2a_real_s1 graph=aew miss=[0.4] mode=base

## Dataset: bci_iv2a_real_s1 | rows=14
  Graph: aew built OK
    mean | MR=0.4 | seed=0 | MAE=6.3033e-06 | t=0.0020s
    nearest | MR=0.4 | seed=0 | MAE=6.5281e-06 | t=0.0089s
    tikhonov | MR=0.4 | seed=0 | MAE=7.2432e-06 | t=0.0058s
    tv | MR=0.4 | seed=0 | MAE=6.2895e-06 | t=0.1513s
    trss | MR=0.4 | seed=0 | MAE=4.7428e-06 | t=0.0202s
    graph_time_tikhonov | MR=0.4 | seed=0 | MAE=9.8795e-06 | t=0.0084s
    temporal_laplacian | MR=0.4 | seed=0 | MAE=1.5997e-05 | t=1.2483s
    mean | MR=0.4 | seed=1 | MAE=6.2507e-06 | t=0.0020s
    nearest | MR=0.4 | seed=1 | MAE=6.8607e-06 | t=0.0086s
    tikhonov | MR=0.4 | seed=1 | MAE=7.1729e-06 | t=0.0058s
    tv | MR=0.4 | seed=1 | MAE=6.2358e-06 | t=0.1516s
    trss | MR=0.4 | seed=1 | MAE=4.7404e-06 | t=0.0202s

Completed: 2026-04-16T11:52:10.845725+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.