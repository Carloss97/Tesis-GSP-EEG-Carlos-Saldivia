# Integration Log: scr_00999
Started: 2026-04-16T12:49:01.601750+00:00
Description: Screening scr_00999 ds=bci_iv2a_real_s1 graph=knn miss=3ch mode=lambda

## Dataset: bci_iv2a_real_s1 | rows=24
  Graph: knn__k7 built OK
    tv | MR=0.2 | seed=0 | MAE=3.0347e-06 | t=0.3821s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=6.5215e-06 | t=0.0138s
    trss | MR=0.2 | seed=0 | MAE=6.9439e-07 | t=0.0956s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.0892e-05 | t=2.2837s
    tv | MR=0.2 | seed=1 | MAE=3.3724e-06 | t=0.1720s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=6.7159e-06 | t=0.0121s
    trss | MR=0.2 | seed=1 | MAE=8.2497e-07 | t=0.0965s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.1020e-05 | t=2.1667s
    tv | MR=0.2 | seed=0 | MAE=3.0352e-06 | t=0.1817s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=8.2085e-06 | t=0.0082s
    trss | MR=0.2 | seed=0 | MAE=9.3167e-07 | t=0.0205s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.2901e-05 | t=4.6348s

Completed: 2026-04-16T12:49:01.602471+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.