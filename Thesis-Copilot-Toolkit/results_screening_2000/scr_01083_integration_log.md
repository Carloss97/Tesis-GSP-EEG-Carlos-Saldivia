# Integration Log: scr_01083
Started: 2026-04-16T13:29:38.106936+00:00
Description: Screening scr_01083 ds=bci_iv2a_real_s1 graph=knn miss=[0.1] mode=lambda

## Dataset: bci_iv2a_real_s1 | rows=24
  Graph: knn__k3 built OK
    tv | MR=0.2 | seed=0 | MAE=3.0347e-06 | t=0.1528s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=5.0523e-06 | t=0.0087s
    trss | MR=0.2 | seed=0 | MAE=8.1913e-07 | t=0.0200s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=9.2028e-06 | t=16.3211s
    tv | MR=0.2 | seed=1 | MAE=3.3724e-06 | t=0.1514s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=5.3176e-06 | t=0.0080s
    trss | MR=0.2 | seed=1 | MAE=1.0218e-06 | t=0.0184s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=9.3894e-06 | t=23.7828s
    tv | MR=0.2 | seed=0 | MAE=3.0352e-06 | t=0.1539s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=6.1521e-06 | t=0.0079s
    trss | MR=0.2 | seed=0 | MAE=1.0348e-06 | t=0.0205s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.0450e-05 | t=2.8773s

Completed: 2026-04-16T13:29:38.107700+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.