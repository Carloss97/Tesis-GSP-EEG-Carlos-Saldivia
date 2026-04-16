# Integration Log: scr_01000
Started: 2026-04-16T12:49:43.630070+00:00
Description: Screening scr_01000 ds=bci_iv2a_real_s2 graph=knn miss=3ch mode=lambda

## Dataset: bci_iv2a_real_s2 | rows=24
  Graph: knn__k7 built OK
    tv | MR=0.2 | seed=0 | MAE=8.7656e-07 | t=0.2928s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=4.1567e-06 | t=0.0172s
    trss | MR=0.2 | seed=0 | MAE=4.0514e-07 | t=0.0817s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=8.3842e-06 | t=2.4714s
    tv | MR=0.2 | seed=1 | MAE=9.0517e-07 | t=0.1669s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=4.1961e-06 | t=0.0081s
    trss | MR=0.2 | seed=1 | MAE=4.1073e-07 | t=0.0199s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=8.4067e-06 | t=4.9485s
    tv | MR=0.2 | seed=0 | MAE=8.7647e-07 | t=0.3158s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=4.4054e-06 | t=0.0208s
    trss | MR=0.2 | seed=0 | MAE=4.5066e-07 | t=0.2330s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.0963e-05 | t=4.4906s

Completed: 2026-04-16T12:49:43.630948+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.