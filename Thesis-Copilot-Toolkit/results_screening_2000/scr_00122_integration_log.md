# Integration Log: scr_00122
Started: 2026-04-16T15:11:51.301207+00:00
Description: Screening scr_00122 ds=physionet_real graph=knn miss=2ch mode=base

## Dataset: physionet_eegmmidb_real | rows=14
  Graph: knn__k5 built OK
    mean | MR=2ch | seed=0 | MAE=2.0892e-06 | t=0.0036s
    nearest | MR=2ch | seed=0 | MAE=2.3639e-06 | t=0.0047s
    tikhonov | MR=2ch | seed=0 | MAE=6.1981e-06 | t=0.0090s
    tv | MR=2ch | seed=0 | MAE=2.0760e-06 | t=0.2897s
    trss | MR=2ch | seed=0 | MAE=9.9346e-07 | t=0.0604s
    graph_time_tikhonov | MR=2ch | seed=0 | MAE=1.3073e-05 | t=0.0161s
    temporal_laplacian | MR=2ch | seed=0 | MAE=3.1644e-05 | t=10.9815s
    mean | MR=2ch | seed=1 | MAE=2.0496e-06 | t=0.0033s
    nearest | MR=2ch | seed=1 | MAE=2.3187e-06 | t=0.0053s
    tikhonov | MR=2ch | seed=1 | MAE=6.1834e-06 | t=0.0116s
    tv | MR=2ch | seed=1 | MAE=2.0371e-06 | t=0.8674s
    trss | MR=2ch | seed=1 | MAE=9.6487e-07 | t=0.5423s

Completed: 2026-04-16T15:11:51.302209+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.