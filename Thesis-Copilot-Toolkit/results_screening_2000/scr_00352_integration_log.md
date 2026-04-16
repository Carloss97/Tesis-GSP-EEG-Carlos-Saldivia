# Integration Log: scr_00352
Started: 2026-04-16T13:06:57.539514+00:00
Description: Screening scr_00352 ds=bci_iv2a_real_s2 graph=knn miss=[0.1] mode=base

## Dataset: bci_iv2a_real_s2 | rows=14
  Graph: knn__k7 built OK
    mean | MR=0.1 | seed=0 | MAE=3.3429e-07 | t=0.0030s
    nearest | MR=0.1 | seed=0 | MAE=3.2237e-07 | t=0.0042s
    tikhonov | MR=0.1 | seed=0 | MAE=2.1282e-06 | t=0.0068s
    tv | MR=0.1 | seed=0 | MAE=3.3430e-07 | t=0.1622s
    trss | MR=0.1 | seed=0 | MAE=2.6217e-07 | t=0.0164s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=4.9978e-06 | t=0.0078s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=1.5420e-05 | t=8.8618s
    mean | MR=0.1 | seed=1 | MAE=3.4821e-07 | t=0.0020s
    nearest | MR=0.1 | seed=1 | MAE=3.1417e-07 | t=0.0027s
    tikhonov | MR=0.1 | seed=1 | MAE=2.1327e-06 | t=0.0065s
    tv | MR=0.1 | seed=1 | MAE=3.4822e-07 | t=0.1607s
    trss | MR=0.1 | seed=1 | MAE=2.7673e-07 | t=0.0165s

Completed: 2026-04-16T13:06:57.540439+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.