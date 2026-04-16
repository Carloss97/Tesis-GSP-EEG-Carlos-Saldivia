# Integration Log: scr_01084
Started: 2026-04-16T13:31:19.303726+00:00
Description: Screening scr_01084 ds=bci_iv2a_real_s2 graph=knn miss=[0.1] mode=lambda

## Dataset: bci_iv2a_real_s2 | rows=24
  Graph: knn__k3 built OK
    tv | MR=0.2 | seed=0 | MAE=8.7654e-07 | t=0.5543s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=3.9783e-06 | t=0.0142s
    trss | MR=0.2 | seed=0 | MAE=4.9429e-07 | t=0.0935s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=5.4679e-06 | t=10.8379s
    tv | MR=0.2 | seed=1 | MAE=9.0513e-07 | t=0.1725s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=4.0223e-06 | t=0.0083s
    trss | MR=0.2 | seed=1 | MAE=5.0034e-07 | t=0.0189s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=5.5053e-06 | t=26.4861s
    tv | MR=0.2 | seed=0 | MAE=8.7646e-07 | t=0.1994s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=4.1008e-06 | t=0.0079s
    trss | MR=0.2 | seed=0 | MAE=5.0815e-07 | t=0.0195s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=7.4657e-06 | t=2.5414s

Completed: 2026-04-16T13:31:19.305284+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.