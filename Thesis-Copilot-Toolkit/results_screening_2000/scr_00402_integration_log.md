# Integration Log: scr_00402
Started: 2026-04-16T13:19:02.100968+00:00
Description: Screening scr_00402 ds=iv100hz_mat graph=knng miss=[0.1] mode=base

## Dataset: iv100hz_mat | rows=14
  Graph: knng built OK
    mean | MR=0.1 | seed=0 | MAE=2.0300e+01 | t=0.0207s
    nearest | MR=0.1 | seed=0 | MAE=3.2925e+01 | t=0.0042s
    tikhonov | MR=0.1 | seed=0 | MAE=8.2912e+01 | t=0.0520s
    tv | MR=0.1 | seed=0 | MAE=1.3573e+01 | t=0.5173s
    trss | MR=0.1 | seed=0 | MAE=1.4332e+01 | t=0.1000s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=1.6135e+02 | t=0.0179s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=1.9837e+02 | t=19.4359s
    mean | MR=0.1 | seed=1 | MAE=2.0537e+01 | t=0.0030s
    nearest | MR=0.1 | seed=1 | MAE=3.3573e+01 | t=0.0043s
    tikhonov | MR=0.1 | seed=1 | MAE=8.3459e+01 | t=0.0085s
    tv | MR=0.1 | seed=1 | MAE=1.5122e+01 | t=0.4209s
    trss | MR=0.1 | seed=1 | MAE=1.5023e+01 | t=0.3045s

Completed: 2026-04-16T13:19:02.101695+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.