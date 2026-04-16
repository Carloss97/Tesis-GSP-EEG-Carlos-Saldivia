# Integration Log: scr_00918
Started: 2026-04-16T12:20:29.616527+00:00
Description: Screening scr_00918 ds=iv100hz_mat graph=gaussian miss=2ch mode=lambda

## Dataset: iv100hz_mat | rows=24
  Graph: gaussian__sigma0.6 built OK
    tv | MR=0.2 | seed=0 | MAE=3.6157e+01 | t=0.3516s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=9.8821e+01 | t=0.0126s
    trss | MR=0.2 | seed=0 | MAE=1.2237e+01 | t=0.1082s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.6226e+02 | t=2.7190s
    tv | MR=0.2 | seed=1 | MAE=3.3546e+01 | t=0.1935s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=9.8929e+01 | t=0.0080s
    trss | MR=0.2 | seed=1 | MAE=1.2301e+01 | t=0.0183s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.6235e+02 | t=11.9738s
    tv | MR=0.2 | seed=0 | MAE=3.5058e+01 | t=0.3859s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.2394e+02 | t=0.0569s
    trss | MR=0.2 | seed=0 | MAE=1.7275e+01 | t=0.0256s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.7594e+02 | t=6.1856s

Completed: 2026-04-16T12:20:29.617422+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.