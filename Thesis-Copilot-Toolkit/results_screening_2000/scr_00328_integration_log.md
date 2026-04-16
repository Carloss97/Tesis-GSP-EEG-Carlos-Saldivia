# Integration Log: scr_00328
Started: 2026-04-16T15:35:43.119247+00:00
Description: Screening scr_00328 ds=bci_iv2a_real_s2 graph=knn miss=[0.1] mode=base

## Dataset: bci_iv2a_real_s2 | rows=14
  Graph: knn__k3 built OK
    mean | MR=0.1 | seed=0 | MAE=3.3429e-07 | t=0.0032s
    nearest | MR=0.1 | seed=0 | MAE=3.2237e-07 | t=0.0046s
    tikhonov | MR=0.1 | seed=0 | MAE=1.3859e-06 | t=0.0279s
    tv | MR=0.1 | seed=0 | MAE=3.3429e-07 | t=0.4323s
    trss | MR=0.1 | seed=0 | MAE=2.7621e-07 | t=0.1060s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=4.5658e-06 | t=0.0270s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=1.2481e-05 | t=22.3829s
    mean | MR=0.1 | seed=1 | MAE=3.4821e-07 | t=0.0038s
    nearest | MR=0.1 | seed=1 | MAE=3.1417e-07 | t=0.0231s
    tikhonov | MR=0.1 | seed=1 | MAE=1.3896e-06 | t=0.0110s
    tv | MR=0.1 | seed=1 | MAE=3.4820e-07 | t=0.4508s
    trss | MR=0.1 | seed=1 | MAE=2.8718e-07 | t=0.0553s

Completed: 2026-04-16T15:35:43.120518+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.