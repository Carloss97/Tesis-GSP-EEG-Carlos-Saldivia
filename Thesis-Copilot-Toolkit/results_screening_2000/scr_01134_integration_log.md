# Integration Log: scr_01134
Started: 2026-04-16T14:14:09.689742+00:00
Description: Screening scr_01134 ds=iv100hz_mat graph=gaussian miss=[0.1] mode=lambda

## Dataset: iv100hz_mat | rows=24
  Graph: gaussian__sigma0.6 built OK
    tv | MR=0.2 | seed=0 | MAE=3.6157e+01 | t=0.8050s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=9.8821e+01 | t=0.0125s
    trss | MR=0.2 | seed=0 | MAE=1.2237e+01 | t=0.3386s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.6226e+02 | t=17.2825s
    tv | MR=0.2 | seed=1 | MAE=3.3546e+01 | t=0.2042s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=9.8929e+01 | t=0.0085s
    trss | MR=0.2 | seed=1 | MAE=1.2301e+01 | t=0.0207s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.6235e+02 | t=12.3187s
    tv | MR=0.2 | seed=0 | MAE=3.5058e+01 | t=0.6394s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.2394e+02 | t=0.0129s
    trss | MR=0.2 | seed=0 | MAE=1.7275e+01 | t=0.6833s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.7594e+02 | t=24.7703s

Completed: 2026-04-16T14:14:09.691106+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.