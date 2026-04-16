# Integration Log: scr_00594
Started: 2026-04-16T14:33:11.627517+00:00
Description: Screening scr_00594 ds=iv100hz_mat graph=gaussian miss=[0.3] mode=base

## Dataset: iv100hz_mat | rows=14
  Graph: gaussian__sigma0.6 built OK
    mean | MR=0.3 | seed=0 | MAE=7.3919e+01 | t=0.0020s
    nearest | MR=0.3 | seed=0 | MAE=1.1253e+02 | t=0.0143s
    tikhonov | MR=0.3 | seed=0 | MAE=1.3785e+02 | t=0.0058s
    tv | MR=0.3 | seed=0 | MAE=5.3417e+01 | t=0.2136s
    trss | MR=0.3 | seed=0 | MAE=6.0541e+01 | t=0.5590s
    graph_time_tikhonov | MR=0.3 | seed=0 | MAE=1.9641e+02 | t=0.0456s
    temporal_laplacian | MR=0.3 | seed=0 | MAE=2.4428e+02 | t=22.2647s
    mean | MR=0.3 | seed=1 | MAE=7.2756e+01 | t=0.0031s
    nearest | MR=0.3 | seed=1 | MAE=1.1224e+02 | t=0.0102s
    tikhonov | MR=0.3 | seed=1 | MAE=1.3761e+02 | t=0.0152s
    tv | MR=0.3 | seed=1 | MAE=5.0594e+01 | t=0.4125s
    trss | MR=0.3 | seed=1 | MAE=5.9011e+01 | t=0.2371s

Completed: 2026-04-16T14:33:11.628372+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.