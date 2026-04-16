# Integration Log: scr_00042
Started: 2026-04-16T15:37:53.670031+00:00
Description: Screening scr_00042 ds=iv100hz_mat graph=gaussian miss=1ch mode=base

## Dataset: iv100hz_mat | rows=14
  Graph: gaussian__sigma1.0 built OK
    mean | MR=1ch | seed=0 | MAE=1.1091e+01 | t=0.0042s
    nearest | MR=1ch | seed=0 | MAE=1.6962e+01 | t=0.0064s
    tikhonov | MR=1ch | seed=0 | MAE=1.2953e+02 | t=0.1343s
    tv | MR=1ch | seed=0 | MAE=6.8988e+00 | t=1.1289s
    trss | MR=1ch | seed=0 | MAE=7.4137e+00 | t=0.4676s
    graph_time_tikhonov | MR=1ch | seed=0 | MAE=2.0283e+02 | t=0.0781s
    temporal_laplacian | MR=1ch | seed=0 | MAE=2.6386e+02 | t=16.7238s
    mean | MR=1ch | seed=1 | MAE=1.0242e+01 | t=0.0042s
    nearest | MR=1ch | seed=1 | MAE=1.6572e+01 | t=0.0031s
    tikhonov | MR=1ch | seed=1 | MAE=1.2928e+02 | t=0.0275s
    tv | MR=1ch | seed=1 | MAE=5.7627e+00 | t=0.6791s
    trss | MR=1ch | seed=1 | MAE=7.0485e+00 | t=0.3631s

Completed: 2026-04-16T15:37:53.671305+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.