# Integration Log: scr_00123
Started: 2026-04-16T15:12:34.836394+00:00
Description: Screening scr_00123 ds=bci_iv2a_real_s1 graph=knn miss=2ch mode=base

## Dataset: bci_iv2a_real_s1 | rows=14
  Graph: knn__k5 built OK
    mean | MR=2ch | seed=0 | MAE=1.3025e-06 | t=0.0033s
    nearest | MR=2ch | seed=0 | MAE=1.3708e-06 | t=0.0365s
    tikhonov | MR=2ch | seed=0 | MAE=6.0125e-06 | t=0.0086s
    tv | MR=2ch | seed=0 | MAE=1.3025e-06 | t=0.5663s
    trss | MR=2ch | seed=0 | MAE=9.1600e-07 | t=0.3599s
    graph_time_tikhonov | MR=2ch | seed=0 | MAE=1.0783e-05 | t=0.0155s
    temporal_laplacian | MR=2ch | seed=0 | MAE=1.6058e-05 | t=4.2170s
    mean | MR=2ch | seed=1 | MAE=1.2372e-06 | t=0.0022s
    nearest | MR=2ch | seed=1 | MAE=1.2545e-06 | t=0.0029s
    tikhonov | MR=2ch | seed=1 | MAE=5.9697e-06 | t=0.0064s
    tv | MR=2ch | seed=1 | MAE=1.2371e-06 | t=0.1650s
    trss | MR=2ch | seed=1 | MAE=8.3782e-07 | t=0.1940s

Completed: 2026-04-16T15:12:34.837479+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.