# Integration Log: scr_01191
Started: 2026-04-16T15:25:11.334703+00:00
Description: Screening scr_01191 ds=bci_iv2a_real_s1 graph=knn miss=[0.2] mode=lambda

## Dataset: bci_iv2a_real_s1 | rows=24
  Graph: knn__k3 built OK
    tv | MR=0.2 | seed=0 | MAE=3.0347e-06 | t=1.0026s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=5.0523e-06 | t=0.0530s
    trss | MR=0.2 | seed=0 | MAE=8.1913e-07 | t=0.0932s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=9.2028e-06 | t=28.9971s
    tv | MR=0.2 | seed=1 | MAE=3.3724e-06 | t=1.6073s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=5.3176e-06 | t=0.1002s
    trss | MR=0.2 | seed=1 | MAE=1.0218e-06 | t=0.6011s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=9.3894e-06 | t=22.9744s
    tv | MR=0.2 | seed=0 | MAE=3.0352e-06 | t=0.5346s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=6.1521e-06 | t=0.1087s
    trss | MR=0.2 | seed=0 | MAE=1.0348e-06 | t=1.3043s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.0450e-05 | t=18.9335s

Completed: 2026-04-16T15:25:11.335618+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.