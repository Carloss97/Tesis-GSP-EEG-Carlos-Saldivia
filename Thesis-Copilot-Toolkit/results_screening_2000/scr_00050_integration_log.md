# Integration Log: scr_00050
Started: 2026-04-16T15:40:28.035791+00:00
Description: Screening scr_00050 ds=physionet_real graph=gaussian miss=1ch mode=base

## Dataset: physionet_eegmmidb_real | rows=14
  Graph: gaussian__sigma0.6 built OK
    mean | MR=1ch | seed=0 | MAE=9.6765e-07 | t=0.0042s
    nearest | MR=1ch | seed=0 | MAE=1.0997e-06 | t=0.0041s
    tikhonov | MR=1ch | seed=0 | MAE=1.6784e-05 | t=0.0161s
    tv | MR=1ch | seed=0 | MAE=9.6764e-07 | t=0.6528s
    trss | MR=1ch | seed=0 | MAE=6.7553e-07 | t=0.1203s
    graph_time_tikhonov | MR=1ch | seed=0 | MAE=2.1872e-05 | t=0.0462s
    temporal_laplacian | MR=1ch | seed=0 | MAE=3.8545e-05 | t=30.2409s
    mean | MR=1ch | seed=1 | MAE=1.0229e-06 | t=0.0045s
    nearest | MR=1ch | seed=1 | MAE=1.1352e-06 | t=0.0035s
    tikhonov | MR=1ch | seed=1 | MAE=1.6799e-05 | t=0.2288s
    tv | MR=1ch | seed=1 | MAE=1.0229e-06 | t=1.0781s
    trss | MR=1ch | seed=1 | MAE=7.1619e-07 | t=0.5204s

Completed: 2026-04-16T15:40:28.036687+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.