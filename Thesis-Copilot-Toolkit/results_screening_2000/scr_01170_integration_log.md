# Integration Log: scr_01170
Started: 2026-04-16T14:59:05.918558+00:00
Description: Screening scr_01170 ds=iv100hz_mat graph=vknng miss=[0.1] mode=lambda

## Dataset: iv100hz_mat | rows=24
  Graph: vknng built OK
    tv | MR=0.2 | seed=0 | MAE=4.1430e+01 | t=0.5087s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=8.8718e+01 | t=0.0124s
    trss | MR=0.2 | seed=0 | MAE=1.1850e+01 | t=0.6448s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.5962e+02 | t=18.8039s
    tv | MR=0.2 | seed=1 | MAE=4.4711e+01 | t=0.3933s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=8.9660e+01 | t=0.0140s
    trss | MR=0.2 | seed=1 | MAE=1.2027e+01 | t=0.2073s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.6002e+02 | t=28.8819s
    tv | MR=0.2 | seed=0 | MAE=4.2961e+01 | t=0.3702s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.1012e+02 | t=0.0139s
    trss | MR=0.2 | seed=0 | MAE=1.6673e+01 | t=0.0883s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.6853e+02 | t=20.2988s

Completed: 2026-04-16T14:59:05.919519+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.