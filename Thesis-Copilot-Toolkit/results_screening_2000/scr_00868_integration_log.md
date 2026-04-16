# Integration Log: scr_00868
Started: 2026-04-16T12:07:14.711583+00:00
Description: Screening scr_00868 ds=bci_iv2a_real_s2 graph=knn miss=2ch mode=lambda

## Dataset: bci_iv2a_real_s2 | rows=24
  Graph: knn__k3 built OK
    tv | MR=0.2 | seed=0 | MAE=8.7654e-07 | t=0.1469s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=3.9783e-06 | t=0.0079s
    trss | MR=0.2 | seed=0 | MAE=4.9429e-07 | t=0.0188s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=5.4679e-06 | t=1.3235s
    tv | MR=0.2 | seed=1 | MAE=9.0513e-07 | t=0.1661s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=4.0223e-06 | t=0.0088s
    trss | MR=0.2 | seed=1 | MAE=5.0034e-07 | t=0.0190s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=5.5053e-06 | t=1.3934s
    tv | MR=0.2 | seed=0 | MAE=8.7646e-07 | t=0.1468s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=4.1008e-06 | t=0.0078s
    trss | MR=0.2 | seed=0 | MAE=5.0815e-07 | t=0.0204s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=7.4657e-06 | t=1.2653s

Completed: 2026-04-16T12:07:14.712435+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.