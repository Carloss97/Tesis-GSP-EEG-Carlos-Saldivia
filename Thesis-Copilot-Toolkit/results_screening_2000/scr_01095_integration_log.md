# Integration Log: scr_01095
Started: 2026-04-16T13:38:50.169769+00:00
Description: Screening scr_01095 ds=bci_iv2a_real_s1 graph=knn miss=[0.1] mode=lambda

## Dataset: bci_iv2a_real_s1 | rows=24
  Graph: knn__k5 built OK
    tv | MR=0.2 | seed=0 | MAE=3.0348e-06 | t=0.4611s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=5.8873e-06 | t=0.0518s
    trss | MR=0.2 | seed=0 | MAE=7.3001e-07 | t=0.1265s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.0259e-05 | t=15.5713s
    tv | MR=0.2 | seed=1 | MAE=3.3726e-06 | t=0.1603s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=6.1319e-06 | t=0.0088s
    trss | MR=0.2 | seed=1 | MAE=8.7337e-07 | t=0.2472s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.0411e-05 | t=11.5358s
    tv | MR=0.2 | seed=0 | MAE=3.0353e-06 | t=0.3177s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=7.3590e-06 | t=0.0083s
    trss | MR=0.2 | seed=0 | MAE=9.7299e-07 | t=0.0188s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.1963e-05 | t=9.4124s

Completed: 2026-04-16T13:38:50.170638+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.