# Integration Log: scr_00098
Started: 2026-04-16T15:00:27.508871+00:00
Description: Screening scr_00098 ds=physionet_real graph=aew miss=1ch mode=base

## Dataset: physionet_eegmmidb_real | rows=14
  Graph: aew built OK
    mean | MR=1ch | seed=0 | MAE=9.6765e-07 | t=0.0033s
    nearest | MR=1ch | seed=0 | MAE=1.0997e-06 | t=0.0067s
    tikhonov | MR=1ch | seed=0 | MAE=4.3100e-06 | t=0.0088s
    tv | MR=1ch | seed=0 | MAE=9.5544e-07 | t=0.6442s
    trss | MR=1ch | seed=0 | MAE=4.4618e-07 | t=0.5197s
    graph_time_tikhonov | MR=1ch | seed=0 | MAE=1.0569e-05 | t=0.0126s
    temporal_laplacian | MR=1ch | seed=0 | MAE=2.7544e-05 | t=26.1707s
    mean | MR=1ch | seed=1 | MAE=1.0229e-06 | t=0.0034s
    nearest | MR=1ch | seed=1 | MAE=1.1352e-06 | t=0.0033s
    tikhonov | MR=1ch | seed=1 | MAE=4.3462e-06 | t=0.0100s
    tv | MR=1ch | seed=1 | MAE=1.0109e-06 | t=0.6650s
    trss | MR=1ch | seed=1 | MAE=4.7945e-07 | t=0.4441s

Completed: 2026-04-16T15:00:27.509913+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.