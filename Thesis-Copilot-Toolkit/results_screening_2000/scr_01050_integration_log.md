# Integration Log: scr_01050
Started: 2026-04-16T13:08:41.164694+00:00
Description: Screening scr_01050 ds=iv100hz_mat graph=knng miss=3ch mode=lambda

## Dataset: iv100hz_mat | rows=24
  Graph: knng built OK
    tv | MR=0.2 | seed=0 | MAE=4.2210e+01 | t=0.2552s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=8.7632e+01 | t=0.0223s
    trss | MR=0.2 | seed=0 | MAE=1.1947e+01 | t=0.1188s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.5907e+02 | t=4.8126s
    tv | MR=0.2 | seed=1 | MAE=4.2807e+01 | t=0.1468s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=8.8637e+01 | t=0.0082s
    trss | MR=0.2 | seed=1 | MAE=1.2085e+01 | t=0.0183s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.5951e+02 | t=11.9843s
    tv | MR=0.2 | seed=0 | MAE=4.0004e+01 | t=0.2159s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.0821e+02 | t=0.0081s
    trss | MR=0.2 | seed=0 | MAE=1.6798e+01 | t=0.0190s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.6734e+02 | t=6.1912s

Completed: 2026-04-16T13:08:41.165563+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.