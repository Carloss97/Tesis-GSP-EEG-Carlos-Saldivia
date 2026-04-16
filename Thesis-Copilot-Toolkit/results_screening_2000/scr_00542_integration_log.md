# Integration Log: scr_00542
Started: 2026-04-16T14:06:54.787623+00:00
Description: Screening scr_00542 ds=physionet_real graph=knn miss=[0.3] mode=base

## Dataset: physionet_eegmmidb_real | rows=14
  Graph: knn__k3 built OK
    mean | MR=0.3 | seed=0 | MAE=7.1409e-06 | t=0.0031s
    nearest | MR=0.3 | seed=0 | MAE=8.1341e-06 | t=0.0589s
    tikhonov | MR=0.3 | seed=0 | MAE=7.1847e-06 | t=0.0086s
    tv | MR=0.3 | seed=0 | MAE=6.9969e-06 | t=0.4497s
    trss | MR=0.3 | seed=0 | MAE=3.7536e-06 | t=0.4617s
    graph_time_tikhonov | MR=0.3 | seed=0 | MAE=1.1711e-05 | t=0.0497s
    temporal_laplacian | MR=0.3 | seed=0 | MAE=3.0584e-05 | t=13.6719s
    mean | MR=0.3 | seed=1 | MAE=7.3000e-06 | t=0.0022s
    nearest | MR=0.3 | seed=1 | MAE=8.0659e-06 | t=0.0064s
    tikhonov | MR=0.3 | seed=1 | MAE=7.2170e-06 | t=0.0057s
    tv | MR=0.3 | seed=1 | MAE=7.1544e-06 | t=0.1630s
    trss | MR=0.3 | seed=1 | MAE=3.7626e-06 | t=0.1848s

Completed: 2026-04-16T14:06:54.788577+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.