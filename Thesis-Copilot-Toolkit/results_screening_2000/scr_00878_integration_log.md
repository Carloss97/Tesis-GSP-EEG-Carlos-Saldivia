# Integration Log: scr_00878
Started: 2026-04-16T12:08:19.874852+00:00
Description: Screening scr_00878 ds=physionet_real graph=knn miss=2ch mode=lambda

## Dataset: physionet_eegmmidb_real | rows=24
  Graph: knn__k5 built OK
    tv | MR=0.2 | seed=0 | MAE=5.1032e-06 | t=0.1483s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=6.6501e-06 | t=0.0079s
    trss | MR=0.2 | seed=0 | MAE=1.7786e-06 | t=0.0190s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.7023e-05 | t=3.1958s
    tv | MR=0.2 | seed=1 | MAE=5.1120e-06 | t=0.1544s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=6.5763e-06 | t=0.0078s
    trss | MR=0.2 | seed=1 | MAE=1.8204e-06 | t=0.0184s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.7171e-05 | t=2.8818s
    tv | MR=0.2 | seed=0 | MAE=5.1533e-06 | t=0.1557s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=8.2347e-06 | t=0.0080s
    trss | MR=0.2 | seed=0 | MAE=1.8814e-06 | t=0.0191s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.1365e-05 | t=2.7756s

Completed: 2026-04-16T12:08:19.875717+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.