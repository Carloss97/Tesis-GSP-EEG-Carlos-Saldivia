# Integration Log: scr_01193
Started: 2026-04-16T15:29:59.060730+00:00
Description: Screening scr_01193 ds=bci_iv2a_real_s3 graph=knn miss=[0.2] mode=lambda

## Dataset: bci_iv2a_real_s3 | rows=24
  Graph: knn__k3 built OK
    tv | MR=0.2 | seed=0 | MAE=7.3148e-07 | t=1.3271s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.5453e-06 | t=0.0139s
    trss | MR=0.2 | seed=0 | MAE=3.9898e-07 | t=0.7033s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.4295e-06 | t=26.1635s
    tv | MR=0.2 | seed=1 | MAE=7.3470e-07 | t=0.6259s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=1.5388e-06 | t=0.1458s
    trss | MR=0.2 | seed=1 | MAE=4.0184e-07 | t=0.1355s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=2.4396e-06 | t=31.3216s
    tv | MR=0.2 | seed=0 | MAE=7.3141e-07 | t=1.2792s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.7527e-06 | t=0.0765s
    trss | MR=0.2 | seed=0 | MAE=4.2757e-07 | t=0.4311s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=3.0806e-06 | t=17.2019s

Completed: 2026-04-16T15:29:59.125233+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.