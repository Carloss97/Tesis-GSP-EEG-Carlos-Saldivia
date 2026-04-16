# Integration Log: scr_00892
Started: 2026-04-16T12:10:30.150416+00:00
Description: Screening scr_00892 ds=bci_iv2a_real_s2 graph=knn miss=2ch mode=lambda

## Dataset: bci_iv2a_real_s2 | rows=24
  Graph: knn__k7 built OK
    tv | MR=0.2 | seed=0 | MAE=8.7656e-07 | t=0.1631s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=4.1567e-06 | t=0.0088s
    trss | MR=0.2 | seed=0 | MAE=4.0514e-07 | t=0.0188s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=8.3842e-06 | t=1.3804s
    tv | MR=0.2 | seed=1 | MAE=9.0517e-07 | t=0.1596s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=4.1961e-06 | t=0.0078s
    trss | MR=0.2 | seed=1 | MAE=4.1073e-07 | t=0.0191s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=8.4067e-06 | t=1.2769s
    tv | MR=0.2 | seed=0 | MAE=8.7647e-07 | t=0.1631s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=4.4054e-06 | t=0.0078s
    trss | MR=0.2 | seed=0 | MAE=4.5066e-07 | t=0.0190s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.0963e-05 | t=1.4904s

Completed: 2026-04-16T12:10:30.151135+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.