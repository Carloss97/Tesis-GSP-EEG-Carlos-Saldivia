# Integration Log: scr_00002
Started: 2026-04-16T15:14:40.686710+00:00
Description: Screening scr_00002 ds=physionet_real graph=knn miss=1ch mode=base

## Dataset: physionet_eegmmidb_real | rows=14
  Graph: knn__k3 built OK
    mean | MR=1ch | seed=0 | MAE=9.6765e-07 | t=0.0031s
    nearest | MR=1ch | seed=0 | MAE=1.0997e-06 | t=0.0031s
    tikhonov | MR=1ch | seed=0 | MAE=4.0683e-06 | t=0.0093s
    tv | MR=1ch | seed=0 | MAE=9.4225e-07 | t=0.8318s
    trss | MR=1ch | seed=0 | MAE=4.4946e-07 | t=0.0851s
    graph_time_tikhonov | MR=1ch | seed=0 | MAE=9.7351e-06 | t=0.0153s
    temporal_laplacian | MR=1ch | seed=0 | MAE=2.7184e-05 | t=29.7668s
    mean | MR=1ch | seed=1 | MAE=1.0229e-06 | t=0.0031s
    nearest | MR=1ch | seed=1 | MAE=1.1352e-06 | t=0.0031s
    tikhonov | MR=1ch | seed=1 | MAE=4.0990e-06 | t=0.0905s
    tv | MR=1ch | seed=1 | MAE=9.9681e-07 | t=0.5562s
    trss | MR=1ch | seed=1 | MAE=4.8245e-07 | t=0.5235s

Completed: 2026-04-16T15:14:40.687874+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.