# Integration Log: scr_00760
Started: 2026-04-16T11:53:20.722544+00:00
Description: Screening scr_00760 ds=bci_iv2a_real_s2 graph=knn miss=1ch mode=lambda

## Dataset: bci_iv2a_real_s2 | rows=24
  Graph: knn__k3 built OK
    tv | MR=0.2 | seed=0 | MAE=8.7654e-07 | t=0.1455s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=3.9783e-06 | t=0.0080s
    trss | MR=0.2 | seed=0 | MAE=4.9429e-07 | t=0.0195s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=5.4679e-06 | t=2.2130s
    tv | MR=0.2 | seed=1 | MAE=9.0513e-07 | t=0.1473s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=4.0223e-06 | t=0.0079s
    trss | MR=0.2 | seed=1 | MAE=5.0034e-07 | t=0.0188s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=5.5053e-06 | t=1.3559s
    tv | MR=0.2 | seed=0 | MAE=8.7646e-07 | t=0.1671s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=4.1008e-06 | t=0.0079s
    trss | MR=0.2 | seed=0 | MAE=5.0815e-07 | t=0.0191s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=7.4657e-06 | t=1.2559s

Completed: 2026-04-16T11:53:20.723369+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.