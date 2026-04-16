# Integration Log: scr_00351
Started: 2026-04-16T13:06:38.839213+00:00
Description: Screening scr_00351 ds=bci_iv2a_real_s1 graph=knn miss=[0.1] mode=base

## Dataset: bci_iv2a_real_s1 | rows=14
  Graph: knn__k7 built OK
    mean | MR=0.1 | seed=0 | MAE=1.3025e-06 | t=0.0035s
    nearest | MR=0.1 | seed=0 | MAE=1.3708e-06 | t=0.0046s
    tikhonov | MR=0.1 | seed=0 | MAE=6.9979e-06 | t=0.0094s
    tv | MR=0.1 | seed=0 | MAE=1.3024e-06 | t=0.3653s
    trss | MR=0.1 | seed=0 | MAE=8.5933e-07 | t=0.2110s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=1.1542e-05 | t=0.0079s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=1.7024e-05 | t=3.2554s
    mean | MR=0.1 | seed=1 | MAE=1.2372e-06 | t=0.0040s
    nearest | MR=0.1 | seed=1 | MAE=1.2545e-06 | t=0.0028s
    tikhonov | MR=0.1 | seed=1 | MAE=6.9717e-06 | t=0.0058s
    tv | MR=0.1 | seed=1 | MAE=1.2371e-06 | t=0.2063s
    trss | MR=0.1 | seed=1 | MAE=8.0482e-07 | t=0.2344s

Completed: 2026-04-16T13:06:38.840075+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.