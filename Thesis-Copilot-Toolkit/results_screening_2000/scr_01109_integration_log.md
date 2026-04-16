# Integration Log: scr_01109
Started: 2026-04-16T13:51:53.923675+00:00
Description: Screening scr_01109 ds=bci_iv2a_real_s3 graph=knn miss=[0.1] mode=lambda

## Dataset: bci_iv2a_real_s3 | rows=24
  Graph: knn__k7 built OK
    tv | MR=0.2 | seed=0 | MAE=7.3147e-07 | t=0.8100s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.8640e-06 | t=0.0123s
    trss | MR=0.2 | seed=0 | MAE=3.4930e-07 | t=0.4549s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=3.4121e-06 | t=12.2617s
    tv | MR=0.2 | seed=1 | MAE=7.3468e-07 | t=0.2422s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=1.8568e-06 | t=0.0124s
    trss | MR=0.2 | seed=1 | MAE=3.5867e-07 | t=0.3049s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=3.4241e-06 | t=20.7358s
    tv | MR=0.2 | seed=0 | MAE=7.3141e-07 | t=0.1639s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.2199e-06 | t=0.0084s
    trss | MR=0.2 | seed=0 | MAE=3.8288e-07 | t=0.0200s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=4.3080e-06 | t=6.6481s

Completed: 2026-04-16T13:51:53.924527+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.