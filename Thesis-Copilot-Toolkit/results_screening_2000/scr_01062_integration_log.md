# Integration Log: scr_01062
Started: 2026-04-16T13:14:26.020691+00:00
Description: Screening scr_01062 ds=iv100hz_mat graph=vknng miss=3ch mode=lambda

## Dataset: iv100hz_mat | rows=24
  Graph: vknng built OK
    tv | MR=0.2 | seed=0 | MAE=4.1430e+01 | t=0.6549s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=8.8718e+01 | t=0.0753s
    trss | MR=0.2 | seed=0 | MAE=1.1850e+01 | t=0.1977s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.5962e+02 | t=5.8623s
    tv | MR=0.2 | seed=1 | MAE=4.4711e+01 | t=0.3574s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=8.9660e+01 | t=0.0125s
    trss | MR=0.2 | seed=1 | MAE=1.2027e+01 | t=0.2244s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.6002e+02 | t=11.7540s
    tv | MR=0.2 | seed=0 | MAE=4.2961e+01 | t=0.1573s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.1012e+02 | t=0.0106s
    trss | MR=0.2 | seed=0 | MAE=1.6673e+01 | t=0.0200s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.6853e+02 | t=21.1245s

Completed: 2026-04-16T13:14:26.021539+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.