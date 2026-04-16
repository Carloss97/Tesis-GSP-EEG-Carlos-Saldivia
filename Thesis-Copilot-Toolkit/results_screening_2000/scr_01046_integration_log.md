# Integration Log: scr_01046
Started: 2026-04-16T13:05:50.895781+00:00
Description: Screening scr_01046 ds=physionet_real graph=knng miss=3ch mode=lambda

## Dataset: physionet_eegmmidb_real | rows=24
  Graph: knng built OK
    tv | MR=0.2 | seed=0 | MAE=5.0492e-06 | t=0.1554s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=6.3236e-06 | t=0.0079s
    trss | MR=0.2 | seed=0 | MAE=1.8066e-06 | t=0.0198s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.6182e-05 | t=5.2329s
    tv | MR=0.2 | seed=1 | MAE=5.0593e-06 | t=0.3139s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=6.2448e-06 | t=0.0083s
    trss | MR=0.2 | seed=1 | MAE=1.8476e-06 | t=0.0572s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.6313e-05 | t=5.0934s
    tv | MR=0.2 | seed=0 | MAE=5.1244e-06 | t=0.2984s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=7.7191e-06 | t=0.0172s
    trss | MR=0.2 | seed=0 | MAE=1.8935e-06 | t=0.0200s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.0082e-05 | t=2.1846s

Completed: 2026-04-16T13:05:50.896563+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.