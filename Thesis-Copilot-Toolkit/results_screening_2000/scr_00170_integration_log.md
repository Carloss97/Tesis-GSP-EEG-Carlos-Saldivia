# Integration Log: scr_00170
Started: 2026-04-16T15:38:20.438880+00:00
Description: Screening scr_00170 ds=physionet_real graph=kalofolias miss=2ch mode=base

## Dataset: physionet_eegmmidb_real | rows=14
  Graph: kalofolias built OK
    mean | MR=2ch | seed=0 | MAE=2.0892e-06 | t=0.0271s
    nearest | MR=2ch | seed=0 | MAE=2.3639e-06 | t=0.0045s
    tikhonov | MR=2ch | seed=0 | MAE=1.0990e-05 | t=0.0338s
    tv | MR=2ch | seed=0 | MAE=2.0892e-06 | t=0.6400s
    trss | MR=2ch | seed=0 | MAE=1.5121e-06 | t=0.1736s
    graph_time_tikhonov | MR=2ch | seed=0 | MAE=1.8987e-05 | t=0.0393s
    temporal_laplacian | MR=2ch | seed=0 | MAE=3.3587e-05 | t=17.7058s
    mean | MR=2ch | seed=1 | MAE=2.0496e-06 | t=0.0242s
    nearest | MR=2ch | seed=1 | MAE=2.3187e-06 | t=0.0051s
    tikhonov | MR=2ch | seed=1 | MAE=1.0983e-05 | t=0.0306s
    tv | MR=2ch | seed=1 | MAE=2.0496e-06 | t=0.7559s
    trss | MR=2ch | seed=1 | MAE=1.4845e-06 | t=0.1183s

Completed: 2026-04-16T15:38:20.439965+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.