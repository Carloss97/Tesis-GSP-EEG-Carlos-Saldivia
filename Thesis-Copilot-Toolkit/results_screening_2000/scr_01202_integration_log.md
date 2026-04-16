# Integration Log: scr_01202
Started: 2026-04-16T15:37:59.524345+00:00
Description: Screening scr_01202 ds=physionet_real graph=knn miss=[0.2] mode=lambda

## Dataset: physionet_eegmmidb_real | rows=24
  Graph: knn__k5 built OK
    tv | MR=0.2 | seed=0 | MAE=5.1032e-06 | t=0.9206s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=6.6501e-06 | t=0.0342s
    trss | MR=0.2 | seed=0 | MAE=1.7786e-06 | t=0.5031s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.7023e-05 | t=5.3776s
    tv | MR=0.2 | seed=1 | MAE=5.1120e-06 | t=0.6923s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=6.5763e-06 | t=0.0395s
    trss | MR=0.2 | seed=1 | MAE=1.8204e-06 | t=0.3075s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.7171e-05 | t=34.2258s
    tv | MR=0.2 | seed=0 | MAE=5.1533e-06 | t=0.2199s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=8.2347e-06 | t=0.0095s
    trss | MR=0.2 | seed=0 | MAE=1.8814e-06 | t=0.0287s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.1365e-05 | t=39.6297s

Completed: 2026-04-16T15:37:59.525647+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.