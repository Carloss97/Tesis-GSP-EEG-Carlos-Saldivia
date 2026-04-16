# Integration Log: scr_00459
Started: 2026-04-16T13:37:37.941711+00:00
Description: Screening scr_00459 ds=bci_iv2a_real_s1 graph=knn miss=[0.2] mode=base

## Dataset: bci_iv2a_real_s1 | rows=14
  Graph: knn__k7 built OK
    mean | MR=0.2 | seed=0 | MAE=3.0357e-06 | t=0.0032s
    nearest | MR=0.2 | seed=0 | MAE=3.2140e-06 | t=0.0077s
    tikhonov | MR=0.2 | seed=0 | MAE=8.0179e-06 | t=0.0141s
    tv | MR=0.2 | seed=0 | MAE=3.0355e-06 | t=0.5626s
    trss | MR=0.2 | seed=0 | MAE=2.0527e-06 | t=0.1256s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.2053e-05 | t=0.0136s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.7539e-05 | t=13.3850s
    mean | MR=0.2 | seed=1 | MAE=3.3734e-06 | t=0.0040s
    nearest | MR=0.2 | seed=1 | MAE=3.5344e-06 | t=0.0078s
    tikhonov | MR=0.2 | seed=1 | MAE=8.1417e-06 | t=0.0226s
    tv | MR=0.2 | seed=1 | MAE=3.3731e-06 | t=0.3470s
    trss | MR=0.2 | seed=1 | MAE=2.3376e-06 | t=0.0201s

Completed: 2026-04-16T13:37:37.942724+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.