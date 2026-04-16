# Integration Log: scr_00976
Started: 2026-04-16T12:41:03.422335+00:00
Description: Screening scr_00976 ds=bci_iv2a_real_s2 graph=knn miss=3ch mode=lambda

## Dataset: bci_iv2a_real_s2 | rows=24
  Graph: knn__k3 built OK
    tv | MR=0.2 | seed=0 | MAE=8.7654e-07 | t=0.1569s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=3.9783e-06 | t=0.0088s
    trss | MR=0.2 | seed=0 | MAE=4.9429e-07 | t=0.0196s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=5.4679e-06 | t=4.9103s
    tv | MR=0.2 | seed=1 | MAE=9.0513e-07 | t=0.2474s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=4.0223e-06 | t=0.0097s
    trss | MR=0.2 | seed=1 | MAE=5.0034e-07 | t=0.0201s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=5.5053e-06 | t=2.1189s
    tv | MR=0.2 | seed=0 | MAE=8.7646e-07 | t=0.1491s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=4.1008e-06 | t=0.0084s
    trss | MR=0.2 | seed=0 | MAE=5.0815e-07 | t=0.0191s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=7.4657e-06 | t=10.9271s

Completed: 2026-04-16T12:41:03.423236+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.