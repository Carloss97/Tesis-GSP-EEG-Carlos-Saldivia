# Integration Log: scr_01107
Started: 2026-04-16T13:48:57.070540+00:00
Description: Screening scr_01107 ds=bci_iv2a_real_s1 graph=knn miss=[0.1] mode=lambda

## Dataset: bci_iv2a_real_s1 | rows=24
  Graph: knn__k7 built OK
    tv | MR=0.2 | seed=0 | MAE=3.0347e-06 | t=0.6353s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=6.5215e-06 | t=0.0124s
    trss | MR=0.2 | seed=0 | MAE=6.9439e-07 | t=0.7203s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.0892e-05 | t=19.2293s
    tv | MR=0.2 | seed=1 | MAE=3.3724e-06 | t=0.2677s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=6.7159e-06 | t=0.0127s
    trss | MR=0.2 | seed=1 | MAE=8.2497e-07 | t=0.5014s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.1020e-05 | t=12.4357s
    tv | MR=0.2 | seed=0 | MAE=3.0352e-06 | t=0.2662s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=8.2085e-06 | t=0.0123s
    trss | MR=0.2 | seed=0 | MAE=9.3167e-07 | t=0.0427s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.2901e-05 | t=11.9329s

Completed: 2026-04-16T13:48:57.071418+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.