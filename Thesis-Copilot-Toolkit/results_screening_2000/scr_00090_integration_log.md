# Integration Log: scr_00090
Started: 2026-04-16T14:57:58.407371+00:00
Description: Screening scr_00090 ds=iv100hz_mat graph=vknng miss=1ch mode=base

## Dataset: iv100hz_mat | rows=14
  Graph: vknng built OK
    mean | MR=1ch | seed=0 | MAE=1.1091e+01 | t=0.0032s
    nearest | MR=1ch | seed=0 | MAE=1.6962e+01 | t=0.0032s
    tikhonov | MR=1ch | seed=0 | MAE=7.8189e+01 | t=0.0419s
    tv | MR=1ch | seed=0 | MAE=7.7123e+00 | t=0.5229s
    trss | MR=1ch | seed=0 | MAE=7.3504e+00 | t=0.1557s
    graph_time_tikhonov | MR=1ch | seed=0 | MAE=1.6042e+02 | t=0.0344s
    temporal_laplacian | MR=1ch | seed=0 | MAE=1.9806e+02 | t=28.1835s
    mean | MR=1ch | seed=1 | MAE=1.0242e+01 | t=0.0362s
    nearest | MR=1ch | seed=1 | MAE=1.6572e+01 | t=0.0032s
    tikhonov | MR=1ch | seed=1 | MAE=7.8068e+01 | t=0.0093s
    tv | MR=1ch | seed=1 | MAE=7.4363e+00 | t=0.3510s
    trss | MR=1ch | seed=1 | MAE=7.2307e+00 | t=0.0264s

Completed: 2026-04-16T14:57:58.408242+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.