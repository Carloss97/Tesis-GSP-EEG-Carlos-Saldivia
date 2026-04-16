# Integration Log: scr_00134
Started: 2026-04-16T15:18:47.600786+00:00
Description: Screening scr_00134 ds=physionet_real graph=knn miss=2ch mode=base

## Dataset: physionet_eegmmidb_real | rows=14
  Graph: knn__k7 built OK
    mean | MR=2ch | seed=0 | MAE=2.0892e-06 | t=0.0032s
    nearest | MR=2ch | seed=0 | MAE=2.3639e-06 | t=0.0046s
    tikhonov | MR=2ch | seed=0 | MAE=8.2154e-06 | t=0.0419s
    tv | MR=2ch | seed=0 | MAE=2.0831e-06 | t=0.6554s
    trss | MR=2ch | seed=0 | MAE=1.0520e-06 | t=0.4090s
    graph_time_tikhonov | MR=2ch | seed=0 | MAE=1.5884e-05 | t=0.0127s
    temporal_laplacian | MR=2ch | seed=0 | MAE=3.4096e-05 | t=20.6502s
    mean | MR=2ch | seed=1 | MAE=2.0496e-06 | t=0.0032s
    nearest | MR=2ch | seed=1 | MAE=2.3187e-06 | t=0.0044s
    tikhonov | MR=2ch | seed=1 | MAE=8.1835e-06 | t=0.1461s
    tv | MR=2ch | seed=1 | MAE=2.0437e-06 | t=1.2082s
    trss | MR=2ch | seed=1 | MAE=1.0412e-06 | t=0.6556s

Completed: 2026-04-16T15:18:47.601758+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.