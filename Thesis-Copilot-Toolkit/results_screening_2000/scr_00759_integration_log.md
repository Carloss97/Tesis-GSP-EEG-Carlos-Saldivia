# Integration Log: scr_00759
Started: 2026-04-16T11:53:07.290788+00:00
Description: Screening scr_00759 ds=bci_iv2a_real_s1 graph=knn miss=1ch mode=lambda

## Dataset: bci_iv2a_real_s1 | rows=24
  Graph: knn__k3 built OK
    tv | MR=0.2 | seed=0 | MAE=3.0347e-06 | t=0.1468s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=5.0523e-06 | t=0.0078s
    trss | MR=0.2 | seed=0 | MAE=8.1913e-07 | t=0.0194s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=9.2028e-06 | t=1.3119s
    tv | MR=0.2 | seed=1 | MAE=3.3724e-06 | t=0.1449s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=5.3176e-06 | t=0.0077s
    trss | MR=0.2 | seed=1 | MAE=1.0218e-06 | t=0.0187s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=9.3894e-06 | t=1.3298s
    tv | MR=0.2 | seed=0 | MAE=3.0352e-06 | t=0.1470s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=6.1521e-06 | t=0.0078s
    trss | MR=0.2 | seed=0 | MAE=1.0348e-06 | t=0.0183s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.0450e-05 | t=1.2436s

Completed: 2026-04-16T11:53:07.291641+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.