# Integration Log: scr_00112
Started: 2026-04-16T15:07:59.049313+00:00
Description: Screening scr_00112 ds=bci_iv2a_real_s2 graph=knn miss=2ch mode=base

## Dataset: bci_iv2a_real_s2 | rows=14
  Graph: knn__k3 built OK
    mean | MR=2ch | seed=0 | MAE=3.3429e-07 | t=0.0022s
    nearest | MR=2ch | seed=0 | MAE=3.2237e-07 | t=0.0028s
    tikhonov | MR=2ch | seed=0 | MAE=1.3859e-06 | t=0.0059s
    tv | MR=2ch | seed=0 | MAE=3.3429e-07 | t=0.4293s
    trss | MR=2ch | seed=0 | MAE=2.7621e-07 | t=0.5561s
    graph_time_tikhonov | MR=2ch | seed=0 | MAE=4.5658e-06 | t=0.0797s
    temporal_laplacian | MR=2ch | seed=0 | MAE=1.2481e-05 | t=26.6519s
    mean | MR=2ch | seed=1 | MAE=3.4821e-07 | t=0.0032s
    nearest | MR=2ch | seed=1 | MAE=3.1417e-07 | t=0.0029s
    tikhonov | MR=2ch | seed=1 | MAE=1.3896e-06 | t=0.0072s
    tv | MR=2ch | seed=1 | MAE=3.4820e-07 | t=0.1547s
    trss | MR=2ch | seed=1 | MAE=2.8718e-07 | t=0.0154s

Completed: 2026-04-16T15:07:59.050195+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.