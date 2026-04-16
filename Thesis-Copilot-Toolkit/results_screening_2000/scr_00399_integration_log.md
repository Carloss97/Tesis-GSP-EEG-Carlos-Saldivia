# Integration Log: scr_00399
Started: 2026-04-16T13:17:14.451429+00:00
Description: Screening scr_00399 ds=bci_iv2a_real_s1 graph=knng miss=[0.1] mode=base

## Dataset: bci_iv2a_real_s1 | rows=14
  Graph: knng built OK
    mean | MR=0.1 | seed=0 | MAE=1.3025e-06 | t=0.0039s
    nearest | MR=0.1 | seed=0 | MAE=1.3708e-06 | t=0.0493s
    tikhonov | MR=0.1 | seed=0 | MAE=5.4259e-06 | t=0.0497s
    tv | MR=0.1 | seed=0 | MAE=1.3025e-06 | t=0.6289s
    trss | MR=0.1 | seed=0 | MAE=9.5392e-07 | t=0.2741s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=1.0216e-05 | t=0.0135s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=1.5353e-05 | t=7.5441s
    mean | MR=0.1 | seed=1 | MAE=1.2372e-06 | t=0.0020s
    nearest | MR=0.1 | seed=1 | MAE=1.2545e-06 | t=0.0029s
    tikhonov | MR=0.1 | seed=1 | MAE=5.3746e-06 | t=0.0058s
    tv | MR=0.1 | seed=1 | MAE=1.2372e-06 | t=0.1697s
    trss | MR=0.1 | seed=1 | MAE=8.8079e-07 | t=0.1525s

Completed: 2026-04-16T13:17:14.452305+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.