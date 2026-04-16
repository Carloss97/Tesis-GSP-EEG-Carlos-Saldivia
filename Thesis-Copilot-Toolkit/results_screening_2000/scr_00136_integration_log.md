# Integration Log: scr_00136
Started: 2026-04-16T15:21:06.011086+00:00
Description: Screening scr_00136 ds=bci_iv2a_real_s2 graph=knn miss=2ch mode=base

## Dataset: bci_iv2a_real_s2 | rows=14
  Graph: knn__k7 built OK
    mean | MR=2ch | seed=0 | MAE=3.3429e-07 | t=0.0033s
    nearest | MR=2ch | seed=0 | MAE=3.2237e-07 | t=0.0049s
    tikhonov | MR=2ch | seed=0 | MAE=2.1282e-06 | t=0.0365s
    tv | MR=2ch | seed=0 | MAE=3.3430e-07 | t=0.8236s
    trss | MR=2ch | seed=0 | MAE=2.6217e-07 | t=0.4620s
    graph_time_tikhonov | MR=2ch | seed=0 | MAE=4.9978e-06 | t=0.0375s
    temporal_laplacian | MR=2ch | seed=0 | MAE=1.5420e-05 | t=35.5306s
    mean | MR=2ch | seed=1 | MAE=3.4821e-07 | t=0.0035s
    nearest | MR=2ch | seed=1 | MAE=3.1417e-07 | t=0.0058s
    tikhonov | MR=2ch | seed=1 | MAE=2.1327e-06 | t=0.0130s
    tv | MR=2ch | seed=1 | MAE=3.4822e-07 | t=0.9746s
    trss | MR=2ch | seed=1 | MAE=2.7673e-07 | t=0.7017s

Completed: 2026-04-16T15:21:06.011977+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.