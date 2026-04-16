# Integration Log: scr_01203
Started: 2026-04-16T15:40:52.415674+00:00
Description: Screening scr_01203 ds=bci_iv2a_real_s1 graph=knn miss=[0.2] mode=lambda

## Dataset: bci_iv2a_real_s1 | rows=24
  Graph: knn__k5 built OK
    tv | MR=0.2 | seed=0 | MAE=3.0348e-06 | t=1.1228s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=5.8873e-06 | t=0.0157s
    trss | MR=0.2 | seed=0 | MAE=7.3001e-07 | t=0.1099s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.0259e-05 | t=11.9265s
    tv | MR=0.2 | seed=1 | MAE=3.3726e-06 | t=0.3979s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=6.1319e-06 | t=0.0168s
    trss | MR=0.2 | seed=1 | MAE=8.7337e-07 | t=0.5008s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.0411e-05 | t=21.7617s
    tv | MR=0.2 | seed=0 | MAE=3.0353e-06 | t=0.9336s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=7.3590e-06 | t=0.0350s
    trss | MR=0.2 | seed=0 | MAE=9.7299e-07 | t=0.2412s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.1963e-05 | t=25.0034s

Completed: 2026-04-16T15:40:52.420949+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.