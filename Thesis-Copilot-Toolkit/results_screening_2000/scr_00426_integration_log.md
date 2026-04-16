# Integration Log: scr_00426
Started: 2026-04-16T13:27:01.136673+00:00
Description: Screening scr_00426 ds=iv100hz_mat graph=aew miss=[0.1] mode=base

## Dataset: iv100hz_mat | rows=14
  Graph: aew built OK
    mean | MR=0.1 | seed=0 | MAE=2.0300e+01 | t=0.0020s
    nearest | MR=0.1 | seed=0 | MAE=3.2925e+01 | t=0.0028s
    tikhonov | MR=0.1 | seed=0 | MAE=7.5083e+01 | t=0.0057s
    tv | MR=0.1 | seed=0 | MAE=1.3771e+01 | t=0.2579s
    trss | MR=0.1 | seed=0 | MAE=1.4081e+01 | t=0.1741s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=1.5118e+02 | t=0.0134s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=1.8703e+02 | t=14.7088s
    mean | MR=0.1 | seed=1 | MAE=2.0537e+01 | t=0.0030s
    nearest | MR=0.1 | seed=1 | MAE=3.3573e+01 | t=0.0043s
    tikhonov | MR=0.1 | seed=1 | MAE=7.5800e+01 | t=0.0088s
    tv | MR=0.1 | seed=1 | MAE=1.4473e+01 | t=0.1861s
    trss | MR=0.1 | seed=1 | MAE=1.4898e+01 | t=0.2375s

Completed: 2026-04-16T13:27:01.137786+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.