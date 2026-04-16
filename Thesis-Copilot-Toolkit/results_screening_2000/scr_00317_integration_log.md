# Integration Log: scr_00317
Started: 2026-04-16T15:30:48.283841+00:00
Description: Screening scr_00317 ds=bci_iv2a_real_s3 graph=aew miss=3ch mode=base

## Dataset: bci_iv2a_real_s3 | rows=14
  Graph: aew built OK
    mean | MR=3ch | seed=0 | MAE=4.5067e-07 | t=0.0033s
    nearest | MR=3ch | seed=0 | MAE=4.0021e-07 | t=0.0089s
    tikhonov | MR=3ch | seed=0 | MAE=1.2438e-06 | t=0.0124s
    tv | MR=3ch | seed=0 | MAE=4.5065e-07 | t=0.5135s
    trss | MR=3ch | seed=0 | MAE=3.9416e-07 | t=0.6960s
    graph_time_tikhonov | MR=3ch | seed=0 | MAE=2.3268e-06 | t=0.0328s
    temporal_laplacian | MR=3ch | seed=0 | MAE=4.8658e-06 | t=20.4788s
    mean | MR=3ch | seed=1 | MAE=4.4119e-07 | t=0.0039s
    nearest | MR=3ch | seed=1 | MAE=3.7573e-07 | t=0.0074s
    tikhonov | MR=3ch | seed=1 | MAE=1.2395e-06 | t=0.0153s
    tv | MR=3ch | seed=1 | MAE=4.4117e-07 | t=0.4390s
    trss | MR=3ch | seed=1 | MAE=3.8462e-07 | t=0.1649s

Completed: 2026-04-16T15:30:48.313463+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.