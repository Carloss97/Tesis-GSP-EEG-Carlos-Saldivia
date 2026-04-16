# Integration Log: scr_01026
Started: 2026-04-16T12:59:34.050067+00:00
Description: Screening scr_01026 ds=iv100hz_mat graph=gaussian miss=3ch mode=lambda

## Dataset: iv100hz_mat | rows=24
  Graph: gaussian__sigma0.6 built OK
    tv | MR=0.2 | seed=0 | MAE=3.6157e+01 | t=0.1970s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=9.8821e+01 | t=0.0079s
    trss | MR=0.2 | seed=0 | MAE=1.2237e+01 | t=0.0209s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.6226e+02 | t=8.2501s
    tv | MR=0.2 | seed=1 | MAE=3.3546e+01 | t=0.1973s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=9.8929e+01 | t=0.0081s
    trss | MR=0.2 | seed=1 | MAE=1.2301e+01 | t=0.0196s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.6235e+02 | t=8.9722s
    tv | MR=0.2 | seed=0 | MAE=3.5058e+01 | t=0.1962s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.2394e+02 | t=0.0109s
    trss | MR=0.2 | seed=0 | MAE=1.7275e+01 | t=0.0197s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.7594e+02 | t=3.6698s

Completed: 2026-04-16T12:59:34.050945+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.