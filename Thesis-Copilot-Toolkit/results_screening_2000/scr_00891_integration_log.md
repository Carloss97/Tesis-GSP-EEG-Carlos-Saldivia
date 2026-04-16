# Integration Log: scr_00891
Started: 2026-04-16T12:10:02.922507+00:00
Description: Screening scr_00891 ds=bci_iv2a_real_s1 graph=knn miss=2ch mode=lambda

## Dataset: bci_iv2a_real_s1 | rows=24
  Graph: knn__k7 built OK
    tv | MR=0.2 | seed=0 | MAE=3.0347e-06 | t=0.1617s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=6.5215e-06 | t=0.0081s
    trss | MR=0.2 | seed=0 | MAE=6.9439e-07 | t=0.0187s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.0892e-05 | t=1.3427s
    tv | MR=0.2 | seed=1 | MAE=3.3724e-06 | t=0.1617s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=6.7159e-06 | t=0.0080s
    trss | MR=0.2 | seed=1 | MAE=8.2497e-07 | t=0.0194s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.1020e-05 | t=1.2763s
    tv | MR=0.2 | seed=0 | MAE=3.0352e-06 | t=0.1600s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=8.2085e-06 | t=0.0080s
    trss | MR=0.2 | seed=0 | MAE=9.3167e-07 | t=0.0196s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.2901e-05 | t=1.2954s

Completed: 2026-04-16T12:10:02.923343+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.