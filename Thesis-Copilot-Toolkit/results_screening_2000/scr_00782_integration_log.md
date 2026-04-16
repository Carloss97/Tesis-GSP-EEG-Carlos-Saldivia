# Integration Log: scr_00782
Started: 2026-04-16T11:55:58.618051+00:00
Description: Screening scr_00782 ds=physionet_real graph=knn miss=1ch mode=lambda

## Dataset: physionet_eegmmidb_real | rows=24
  Graph: knn__k7 built OK
    tv | MR=0.2 | seed=0 | MAE=5.1566e-06 | t=0.1654s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=7.9522e-06 | t=0.0078s
    trss | MR=0.2 | seed=0 | MAE=1.8510e-06 | t=0.0182s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.9030e-05 | t=2.6426s
    tv | MR=0.2 | seed=1 | MAE=5.1672e-06 | t=0.1576s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=7.9369e-06 | t=0.0091s
    trss | MR=0.2 | seed=1 | MAE=1.8855e-06 | t=0.0205s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.9216e-05 | t=2.7906s
    tv | MR=0.2 | seed=0 | MAE=5.1809e-06 | t=0.1517s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.0121e-05 | t=0.0078s
    trss | MR=0.2 | seed=0 | MAE=1.9543e-06 | t=0.0186s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.4069e-05 | t=2.6125s

Completed: 2026-04-16T11:55:58.618873+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.