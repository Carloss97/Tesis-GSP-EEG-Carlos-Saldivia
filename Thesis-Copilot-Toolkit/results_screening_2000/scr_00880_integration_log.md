# Integration Log: scr_00880
Started: 2026-04-16T12:08:45.520597+00:00
Description: Screening scr_00880 ds=bci_iv2a_real_s2 graph=knn miss=2ch mode=lambda

## Dataset: bci_iv2a_real_s2 | rows=24
  Graph: knn__k5 built OK
    tv | MR=0.2 | seed=0 | MAE=8.7659e-07 | t=0.1530s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=4.0635e-06 | t=0.0078s
    trss | MR=0.2 | seed=0 | MAE=4.2026e-07 | t=0.0198s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=7.0377e-06 | t=1.2641s
    tv | MR=0.2 | seed=1 | MAE=9.0517e-07 | t=0.1517s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=4.1013e-06 | t=0.0079s
    trss | MR=0.2 | seed=1 | MAE=4.2224e-07 | t=0.0184s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=7.0696e-06 | t=1.2883s
    tv | MR=0.2 | seed=0 | MAE=8.7649e-07 | t=0.1547s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=4.2613e-06 | t=0.0080s
    trss | MR=0.2 | seed=0 | MAE=4.5962e-07 | t=0.0187s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=9.4732e-06 | t=1.3515s

Completed: 2026-04-16T12:08:45.521452+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.