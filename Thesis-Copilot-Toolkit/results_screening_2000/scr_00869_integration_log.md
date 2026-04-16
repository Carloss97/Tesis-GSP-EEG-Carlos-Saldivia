# Integration Log: scr_00869
Started: 2026-04-16T12:07:33.012279+00:00
Description: Screening scr_00869 ds=bci_iv2a_real_s3 graph=knn miss=2ch mode=lambda

## Dataset: bci_iv2a_real_s3 | rows=24
  Graph: knn__k3 built OK
    tv | MR=0.2 | seed=0 | MAE=7.3148e-07 | t=0.1544s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.5453e-06 | t=0.0089s
    trss | MR=0.2 | seed=0 | MAE=3.9898e-07 | t=0.0213s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.4295e-06 | t=2.6735s
    tv | MR=0.2 | seed=1 | MAE=7.3470e-07 | t=0.1602s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=1.5388e-06 | t=0.0083s
    trss | MR=0.2 | seed=1 | MAE=4.0184e-07 | t=0.0201s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=2.4396e-06 | t=2.6259s
    tv | MR=0.2 | seed=0 | MAE=7.3141e-07 | t=0.1519s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.7527e-06 | t=0.0079s
    trss | MR=0.2 | seed=0 | MAE=4.2757e-07 | t=0.0194s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=3.0806e-06 | t=2.6933s

Completed: 2026-04-16T12:07:33.013220+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.