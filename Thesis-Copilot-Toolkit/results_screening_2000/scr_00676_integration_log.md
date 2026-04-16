# Integration Log: scr_00676
Started: 2026-04-16T15:14:16.701670+00:00
Description: Screening scr_00676 ds=bci_iv2a_real_s2 graph=knn miss=[0.4] mode=base

## Dataset: bci_iv2a_real_s2 | rows=14
  Graph: knn__k7 built OK
    mean | MR=0.4 | seed=0 | MAE=1.7972e-06 | t=0.0287s
    nearest | MR=0.4 | seed=0 | MAE=1.7309e-06 | t=0.1469s
    tikhonov | MR=0.4 | seed=0 | MAE=2.9181e-06 | t=0.1321s
    tv | MR=0.4 | seed=0 | MAE=1.7972e-06 | t=0.8715s
    trss | MR=0.4 | seed=0 | MAE=1.5057e-06 | t=0.3995s
    graph_time_tikhonov | MR=0.4 | seed=0 | MAE=5.2231e-06 | t=0.0610s
    temporal_laplacian | MR=0.4 | seed=0 | MAE=1.6508e-05 | t=28.4949s
    mean | MR=0.4 | seed=1 | MAE=1.7508e-06 | t=0.0718s
    nearest | MR=0.4 | seed=1 | MAE=1.7485e-06 | t=0.0147s
    tikhonov | MR=0.4 | seed=1 | MAE=2.8765e-06 | t=0.0263s
    tv | MR=0.4 | seed=1 | MAE=1.7508e-06 | t=0.7738s
    trss | MR=0.4 | seed=1 | MAE=1.4809e-06 | t=0.4650s

Completed: 2026-04-16T15:14:16.702540+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.