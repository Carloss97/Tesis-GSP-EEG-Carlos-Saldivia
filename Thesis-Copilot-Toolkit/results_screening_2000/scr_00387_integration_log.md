# Integration Log: scr_00387
Started: 2026-04-16T13:13:36.965172+00:00
Description: Screening scr_00387 ds=bci_iv2a_real_s1 graph=kalofolias miss=[0.1] mode=base

## Dataset: bci_iv2a_real_s1 | rows=14
  Graph: kalofolias built OK
    mean | MR=0.1 | seed=0 | MAE=1.3025e-06 | t=0.0217s
    nearest | MR=0.1 | seed=0 | MAE=1.3708e-06 | t=0.0049s
    tikhonov | MR=0.1 | seed=0 | MAE=6.5591e-06 | t=0.0091s
    tv | MR=0.1 | seed=0 | MAE=1.3025e-06 | t=0.4772s
    trss | MR=0.1 | seed=0 | MAE=8.8942e-07 | t=0.1881s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=1.1339e-05 | t=0.0485s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=1.6525e-05 | t=8.3359s
    mean | MR=0.1 | seed=1 | MAE=1.2372e-06 | t=0.0020s
    nearest | MR=0.1 | seed=1 | MAE=1.2545e-06 | t=0.0028s
    tikhonov | MR=0.1 | seed=1 | MAE=6.5380e-06 | t=0.0063s
    tv | MR=0.1 | seed=1 | MAE=1.2372e-06 | t=0.2182s
    trss | MR=0.1 | seed=1 | MAE=8.3377e-07 | t=0.2008s

Completed: 2026-04-16T13:13:36.966325+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.