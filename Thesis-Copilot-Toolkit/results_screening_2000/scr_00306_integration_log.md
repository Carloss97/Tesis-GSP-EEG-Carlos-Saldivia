# Integration Log: scr_00306
Started: 2026-04-16T15:25:06.787018+00:00
Description: Screening scr_00306 ds=iv100hz_mat graph=vknng miss=3ch mode=base

## Dataset: iv100hz_mat | rows=14
  Graph: vknng built OK
    mean | MR=3ch | seed=0 | MAE=3.0766e+01 | t=0.0051s
    nearest | MR=3ch | seed=0 | MAE=4.8015e+01 | t=0.0055s
    tikhonov | MR=3ch | seed=0 | MAE=9.3770e+01 | t=0.0467s
    tv | MR=3ch | seed=0 | MAE=2.3713e+01 | t=0.5217s
    trss | MR=3ch | seed=0 | MAE=2.2300e+01 | t=0.2440s
    graph_time_tikhonov | MR=3ch | seed=0 | MAE=1.6814e+02 | t=0.0245s
    temporal_laplacian | MR=3ch | seed=0 | MAE=2.0366e+02 | t=36.9309s
    mean | MR=3ch | seed=1 | MAE=3.1144e+01 | t=0.0522s
    nearest | MR=3ch | seed=1 | MAE=4.9179e+01 | t=0.0068s
    tikhonov | MR=3ch | seed=1 | MAE=9.3678e+01 | t=0.0460s
    tv | MR=3ch | seed=1 | MAE=2.2461e+01 | t=1.0505s
    trss | MR=3ch | seed=1 | MAE=2.2643e+01 | t=0.3518s

Completed: 2026-04-16T15:25:06.788603+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.