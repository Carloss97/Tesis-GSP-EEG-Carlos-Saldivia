# Integration Log: scr_00206
Started: 2026-04-16T14:30:14.038979+00:00
Description: Screening scr_00206 ds=physionet_real graph=aew miss=2ch mode=base

## Dataset: physionet_eegmmidb_real | rows=14
  Graph: aew built OK
    mean | MR=2ch | seed=0 | MAE=2.0892e-06 | t=0.0030s
    nearest | MR=2ch | seed=0 | MAE=2.3639e-06 | t=0.0120s
    tikhonov | MR=2ch | seed=0 | MAE=4.8416e-06 | t=0.0417s
    tv | MR=2ch | seed=0 | MAE=2.0630e-06 | t=0.4769s
    trss | MR=2ch | seed=0 | MAE=9.8550e-07 | t=0.4809s
    graph_time_tikhonov | MR=2ch | seed=0 | MAE=1.0920e-05 | t=0.0200s
    temporal_laplacian | MR=2ch | seed=0 | MAE=2.8114e-05 | t=28.1341s
    mean | MR=2ch | seed=1 | MAE=2.0496e-06 | t=0.0032s
    nearest | MR=2ch | seed=1 | MAE=2.3187e-06 | t=0.0042s
    tikhonov | MR=2ch | seed=1 | MAE=4.8236e-06 | t=0.0138s
    tv | MR=2ch | seed=1 | MAE=2.0248e-06 | t=0.5724s
    trss | MR=2ch | seed=1 | MAE=9.6475e-07 | t=0.6417s

Completed: 2026-04-16T14:30:14.041339+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.