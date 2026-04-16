# Integration Log: scr_01085
Started: 2026-04-16T13:32:48.979343+00:00
Description: Screening scr_01085 ds=bci_iv2a_real_s3 graph=knn miss=[0.1] mode=lambda

## Dataset: bci_iv2a_real_s3 | rows=24
  Graph: knn__k3 built OK
    tv | MR=0.2 | seed=0 | MAE=7.3148e-07 | t=0.1574s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.5453e-06 | t=0.0079s
    trss | MR=0.2 | seed=0 | MAE=3.9898e-07 | t=0.0187s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.4295e-06 | t=12.7018s
    tv | MR=0.2 | seed=1 | MAE=7.3470e-07 | t=0.1537s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=1.5388e-06 | t=0.0079s
    trss | MR=0.2 | seed=1 | MAE=4.0184e-07 | t=0.0196s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=2.4396e-06 | t=19.8599s
    tv | MR=0.2 | seed=0 | MAE=7.3141e-07 | t=0.4208s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.7527e-06 | t=0.0081s
    trss | MR=0.2 | seed=0 | MAE=4.2757e-07 | t=0.0198s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=3.0806e-06 | t=6.9591s

Completed: 2026-04-16T13:32:48.980221+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.