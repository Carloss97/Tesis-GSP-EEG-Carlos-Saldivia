# Integration Log: scr_00975
Started: 2026-04-16T12:40:24.216886+00:00
Description: Screening scr_00975 ds=bci_iv2a_real_s1 graph=knn miss=3ch mode=lambda

## Dataset: bci_iv2a_real_s1 | rows=24
  Graph: knn__k3 built OK
    tv | MR=0.2 | seed=0 | MAE=3.0347e-06 | t=0.3263s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=5.0523e-06 | t=0.0302s
    trss | MR=0.2 | seed=0 | MAE=8.1913e-07 | t=0.1828s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=9.2028e-06 | t=5.9077s
    tv | MR=0.2 | seed=1 | MAE=3.3724e-06 | t=0.3047s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=5.3176e-06 | t=0.0238s
    trss | MR=0.2 | seed=1 | MAE=1.0218e-06 | t=0.0747s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=9.3894e-06 | t=5.5120s
    tv | MR=0.2 | seed=0 | MAE=3.0352e-06 | t=0.1608s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=6.1521e-06 | t=0.0079s
    trss | MR=0.2 | seed=0 | MAE=1.0348e-06 | t=0.0197s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.0450e-05 | t=2.0835s

Completed: 2026-04-16T12:40:24.217746+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.