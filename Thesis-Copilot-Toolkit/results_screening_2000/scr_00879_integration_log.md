# Integration Log: scr_00879
Started: 2026-04-16T12:08:33.174577+00:00
Description: Screening scr_00879 ds=bci_iv2a_real_s1 graph=knn miss=2ch mode=lambda

## Dataset: bci_iv2a_real_s1 | rows=24
  Graph: knn__k5 built OK
    tv | MR=0.2 | seed=0 | MAE=3.0348e-06 | t=0.1862s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=5.8873e-06 | t=0.0080s
    trss | MR=0.2 | seed=0 | MAE=7.3001e-07 | t=0.0181s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.0259e-05 | t=1.3126s
    tv | MR=0.2 | seed=1 | MAE=3.3726e-06 | t=0.1517s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=6.1319e-06 | t=0.0080s
    trss | MR=0.2 | seed=1 | MAE=8.7337e-07 | t=0.0188s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.0411e-05 | t=1.7149s
    tv | MR=0.2 | seed=0 | MAE=3.0353e-06 | t=0.1552s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=7.3590e-06 | t=0.0082s
    trss | MR=0.2 | seed=0 | MAE=9.7299e-07 | t=0.0186s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.1963e-05 | t=1.5361s

Completed: 2026-04-16T12:08:33.175419+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.