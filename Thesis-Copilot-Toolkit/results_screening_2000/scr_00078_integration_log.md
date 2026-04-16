# Integration Log: scr_00078
Started: 2026-04-16T14:52:20.832024+00:00
Description: Screening scr_00078 ds=iv100hz_mat graph=knng miss=1ch mode=base

## Dataset: iv100hz_mat | rows=14
  Graph: knng built OK
    mean | MR=1ch | seed=0 | MAE=1.1091e+01 | t=0.0021s
    nearest | MR=1ch | seed=0 | MAE=1.6962e+01 | t=0.0023s
    tikhonov | MR=1ch | seed=0 | MAE=7.5381e+01 | t=0.0076s
    tv | MR=1ch | seed=0 | MAE=7.7664e+00 | t=0.2553s
    trss | MR=1ch | seed=0 | MAE=7.4432e+00 | t=0.0957s
    graph_time_tikhonov | MR=1ch | seed=0 | MAE=1.5743e+02 | t=0.0161s
    temporal_laplacian | MR=1ch | seed=0 | MAE=1.9547e+02 | t=24.9727s
    mean | MR=1ch | seed=1 | MAE=1.0242e+01 | t=0.0032s
    nearest | MR=1ch | seed=1 | MAE=1.6572e+01 | t=0.0032s
    tikhonov | MR=1ch | seed=1 | MAE=7.5267e+01 | t=0.0172s
    tv | MR=1ch | seed=1 | MAE=7.4085e+00 | t=0.4290s
    trss | MR=1ch | seed=1 | MAE=7.3379e+00 | t=0.3295s

Completed: 2026-04-16T14:52:20.832941+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.