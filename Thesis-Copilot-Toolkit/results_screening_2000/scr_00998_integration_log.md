# Integration Log: scr_00998
Started: 2026-04-16T12:48:20.705501+00:00
Description: Screening scr_00998 ds=physionet_real graph=knn miss=3ch mode=lambda

## Dataset: physionet_eegmmidb_real | rows=24
  Graph: knn__k7 built OK
    tv | MR=0.2 | seed=0 | MAE=5.1566e-06 | t=0.3117s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=7.9522e-06 | t=0.0123s
    trss | MR=0.2 | seed=0 | MAE=1.8510e-06 | t=0.0638s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.9030e-05 | t=3.6192s
    tv | MR=0.2 | seed=1 | MAE=5.1672e-06 | t=0.2956s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=7.9369e-06 | t=0.0160s
    trss | MR=0.2 | seed=1 | MAE=1.8855e-06 | t=0.0670s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.9216e-05 | t=2.1575s
    tv | MR=0.2 | seed=0 | MAE=5.1809e-06 | t=0.1750s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.0121e-05 | t=0.0080s
    trss | MR=0.2 | seed=0 | MAE=1.9543e-06 | t=0.0194s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.4069e-05 | t=9.2013s

Completed: 2026-04-16T12:48:20.706370+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.