# Integration Log: scr_00640
Started: 2026-04-16T14:55:33.963902+00:00
Description: Screening scr_00640 ds=bci_iv2a_real_s2 graph=aew miss=[0.3] mode=base

## Dataset: bci_iv2a_real_s2 | rows=14
  Graph: aew built OK
    mean | MR=0.3 | seed=0 | MAE=1.2424e-06 | t=0.0030s
    nearest | MR=0.3 | seed=0 | MAE=1.2061e-06 | t=0.0103s
    tikhonov | MR=0.3 | seed=0 | MAE=2.1137e-06 | t=0.0086s
    tv | MR=0.3 | seed=0 | MAE=1.2422e-06 | t=0.2321s
    trss | MR=0.3 | seed=0 | MAE=1.0683e-06 | t=0.0298s
    graph_time_tikhonov | MR=0.3 | seed=0 | MAE=4.8277e-06 | t=0.0152s
    temporal_laplacian | MR=0.3 | seed=0 | MAE=1.4330e-05 | t=26.4396s
    mean | MR=0.3 | seed=1 | MAE=1.2418e-06 | t=0.0033s
    nearest | MR=0.3 | seed=1 | MAE=1.1920e-06 | t=0.0101s
    tikhonov | MR=0.3 | seed=1 | MAE=2.1119e-06 | t=0.0130s
    tv | MR=0.3 | seed=1 | MAE=1.2417e-06 | t=0.3588s
    trss | MR=0.3 | seed=1 | MAE=1.0506e-06 | t=0.4673s

Completed: 2026-04-16T14:55:33.964742+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.