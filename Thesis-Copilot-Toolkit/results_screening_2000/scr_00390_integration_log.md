# Integration Log: scr_00390
Started: 2026-04-16T13:15:06.967223+00:00
Description: Screening scr_00390 ds=iv100hz_mat graph=kalofolias miss=[0.1] mode=base

## Dataset: iv100hz_mat | rows=14
  Graph: kalofolias built OK
    mean | MR=0.1 | seed=0 | MAE=2.0300e+01 | t=0.0030s
    nearest | MR=0.1 | seed=0 | MAE=3.2925e+01 | t=0.0359s
    tikhonov | MR=0.1 | seed=0 | MAE=1.6141e+02 | t=0.0281s
    tv | MR=0.1 | seed=0 | MAE=1.9663e+01 | t=0.5713s
    trss | MR=0.1 | seed=0 | MAE=7.4870e+00 | t=0.4939s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=1.6315e+02 | t=0.0200s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=2.8863e+02 | t=16.7475s
    mean | MR=0.1 | seed=1 | MAE=2.0537e+01 | t=0.0657s
    nearest | MR=0.1 | seed=1 | MAE=3.3573e+01 | t=0.0058s
    tikhonov | MR=0.1 | seed=1 | MAE=1.6248e+02 | t=0.0128s
    tv | MR=0.1 | seed=1 | MAE=2.0234e+01 | t=0.3823s
    trss | MR=0.1 | seed=1 | MAE=7.6641e+00 | t=0.0163s

Completed: 2026-04-16T13:15:06.967908+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.