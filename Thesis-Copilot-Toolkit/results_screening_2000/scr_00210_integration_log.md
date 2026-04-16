# Integration Log: scr_00210
Started: 2026-04-16T14:33:40.285941+00:00
Description: Screening scr_00210 ds=iv100hz_mat graph=aew miss=2ch mode=base

## Dataset: iv100hz_mat | rows=14
  Graph: aew built OK
    mean | MR=2ch | seed=0 | MAE=2.0300e+01 | t=0.0724s
    nearest | MR=2ch | seed=0 | MAE=3.2925e+01 | t=0.0044s
    tikhonov | MR=2ch | seed=0 | MAE=7.5083e+01 | t=0.0142s
    tv | MR=2ch | seed=0 | MAE=1.3771e+01 | t=0.8919s
    trss | MR=2ch | seed=0 | MAE=1.4081e+01 | t=0.4401s
    graph_time_tikhonov | MR=2ch | seed=0 | MAE=1.5118e+02 | t=0.2366s
    temporal_laplacian | MR=2ch | seed=0 | MAE=1.8703e+02 | t=19.8627s
    mean | MR=2ch | seed=1 | MAE=2.0537e+01 | t=0.0020s
    nearest | MR=2ch | seed=1 | MAE=3.3573e+01 | t=0.0088s
    tikhonov | MR=2ch | seed=1 | MAE=7.5800e+01 | t=0.0095s
    tv | MR=2ch | seed=1 | MAE=1.4473e+01 | t=0.4943s
    trss | MR=2ch | seed=1 | MAE=1.4898e+01 | t=0.4252s

Completed: 2026-04-16T14:33:40.286677+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.