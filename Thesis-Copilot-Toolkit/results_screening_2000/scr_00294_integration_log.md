# Integration Log: scr_00294
Started: 2026-04-16T15:17:41.533838+00:00
Description: Screening scr_00294 ds=iv100hz_mat graph=knng miss=3ch mode=base

## Dataset: iv100hz_mat | rows=14
  Graph: knng built OK
    mean | MR=3ch | seed=0 | MAE=3.0766e+01 | t=0.0349s
    nearest | MR=3ch | seed=0 | MAE=4.8015e+01 | t=0.0053s
    tikhonov | MR=3ch | seed=0 | MAE=9.1431e+01 | t=0.0087s
    tv | MR=3ch | seed=0 | MAE=2.3145e+01 | t=0.6510s
    trss | MR=3ch | seed=0 | MAE=2.2635e+01 | t=0.5057s
    graph_time_tikhonov | MR=3ch | seed=0 | MAE=1.6551e+02 | t=0.0690s
    temporal_laplacian | MR=3ch | seed=0 | MAE=2.0124e+02 | t=31.9483s
    mean | MR=3ch | seed=1 | MAE=3.1144e+01 | t=0.0034s
    nearest | MR=3ch | seed=1 | MAE=4.9179e+01 | t=0.0054s
    tikhonov | MR=3ch | seed=1 | MAE=9.1342e+01 | t=0.0087s
    tv | MR=3ch | seed=1 | MAE=2.2014e+01 | t=0.5139s
    trss | MR=3ch | seed=1 | MAE=2.2982e+01 | t=0.4181s

Completed: 2026-04-16T15:17:41.535121+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.