# Integration Log: scr_00770
Started: 2026-04-16T11:54:26.902740+00:00
Description: Screening scr_00770 ds=physionet_real graph=knn miss=1ch mode=lambda

## Dataset: physionet_eegmmidb_real | rows=24
  Graph: knn__k5 built OK
    tv | MR=0.2 | seed=0 | MAE=5.1032e-06 | t=0.1571s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=6.6501e-06 | t=0.0147s
    trss | MR=0.2 | seed=0 | MAE=1.7786e-06 | t=0.0197s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.7023e-05 | t=2.7113s
    tv | MR=0.2 | seed=1 | MAE=5.1120e-06 | t=0.1899s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=6.5763e-06 | t=0.0078s
    trss | MR=0.2 | seed=1 | MAE=1.8204e-06 | t=0.0196s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.7171e-05 | t=2.6241s
    tv | MR=0.2 | seed=0 | MAE=5.1533e-06 | t=0.1471s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=8.2347e-06 | t=0.0081s
    trss | MR=0.2 | seed=0 | MAE=1.8814e-06 | t=0.0200s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.1365e-05 | t=3.0495s

Completed: 2026-04-16T11:54:26.903592+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.