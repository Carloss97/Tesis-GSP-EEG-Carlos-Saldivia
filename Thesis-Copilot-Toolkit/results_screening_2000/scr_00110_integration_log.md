# Integration Log: scr_00110
Started: 2026-04-16T15:06:05.998677+00:00
Description: Screening scr_00110 ds=physionet_real graph=knn miss=2ch mode=base

## Dataset: physionet_eegmmidb_real | rows=14
  Graph: knn__k3 built OK
    mean | MR=2ch | seed=0 | MAE=2.0892e-06 | t=0.0033s
    nearest | MR=2ch | seed=0 | MAE=2.3639e-06 | t=0.0102s
    tikhonov | MR=2ch | seed=0 | MAE=4.5685e-06 | t=0.0106s
    tv | MR=2ch | seed=0 | MAE=2.0331e-06 | t=0.8338s
    trss | MR=2ch | seed=0 | MAE=9.7034e-07 | t=0.4585s
    graph_time_tikhonov | MR=2ch | seed=0 | MAE=1.0050e-05 | t=0.0519s
    temporal_laplacian | MR=2ch | seed=0 | MAE=2.7778e-05 | t=15.4498s
    mean | MR=2ch | seed=1 | MAE=2.0496e-06 | t=0.0032s
    nearest | MR=2ch | seed=1 | MAE=2.3187e-06 | t=0.0044s
    tikhonov | MR=2ch | seed=1 | MAE=4.5474e-06 | t=0.0101s
    tv | MR=2ch | seed=1 | MAE=1.9934e-06 | t=0.8590s
    trss | MR=2ch | seed=1 | MAE=9.4228e-07 | t=1.2427s

Completed: 2026-04-16T15:06:05.999484+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.