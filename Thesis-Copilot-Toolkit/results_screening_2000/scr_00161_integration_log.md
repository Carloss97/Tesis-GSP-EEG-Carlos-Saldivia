# Integration Log: scr_00161
Started: 2026-04-16T15:34:50.538756+00:00
Description: Screening scr_00161 ds=bci_iv2a_real_s3 graph=gaussian miss=2ch mode=base

## Dataset: bci_iv2a_real_s3 | rows=14
  Graph: gaussian__sigma0.6 built OK
    mean | MR=2ch | seed=0 | MAE=3.0419e-07 | t=0.0039s
    nearest | MR=2ch | seed=0 | MAE=2.4876e-07 | t=0.0195s
    tikhonov | MR=2ch | seed=0 | MAE=2.4703e-06 | t=0.0097s
    tv | MR=2ch | seed=0 | MAE=3.0419e-07 | t=0.9634s
    trss | MR=2ch | seed=0 | MAE=2.1652e-07 | t=0.0929s
    graph_time_tikhonov | MR=2ch | seed=0 | MAE=3.2163e-06 | t=0.0444s
    temporal_laplacian | MR=2ch | seed=0 | MAE=6.4614e-06 | t=9.8605s
    mean | MR=2ch | seed=1 | MAE=2.8472e-07 | t=0.0031s
    nearest | MR=2ch | seed=1 | MAE=2.5230e-07 | t=0.0046s
    tikhonov | MR=2ch | seed=1 | MAE=2.4663e-06 | t=0.0385s
    tv | MR=2ch | seed=1 | MAE=2.8472e-07 | t=1.5841s
    trss | MR=2ch | seed=1 | MAE=2.0313e-07 | t=0.3125s

Completed: 2026-04-16T15:34:50.540177+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.