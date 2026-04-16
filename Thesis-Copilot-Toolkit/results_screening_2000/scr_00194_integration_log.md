# Integration Log: scr_00194
Started: 2026-04-16T14:23:58.488310+00:00
Description: Screening scr_00194 ds=physionet_real graph=vknng miss=2ch mode=base

## Dataset: physionet_eegmmidb_real | rows=14
  Graph: vknng built OK
    mean | MR=2ch | seed=0 | MAE=2.0892e-06 | t=0.0041s
    nearest | MR=2ch | seed=0 | MAE=2.3639e-06 | t=0.0043s
    tikhonov | MR=2ch | seed=0 | MAE=5.5903e-06 | t=0.0092s
    tv | MR=2ch | seed=0 | MAE=2.0662e-06 | t=0.5803s
    trss | MR=2ch | seed=0 | MAE=1.0227e-06 | t=0.8452s
    graph_time_tikhonov | MR=2ch | seed=0 | MAE=1.1915e-05 | t=0.0226s
    temporal_laplacian | MR=2ch | seed=0 | MAE=2.9777e-05 | t=25.1905s
    mean | MR=2ch | seed=1 | MAE=2.0496e-06 | t=0.0037s
    nearest | MR=2ch | seed=1 | MAE=2.3187e-06 | t=0.0043s
    tikhonov | MR=2ch | seed=1 | MAE=5.5672e-06 | t=0.0086s
    tv | MR=2ch | seed=1 | MAE=2.0272e-06 | t=0.4531s
    trss | MR=2ch | seed=1 | MAE=1.0059e-06 | t=0.5955s

Completed: 2026-04-16T14:23:58.489529+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.