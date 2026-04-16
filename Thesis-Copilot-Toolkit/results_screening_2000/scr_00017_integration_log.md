# Integration Log: scr_00017
Started: 2026-04-16T15:24:59.764318+00:00
Description: Screening scr_00017 ds=bci_iv2a_real_s3 graph=knn miss=1ch mode=base

## Dataset: bci_iv2a_real_s3 | rows=14
  Graph: knn__k5 built OK
    mean | MR=1ch | seed=0 | MAE=1.5214e-07 | t=0.0066s
    nearest | MR=1ch | seed=0 | MAE=1.2148e-07 | t=0.0036s
    tikhonov | MR=1ch | seed=0 | MAE=1.5091e-06 | t=0.0111s
    tv | MR=1ch | seed=0 | MAE=1.5215e-07 | t=0.5069s
    trss | MR=1ch | seed=0 | MAE=1.2571e-07 | t=0.3019s
    graph_time_tikhonov | MR=1ch | seed=0 | MAE=2.7083e-06 | t=0.0136s
    temporal_laplacian | MR=1ch | seed=0 | MAE=5.4451e-06 | t=33.6425s
    mean | MR=1ch | seed=1 | MAE=1.4873e-07 | t=0.0037s
    nearest | MR=1ch | seed=1 | MAE=1.2335e-07 | t=0.0031s
    tikhonov | MR=1ch | seed=1 | MAE=1.5101e-06 | t=0.0117s
    tv | MR=1ch | seed=1 | MAE=1.4873e-07 | t=1.3203s
    trss | MR=1ch | seed=1 | MAE=1.2603e-07 | t=0.1046s

Completed: 2026-04-16T15:24:59.765480+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.