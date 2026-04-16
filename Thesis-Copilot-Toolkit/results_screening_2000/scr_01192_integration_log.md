# Integration Log: scr_01192
Started: 2026-04-16T15:27:27.027457+00:00
Description: Screening scr_01192 ds=bci_iv2a_real_s2 graph=knn miss=[0.2] mode=lambda

## Dataset: bci_iv2a_real_s2 | rows=24
  Graph: knn__k3 built OK
    tv | MR=0.2 | seed=0 | MAE=8.7654e-07 | t=1.1035s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=3.9783e-06 | t=0.0136s
    trss | MR=0.2 | seed=0 | MAE=4.9429e-07 | t=0.9890s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=5.4679e-06 | t=17.3764s
    tv | MR=0.2 | seed=1 | MAE=9.0513e-07 | t=0.3827s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=4.0223e-06 | t=0.0162s
    trss | MR=0.2 | seed=1 | MAE=5.0034e-07 | t=0.0682s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=5.5053e-06 | t=13.5257s
    tv | MR=0.2 | seed=0 | MAE=8.7646e-07 | t=0.6258s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=4.1008e-06 | t=0.1226s
    trss | MR=0.2 | seed=0 | MAE=5.0815e-07 | t=0.5030s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=7.4657e-06 | t=14.8757s

Completed: 2026-04-16T15:27:27.029984+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.