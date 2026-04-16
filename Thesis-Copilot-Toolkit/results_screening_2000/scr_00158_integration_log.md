# Integration Log: scr_00158
Started: 2026-04-16T15:32:30.348739+00:00
Description: Screening scr_00158 ds=physionet_real graph=gaussian miss=2ch mode=base

## Dataset: physionet_eegmmidb_real | rows=14
  Graph: gaussian__sigma0.6 built OK
    mean | MR=2ch | seed=0 | MAE=2.0892e-06 | t=0.0040s
    nearest | MR=2ch | seed=0 | MAE=2.3639e-06 | t=0.0058s
    tikhonov | MR=2ch | seed=0 | MAE=1.7107e-05 | t=0.0221s
    tv | MR=2ch | seed=0 | MAE=2.0892e-06 | t=0.6347s
    trss | MR=2ch | seed=0 | MAE=1.5039e-06 | t=0.1878s
    graph_time_tikhonov | MR=2ch | seed=0 | MAE=2.1933e-05 | t=0.0171s
    temporal_laplacian | MR=2ch | seed=0 | MAE=3.8732e-05 | t=12.9986s
    mean | MR=2ch | seed=1 | MAE=2.0496e-06 | t=0.0111s
    nearest | MR=2ch | seed=1 | MAE=2.3187e-06 | t=0.0074s
    tikhonov | MR=2ch | seed=1 | MAE=1.7122e-05 | t=0.0095s
    tv | MR=2ch | seed=1 | MAE=2.0495e-06 | t=0.5358s
    trss | MR=2ch | seed=1 | MAE=1.4767e-06 | t=0.4842s

Completed: 2026-04-16T15:32:30.350020+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.