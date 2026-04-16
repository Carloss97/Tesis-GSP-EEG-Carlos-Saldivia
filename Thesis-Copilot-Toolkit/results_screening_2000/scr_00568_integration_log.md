# Integration Log: scr_00568
Started: 2026-04-16T14:19:27.469452+00:00
Description: Screening scr_00568 ds=bci_iv2a_real_s2 graph=knn miss=[0.3] mode=base

## Dataset: bci_iv2a_real_s2 | rows=14
  Graph: knn__k7 built OK
    mean | MR=0.3 | seed=0 | MAE=1.2424e-06 | t=0.0207s
    nearest | MR=0.3 | seed=0 | MAE=1.2061e-06 | t=0.0240s
    tikhonov | MR=0.3 | seed=0 | MAE=2.6168e-06 | t=0.0103s
    tv | MR=0.3 | seed=0 | MAE=1.2424e-06 | t=0.2127s
    trss | MR=0.3 | seed=0 | MAE=1.0333e-06 | t=0.2360s
    graph_time_tikhonov | MR=0.3 | seed=0 | MAE=5.1387e-06 | t=0.0122s
    temporal_laplacian | MR=0.3 | seed=0 | MAE=1.6108e-05 | t=29.2970s
    mean | MR=0.3 | seed=1 | MAE=1.2418e-06 | t=0.0032s
    nearest | MR=0.3 | seed=1 | MAE=1.1920e-06 | t=0.0425s
    tikhonov | MR=0.3 | seed=1 | MAE=2.6190e-06 | t=0.0457s
    tv | MR=0.3 | seed=1 | MAE=1.2418e-06 | t=0.5203s
    trss | MR=0.3 | seed=1 | MAE=1.0139e-06 | t=0.0855s

Completed: 2026-04-16T14:19:27.470619+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.