# Integration Log: scr_00014
Started: 2026-04-16T15:21:54.433749+00:00
Description: Screening scr_00014 ds=physionet_real graph=knn miss=1ch mode=base

## Dataset: physionet_eegmmidb_real | rows=14
  Graph: knn__k5 built OK
    mean | MR=1ch | seed=0 | MAE=9.6765e-07 | t=0.0031s
    nearest | MR=1ch | seed=0 | MAE=1.0997e-06 | t=0.0031s
    tikhonov | MR=1ch | seed=0 | MAE=5.7027e-06 | t=0.0087s
    tv | MR=1ch | seed=0 | MAE=9.6125e-07 | t=0.7845s
    trss | MR=1ch | seed=0 | MAE=4.4365e-07 | t=0.7524s
    graph_time_tikhonov | MR=1ch | seed=0 | MAE=1.2748e-05 | t=0.0747s
    temporal_laplacian | MR=1ch | seed=0 | MAE=3.1173e-05 | t=20.7359s
    mean | MR=1ch | seed=1 | MAE=1.0229e-06 | t=0.0030s
    nearest | MR=1ch | seed=1 | MAE=1.1352e-06 | t=0.0031s
    tikhonov | MR=1ch | seed=1 | MAE=5.7467e-06 | t=0.0086s
    tv | MR=1ch | seed=1 | MAE=1.0168e-06 | t=0.7316s
    trss | MR=1ch | seed=1 | MAE=4.8158e-07 | t=0.6393s

Completed: 2026-04-16T15:21:54.435173+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.