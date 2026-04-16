# Integration Log: scr_00066
Started: 2026-04-16T14:46:41.307414+00:00
Description: Screening scr_00066 ds=iv100hz_mat graph=kalofolias miss=1ch mode=base

## Dataset: iv100hz_mat | rows=14
  Graph: kalofolias built OK
    mean | MR=1ch | seed=0 | MAE=1.1091e+01 | t=0.0034s
    nearest | MR=1ch | seed=0 | MAE=1.6962e+01 | t=0.0221s
    tikhonov | MR=1ch | seed=0 | MAE=1.6677e+02 | t=0.0118s
    tv | MR=1ch | seed=0 | MAE=1.0752e+01 | t=0.6125s
    trss | MR=1ch | seed=0 | MAE=3.8286e+00 | t=0.5878s
    graph_time_tikhonov | MR=1ch | seed=0 | MAE=1.6854e+02 | t=0.1132s
    temporal_laplacian | MR=1ch | seed=0 | MAE=2.8790e+02 | t=16.2036s
    mean | MR=1ch | seed=1 | MAE=1.0242e+01 | t=0.0034s
    nearest | MR=1ch | seed=1 | MAE=1.6572e+01 | t=0.0032s
    tikhonov | MR=1ch | seed=1 | MAE=1.7362e+02 | t=0.0116s
    tv | MR=1ch | seed=1 | MAE=1.0076e+01 | t=0.4596s
    trss | MR=1ch | seed=1 | MAE=3.8017e+00 | t=0.5933s

Completed: 2026-04-16T14:46:41.308346+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.