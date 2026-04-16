# Integration Log: scr_00738
Started: 2026-04-16T11:51:46.595821+00:00
Description: Screening scr_00738 ds=iv100hz_mat graph=vknng miss=[0.4] mode=base

## Dataset: iv100hz_mat | rows=14
  Graph: vknng built OK
    mean | MR=0.4 | seed=0 | MAE=1.0557e+02 | t=0.0020s
    nearest | MR=0.4 | seed=0 | MAE=1.5725e+02 | t=0.0085s
    tikhonov | MR=0.4 | seed=0 | MAE=1.5280e+02 | t=0.0057s
    tv | MR=0.4 | seed=0 | MAE=1.2052e+02 | t=0.1437s
    trss | MR=0.4 | seed=0 | MAE=9.3616e+01 | t=0.0202s
    graph_time_tikhonov | MR=0.4 | seed=0 | MAE=1.9583e+02 | t=0.0079s
    temporal_laplacian | MR=0.4 | seed=0 | MAE=2.2852e+02 | t=1.3107s
    mean | MR=0.4 | seed=1 | MAE=1.0515e+02 | t=0.0020s
    nearest | MR=0.4 | seed=1 | MAE=1.5788e+02 | t=0.0086s
    tikhonov | MR=0.4 | seed=1 | MAE=1.5416e+02 | t=0.0057s
    tv | MR=0.4 | seed=1 | MAE=9.7965e+01 | t=0.1432s
    trss | MR=0.4 | seed=1 | MAE=9.3615e+01 | t=0.0205s

Completed: 2026-04-16T11:51:46.596656+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.