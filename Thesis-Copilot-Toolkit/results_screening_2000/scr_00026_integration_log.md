# Integration Log: scr_00026
Started: 2026-04-16T15:28:08.815664+00:00
Description: Screening scr_00026 ds=physionet_real graph=knn miss=1ch mode=base

## Dataset: physionet_eegmmidb_real | rows=14
  Graph: knn__k7 built OK
    mean | MR=1ch | seed=0 | MAE=9.6765e-07 | t=0.0036s
    nearest | MR=1ch | seed=0 | MAE=1.0997e-06 | t=0.0970s
    tikhonov | MR=1ch | seed=0 | MAE=7.7121e-06 | t=0.0110s
    tv | MR=1ch | seed=0 | MAE=9.6466e-07 | t=0.9254s
    trss | MR=1ch | seed=0 | MAE=4.6637e-07 | t=0.6762s
    graph_time_tikhonov | MR=1ch | seed=0 | MAE=1.5588e-05 | t=0.0879s
    temporal_laplacian | MR=1ch | seed=0 | MAE=3.3725e-05 | t=35.1353s
    mean | MR=1ch | seed=1 | MAE=1.0229e-06 | t=0.0033s
    nearest | MR=1ch | seed=1 | MAE=1.1352e-06 | t=0.0032s
    tikhonov | MR=1ch | seed=1 | MAE=7.7587e-06 | t=0.0535s
    tv | MR=1ch | seed=1 | MAE=1.0201e-06 | t=0.6663s
    trss | MR=1ch | seed=1 | MAE=5.1863e-07 | t=1.0994s

Completed: 2026-04-16T15:28:08.816752+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.