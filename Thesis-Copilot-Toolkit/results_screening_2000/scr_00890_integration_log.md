# Integration Log: scr_00890
Started: 2026-04-16T12:09:50.459549+00:00
Description: Screening scr_00890 ds=physionet_real graph=knn miss=2ch mode=lambda

## Dataset: physionet_eegmmidb_real | rows=24
  Graph: knn__k7 built OK
    tv | MR=0.2 | seed=0 | MAE=5.1566e-06 | t=0.1651s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=7.9522e-06 | t=0.0085s
    trss | MR=0.2 | seed=0 | MAE=1.8510e-06 | t=0.0189s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.9030e-05 | t=2.4935s
    tv | MR=0.2 | seed=1 | MAE=5.1672e-06 | t=0.1845s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=7.9369e-06 | t=0.0129s
    trss | MR=0.2 | seed=1 | MAE=1.8855e-06 | t=0.0199s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.9216e-05 | t=2.6104s
    tv | MR=0.2 | seed=0 | MAE=5.1809e-06 | t=0.1547s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.0121e-05 | t=0.0078s
    trss | MR=0.2 | seed=0 | MAE=1.9543e-06 | t=0.0189s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.4069e-05 | t=2.5403s

Completed: 2026-04-16T12:09:50.460262+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.