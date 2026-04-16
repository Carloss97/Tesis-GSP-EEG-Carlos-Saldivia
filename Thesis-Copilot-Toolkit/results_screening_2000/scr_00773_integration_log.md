# Integration Log: scr_00773
Started: 2026-04-16T11:55:11.792118+00:00
Description: Screening scr_00773 ds=bci_iv2a_real_s3 graph=knn miss=1ch mode=lambda

## Dataset: bci_iv2a_real_s3 | rows=24
  Graph: knn__k5 built OK
    tv | MR=0.2 | seed=0 | MAE=7.3155e-07 | t=0.1542s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.7328e-06 | t=0.0079s
    trss | MR=0.2 | seed=0 | MAE=3.6240e-07 | t=0.0187s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.9958e-06 | t=2.2004s
    tv | MR=0.2 | seed=1 | MAE=7.3474e-07 | t=0.1526s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=1.7246e-06 | t=0.0078s
    trss | MR=0.2 | seed=1 | MAE=3.7337e-07 | t=0.0188s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=3.0066e-06 | t=2.6814s
    tv | MR=0.2 | seed=0 | MAE=7.3145e-07 | t=0.1997s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.0343e-06 | t=0.0081s
    trss | MR=0.2 | seed=0 | MAE=4.0262e-07 | t=0.0194s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=3.8232e-06 | t=2.6584s

Completed: 2026-04-16T11:55:11.792817+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.