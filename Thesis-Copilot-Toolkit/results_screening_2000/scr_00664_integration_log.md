# Integration Log: scr_00664
Started: 2026-04-16T15:07:59.695730+00:00
Description: Screening scr_00664 ds=bci_iv2a_real_s2 graph=knn miss=[0.4] mode=base

## Dataset: bci_iv2a_real_s2 | rows=14
  Graph: knn__k5 built OK
    mean | MR=0.4 | seed=0 | MAE=1.7972e-06 | t=0.0022s
    nearest | MR=0.4 | seed=0 | MAE=1.7309e-06 | t=0.0181s
    tikhonov | MR=0.4 | seed=0 | MAE=2.7098e-06 | t=0.0064s
    tv | MR=0.4 | seed=0 | MAE=1.7972e-06 | t=0.5705s
    trss | MR=0.4 | seed=0 | MAE=1.5155e-06 | t=0.3837s
    graph_time_tikhonov | MR=0.4 | seed=0 | MAE=5.1220e-06 | t=0.0151s
    temporal_laplacian | MR=0.4 | seed=0 | MAE=1.5799e-05 | t=27.2142s
    mean | MR=0.4 | seed=1 | MAE=1.7508e-06 | t=0.0022s
    nearest | MR=0.4 | seed=1 | MAE=1.7485e-06 | t=0.0100s
    tikhonov | MR=0.4 | seed=1 | MAE=2.6727e-06 | t=0.0061s
    tv | MR=0.4 | seed=1 | MAE=1.7508e-06 | t=0.1870s
    trss | MR=0.4 | seed=1 | MAE=1.4938e-06 | t=0.0200s

Completed: 2026-04-16T15:07:59.696827+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.