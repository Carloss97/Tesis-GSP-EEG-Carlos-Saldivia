# Integration Log: scr_00378
Started: 2026-04-16T13:11:51.310566+00:00
Description: Screening scr_00378 ds=iv100hz_mat graph=gaussian miss=[0.1] mode=base

## Dataset: iv100hz_mat | rows=14
  Graph: gaussian__sigma0.6 built OK
    mean | MR=0.1 | seed=0 | MAE=2.0300e+01 | t=0.0035s
    nearest | MR=0.1 | seed=0 | MAE=3.2925e+01 | t=0.0044s
    tikhonov | MR=0.1 | seed=0 | MAE=1.0148e+02 | t=0.0244s
    tv | MR=0.1 | seed=0 | MAE=1.2289e+01 | t=0.1980s
    trss | MR=0.1 | seed=0 | MAE=1.4800e+01 | t=0.0170s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=1.8172e+02 | t=0.0079s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=2.2467e+02 | t=19.0222s
    mean | MR=0.1 | seed=1 | MAE=2.0537e+01 | t=0.0030s
    nearest | MR=0.1 | seed=1 | MAE=3.3573e+01 | t=0.0092s
    tikhonov | MR=0.1 | seed=1 | MAE=1.0174e+02 | t=0.0130s
    tv | MR=0.1 | seed=1 | MAE=1.2851e+01 | t=0.4221s
    trss | MR=0.1 | seed=1 | MAE=1.5152e+01 | t=0.3196s

Completed: 2026-04-16T13:11:51.311470+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.