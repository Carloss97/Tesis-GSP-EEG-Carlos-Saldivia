# Integration Log: scr_00771
Started: 2026-04-16T11:54:39.607877+00:00
Description: Screening scr_00771 ds=bci_iv2a_real_s1 graph=knn miss=1ch mode=lambda

## Dataset: bci_iv2a_real_s1 | rows=24
  Graph: knn__k5 built OK
    tv | MR=0.2 | seed=0 | MAE=3.0348e-06 | t=0.1559s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=5.8873e-06 | t=0.0078s
    trss | MR=0.2 | seed=0 | MAE=7.3001e-07 | t=0.0183s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.0259e-05 | t=1.2601s
    tv | MR=0.2 | seed=1 | MAE=3.3726e-06 | t=0.1540s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=6.1319e-06 | t=0.0078s
    trss | MR=0.2 | seed=1 | MAE=8.7337e-07 | t=0.0188s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.0411e-05 | t=1.2862s
    tv | MR=0.2 | seed=0 | MAE=3.0353e-06 | t=0.1532s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=7.3590e-06 | t=0.0082s
    trss | MR=0.2 | seed=0 | MAE=9.7299e-07 | t=0.0188s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.1963e-05 | t=1.2396s

Completed: 2026-04-16T11:54:39.608795+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.