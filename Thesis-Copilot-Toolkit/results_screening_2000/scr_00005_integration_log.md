# Integration Log: scr_00005
Started: 2026-04-16T15:17:59.812575+00:00
Description: Screening scr_00005 ds=bci_iv2a_real_s3 graph=knn miss=1ch mode=base

## Dataset: bci_iv2a_real_s3 | rows=14
  Graph: knn__k3 built OK
    mean | MR=1ch | seed=0 | MAE=1.5214e-07 | t=0.0031s
    nearest | MR=1ch | seed=0 | MAE=1.2148e-07 | t=0.0032s
    tikhonov | MR=1ch | seed=0 | MAE=1.1084e-06 | t=0.0087s
    tv | MR=1ch | seed=0 | MAE=1.5215e-07 | t=1.0319s
    trss | MR=1ch | seed=0 | MAE=1.3250e-07 | t=0.4800s
    graph_time_tikhonov | MR=1ch | seed=0 | MAE=2.3465e-06 | t=0.0179s
    temporal_laplacian | MR=1ch | seed=0 | MAE=4.7058e-06 | t=32.4859s
    mean | MR=1ch | seed=1 | MAE=1.4873e-07 | t=0.0030s
    nearest | MR=1ch | seed=1 | MAE=1.2335e-07 | t=0.0038s
    tikhonov | MR=1ch | seed=1 | MAE=1.1065e-06 | t=0.0086s
    tv | MR=1ch | seed=1 | MAE=1.4873e-07 | t=0.8481s
    trss | MR=1ch | seed=1 | MAE=1.3151e-07 | t=0.7651s

Completed: 2026-04-16T15:17:59.813453+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.