# Integration Log: scr_01182
Started: 2026-04-16T15:14:47.378005+00:00
Description: Screening scr_01182 ds=iv100hz_mat graph=aew miss=[0.1] mode=lambda

## Dataset: iv100hz_mat | rows=24
  Graph: aew built OK
    tv | MR=0.2 | seed=0 | MAE=4.1160e+01 | t=0.1742s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=8.2856e+01 | t=0.0088s
    trss | MR=0.2 | seed=0 | MAE=1.1835e+01 | t=0.0192s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.5703e+02 | t=29.8856s
    tv | MR=0.2 | seed=1 | MAE=4.2591e+01 | t=0.2900s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=8.3817e+01 | t=0.0144s
    trss | MR=0.2 | seed=1 | MAE=1.1805e+01 | t=0.2177s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.5768e+02 | t=19.3006s
    tv | MR=0.2 | seed=0 | MAE=4.0825e+01 | t=0.4595s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.0117e+02 | t=0.0133s
    trss | MR=0.2 | seed=0 | MAE=1.6457e+01 | t=0.2165s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.6285e+02 | t=20.0976s

Completed: 2026-04-16T15:14:47.379801+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.