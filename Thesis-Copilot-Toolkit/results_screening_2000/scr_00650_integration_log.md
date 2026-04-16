# Integration Log: scr_00650
Started: 2026-04-16T14:59:57.945487+00:00
Description: Screening scr_00650 ds=physionet_real graph=knn miss=[0.4] mode=base

## Dataset: physionet_eegmmidb_real | rows=14
  Graph: knn__k3 built OK
    mean | MR=0.4 | seed=0 | MAE=1.0497e-05 | t=0.0035s
    nearest | MR=0.4 | seed=0 | MAE=1.1571e-05 | t=0.0144s
    tikhonov | MR=0.4 | seed=0 | MAE=9.0742e-06 | t=0.0089s
    tv | MR=0.4 | seed=0 | MAE=1.0327e-05 | t=0.3870s
    trss | MR=0.4 | seed=0 | MAE=5.8699e-06 | t=0.4071s
    graph_time_tikhonov | MR=0.4 | seed=0 | MAE=1.3003e-05 | t=0.0124s
    temporal_laplacian | MR=0.4 | seed=0 | MAE=3.2307e-05 | t=25.1004s
    mean | MR=0.4 | seed=1 | MAE=1.0467e-05 | t=0.0031s
    nearest | MR=0.4 | seed=1 | MAE=1.1385e-05 | t=0.0152s
    tikhonov | MR=0.4 | seed=1 | MAE=9.0046e-06 | t=0.0087s
    tv | MR=0.4 | seed=1 | MAE=1.0293e-05 | t=0.4517s
    trss | MR=0.4 | seed=1 | MAE=5.7674e-06 | t=0.4205s

Completed: 2026-04-16T14:59:57.946364+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.