# Integration Log: scr_00172
Started: 2026-04-16T15:40:47.224386+00:00
Description: Screening scr_00172 ds=bci_iv2a_real_s2 graph=kalofolias miss=2ch mode=base

## Dataset: bci_iv2a_real_s2 | rows=14
  Graph: kalofolias built OK
    mean | MR=2ch | seed=0 | MAE=3.3429e-07 | t=0.0364s
    nearest | MR=2ch | seed=0 | MAE=3.2237e-07 | t=0.1275s
    tikhonov | MR=2ch | seed=0 | MAE=1.8559e-06 | t=0.0108s
    tv | MR=2ch | seed=0 | MAE=3.3429e-07 | t=1.1294s
    trss | MR=2ch | seed=0 | MAE=2.3794e-07 | t=0.3265s
    graph_time_tikhonov | MR=2ch | seed=0 | MAE=4.9271e-06 | t=0.0137s
    temporal_laplacian | MR=2ch | seed=0 | MAE=1.4727e-05 | t=30.9659s
    mean | MR=2ch | seed=1 | MAE=3.4821e-07 | t=0.0038s
    nearest | MR=2ch | seed=1 | MAE=3.1417e-07 | t=0.0049s
    tikhonov | MR=2ch | seed=1 | MAE=1.8665e-06 | t=0.0089s
    tv | MR=2ch | seed=1 | MAE=3.4821e-07 | t=0.7345s
    trss | MR=2ch | seed=1 | MAE=2.5203e-07 | t=0.0456s

Completed: 2026-04-16T15:40:47.226720+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.