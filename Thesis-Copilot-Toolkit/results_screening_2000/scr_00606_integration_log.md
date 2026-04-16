# Integration Log: scr_00606
Started: 2026-04-16T14:39:05.332956+00:00
Description: Screening scr_00606 ds=iv100hz_mat graph=kalofolias miss=[0.3] mode=base

## Dataset: iv100hz_mat | rows=14
  Graph: kalofolias built OK
    mean | MR=0.3 | seed=0 | MAE=7.3919e+01 | t=0.0030s
    nearest | MR=0.3 | seed=0 | MAE=1.1253e+02 | t=0.0733s
    tikhonov | MR=0.3 | seed=0 | MAE=1.3651e+02 | t=0.0122s
    tv | MR=0.3 | seed=0 | MAE=7.2421e+01 | t=0.5594s
    trss | MR=0.3 | seed=0 | MAE=3.0813e+01 | t=0.0960s
    graph_time_tikhonov | MR=0.3 | seed=0 | MAE=1.3870e+02 | t=0.0294s
    temporal_laplacian | MR=0.3 | seed=0 | MAE=2.9330e+02 | t=20.7014s
    mean | MR=0.3 | seed=1 | MAE=7.2756e+01 | t=0.0647s
    nearest | MR=0.3 | seed=1 | MAE=1.1224e+02 | t=0.0119s
    tikhonov | MR=0.3 | seed=1 | MAE=1.3809e+02 | t=0.0119s
    tv | MR=0.3 | seed=1 | MAE=7.2030e+01 | t=0.9653s
    trss | MR=0.3 | seed=1 | MAE=2.8936e+01 | t=0.6940s

Completed: 2026-04-16T14:39:05.333908+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.