# Integration Log: scr_00556
Started: 2026-04-16T14:13:15.870209+00:00
Description: Screening scr_00556 ds=bci_iv2a_real_s2 graph=knn miss=[0.3] mode=base

## Dataset: bci_iv2a_real_s2 | rows=14
  Graph: knn__k5 built OK
    mean | MR=0.3 | seed=0 | MAE=1.2424e-06 | t=0.0021s
    nearest | MR=0.3 | seed=0 | MAE=1.2061e-06 | t=0.0070s
    tikhonov | MR=0.3 | seed=0 | MAE=2.3678e-06 | t=0.0073s
    tv | MR=0.3 | seed=0 | MAE=1.2424e-06 | t=0.3607s
    trss | MR=0.3 | seed=0 | MAE=1.0448e-06 | t=0.2177s
    graph_time_tikhonov | MR=0.3 | seed=0 | MAE=5.0171e-06 | t=0.0124s
    temporal_laplacian | MR=0.3 | seed=0 | MAE=1.5271e-05 | t=22.1420s
    mean | MR=0.3 | seed=1 | MAE=1.2418e-06 | t=0.0364s
    nearest | MR=0.3 | seed=1 | MAE=1.1920e-06 | t=0.0411s
    tikhonov | MR=0.3 | seed=1 | MAE=2.3747e-06 | t=0.0363s
    tv | MR=0.3 | seed=1 | MAE=1.2418e-06 | t=0.7203s
    trss | MR=0.3 | seed=1 | MAE=1.0292e-06 | t=0.1305s

Completed: 2026-04-16T14:13:15.873733+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.