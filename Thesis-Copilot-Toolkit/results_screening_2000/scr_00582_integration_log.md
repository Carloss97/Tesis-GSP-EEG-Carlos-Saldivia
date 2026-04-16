# Integration Log: scr_00582
Started: 2026-04-16T14:27:14.939660+00:00
Description: Screening scr_00582 ds=iv100hz_mat graph=gaussian miss=[0.3] mode=base

## Dataset: iv100hz_mat | rows=14
  Graph: gaussian__sigma1.0 built OK
    mean | MR=0.3 | seed=0 | MAE=7.3919e+01 | t=0.0038s
    nearest | MR=0.3 | seed=0 | MAE=1.1253e+02 | t=0.0101s
    tikhonov | MR=0.3 | seed=0 | MAE=1.6076e+02 | t=0.0086s
    tv | MR=0.3 | seed=0 | MAE=5.2130e+01 | t=0.8664s
    trss | MR=0.3 | seed=0 | MAE=5.6649e+01 | t=0.2373s
    graph_time_tikhonov | MR=0.3 | seed=0 | MAE=2.1375e+02 | t=0.0169s
    temporal_laplacian | MR=0.3 | seed=0 | MAE=2.7906e+02 | t=15.5386s
    mean | MR=0.3 | seed=1 | MAE=7.2756e+01 | t=0.0360s
    nearest | MR=0.3 | seed=1 | MAE=1.1224e+02 | t=0.0101s
    tikhonov | MR=0.3 | seed=1 | MAE=1.6051e+02 | t=0.0751s
    tv | MR=0.3 | seed=1 | MAE=4.9881e+01 | t=0.9043s
    trss | MR=0.3 | seed=1 | MAE=5.5154e+01 | t=0.7231s

Completed: 2026-04-16T14:27:14.940667+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.