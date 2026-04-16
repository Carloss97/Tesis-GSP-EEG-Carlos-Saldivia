# Integration Log: scr_00761
Started: 2026-04-16T11:53:40.099742+00:00
Description: Screening scr_00761 ds=bci_iv2a_real_s3 graph=knn miss=1ch mode=lambda

## Dataset: bci_iv2a_real_s3 | rows=24
  Graph: knn__k3 built OK
    tv | MR=0.2 | seed=0 | MAE=7.3148e-07 | t=0.1454s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.5453e-06 | t=0.0078s
    trss | MR=0.2 | seed=0 | MAE=3.9898e-07 | t=0.0190s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.4295e-06 | t=2.6724s
    tv | MR=0.2 | seed=1 | MAE=7.3470e-07 | t=0.1620s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=1.5388e-06 | t=0.0085s
    trss | MR=0.2 | seed=1 | MAE=4.0184e-07 | t=0.0193s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=2.4396e-06 | t=2.6735s
    tv | MR=0.2 | seed=0 | MAE=7.3141e-07 | t=0.1475s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.7527e-06 | t=0.0082s
    trss | MR=0.2 | seed=0 | MAE=4.2757e-07 | t=0.0196s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=3.0806e-06 | t=2.6381s

Completed: 2026-04-16T11:53:40.100500+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.