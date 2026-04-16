# Integration Log: scr_00074
Started: 2026-04-16T14:48:41.558265+00:00
Description: Screening scr_00074 ds=physionet_real graph=knng miss=1ch mode=base

## Dataset: physionet_eegmmidb_real | rows=14
  Graph: knng built OK
    mean | MR=1ch | seed=0 | MAE=9.6765e-07 | t=0.0031s
    nearest | MR=1ch | seed=0 | MAE=1.0997e-06 | t=0.0031s
    tikhonov | MR=1ch | seed=0 | MAE=5.1306e-06 | t=0.0089s
    tv | MR=1ch | seed=0 | MAE=9.5819e-07 | t=0.6770s
    trss | MR=1ch | seed=0 | MAE=4.5676e-07 | t=0.5277s
    graph_time_tikhonov | MR=1ch | seed=0 | MAE=1.1722e-05 | t=0.0516s
    temporal_laplacian | MR=1ch | seed=0 | MAE=2.9631e-05 | t=28.2524s
    mean | MR=1ch | seed=1 | MAE=1.0229e-06 | t=0.0209s
    nearest | MR=1ch | seed=1 | MAE=1.1352e-06 | t=0.0031s
    tikhonov | MR=1ch | seed=1 | MAE=5.1600e-06 | t=0.0113s
    tv | MR=1ch | seed=1 | MAE=1.0135e-06 | t=0.4041s
    trss | MR=1ch | seed=1 | MAE=4.8863e-07 | t=0.2692s

Completed: 2026-04-16T14:48:41.559126+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.