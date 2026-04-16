# Integration Log: scr_00292
Started: 2026-04-16T15:14:57.026655+00:00
Description: Screening scr_00292 ds=bci_iv2a_real_s2 graph=knng miss=3ch mode=base

## Dataset: bci_iv2a_real_s2 | rows=14
  Graph: knng built OK
    mean | MR=3ch | seed=0 | MAE=5.2945e-07 | t=0.0031s
    nearest | MR=3ch | seed=0 | MAE=5.1829e-07 | t=0.0057s
    tikhonov | MR=3ch | seed=0 | MAE=1.7496e-06 | t=0.0086s
    tv | MR=3ch | seed=0 | MAE=5.2947e-07 | t=0.6476s
    trss | MR=3ch | seed=0 | MAE=4.5340e-07 | t=0.4217s
    graph_time_tikhonov | MR=3ch | seed=0 | MAE=4.7667e-06 | t=0.1123s
    temporal_laplacian | MR=3ch | seed=0 | MAE=1.3797e-05 | t=31.5316s
    mean | MR=3ch | seed=1 | MAE=5.2909e-07 | t=0.0031s
    nearest | MR=3ch | seed=1 | MAE=4.9473e-07 | t=0.0054s
    tikhonov | MR=3ch | seed=1 | MAE=1.7486e-06 | t=0.0087s
    tv | MR=3ch | seed=1 | MAE=5.2911e-07 | t=0.5727s
    trss | MR=3ch | seed=1 | MAE=4.4595e-07 | t=0.9231s

Completed: 2026-04-16T15:14:57.027532+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.