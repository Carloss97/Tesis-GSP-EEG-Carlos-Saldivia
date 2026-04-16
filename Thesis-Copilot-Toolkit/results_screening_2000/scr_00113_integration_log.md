# Integration Log: scr_00113
Started: 2026-04-16T15:08:47.051829+00:00
Description: Screening scr_00113 ds=bci_iv2a_real_s3 graph=knn miss=2ch mode=base

## Dataset: bci_iv2a_real_s3 | rows=14
  Graph: knn__k3 built OK
    mean | MR=2ch | seed=0 | MAE=3.0419e-07 | t=0.0033s
    nearest | MR=2ch | seed=0 | MAE=2.4876e-07 | t=0.0043s
    tikhonov | MR=2ch | seed=0 | MAE=1.2245e-06 | t=0.0228s
    tv | MR=2ch | seed=0 | MAE=3.0422e-07 | t=0.5954s
    trss | MR=2ch | seed=0 | MAE=2.7490e-07 | t=0.2254s
    graph_time_tikhonov | MR=2ch | seed=0 | MAE=2.4018e-06 | t=0.0129s
    temporal_laplacian | MR=2ch | seed=0 | MAE=4.7930e-06 | t=21.9224s
    mean | MR=2ch | seed=1 | MAE=2.8472e-07 | t=0.0097s
    nearest | MR=2ch | seed=1 | MAE=2.5230e-07 | t=0.0044s
    tikhonov | MR=2ch | seed=1 | MAE=1.2060e-06 | t=0.1386s
    tv | MR=2ch | seed=1 | MAE=2.8474e-07 | t=0.6365s
    trss | MR=2ch | seed=1 | MAE=2.6659e-07 | t=0.4327s

Completed: 2026-04-16T15:08:47.053151+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.