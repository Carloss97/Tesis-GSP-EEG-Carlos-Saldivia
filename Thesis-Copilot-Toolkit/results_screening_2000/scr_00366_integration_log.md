# Integration Log: scr_00366
Started: 2026-04-16T13:09:35.895962+00:00
Description: Screening scr_00366 ds=iv100hz_mat graph=gaussian miss=[0.1] mode=base

## Dataset: iv100hz_mat | rows=14
  Graph: gaussian__sigma1.0 built OK
    mean | MR=0.1 | seed=0 | MAE=2.0300e+01 | t=0.0020s
    nearest | MR=0.1 | seed=0 | MAE=3.2925e+01 | t=0.0027s
    tikhonov | MR=0.1 | seed=0 | MAE=1.3433e+02 | t=0.0057s
    tv | MR=0.1 | seed=0 | MAE=1.1939e+01 | t=0.1894s
    trss | MR=0.1 | seed=0 | MAE=1.3969e+01 | t=0.0167s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=2.0474e+02 | t=0.0142s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=2.6591e+02 | t=7.3119s
    mean | MR=0.1 | seed=1 | MAE=2.0537e+01 | t=0.0020s
    nearest | MR=0.1 | seed=1 | MAE=3.3573e+01 | t=0.0027s
    tikhonov | MR=0.1 | seed=1 | MAE=1.3439e+02 | t=0.0060s
    tv | MR=0.1 | seed=1 | MAE=1.2631e+01 | t=0.1916s
    trss | MR=0.1 | seed=1 | MAE=1.4213e+01 | t=0.0181s

Completed: 2026-04-16T13:09:35.896719+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.