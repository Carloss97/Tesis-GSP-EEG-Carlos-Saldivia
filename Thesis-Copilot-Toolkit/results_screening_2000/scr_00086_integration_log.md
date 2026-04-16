# Integration Log: scr_00086
Started: 2026-04-16T14:54:36.282842+00:00
Description: Screening scr_00086 ds=physionet_real graph=vknng miss=1ch mode=base

## Dataset: physionet_eegmmidb_real | rows=14
  Graph: vknng built OK
    mean | MR=1ch | seed=0 | MAE=9.6765e-07 | t=0.0033s
    nearest | MR=1ch | seed=0 | MAE=1.0997e-06 | t=0.0035s
    tikhonov | MR=1ch | seed=0 | MAE=5.0767e-06 | t=0.0119s
    tv | MR=1ch | seed=0 | MAE=9.5730e-07 | t=0.4986s
    trss | MR=1ch | seed=0 | MAE=4.6699e-07 | t=0.4594s
    graph_time_tikhonov | MR=1ch | seed=0 | MAE=1.1588e-05 | t=0.0441s
    temporal_laplacian | MR=1ch | seed=0 | MAE=2.9253e-05 | t=21.7311s
    mean | MR=1ch | seed=1 | MAE=1.0229e-06 | t=0.0040s
    nearest | MR=1ch | seed=1 | MAE=1.1352e-06 | t=0.0033s
    tikhonov | MR=1ch | seed=1 | MAE=5.1032e-06 | t=0.0190s
    tv | MR=1ch | seed=1 | MAE=1.0121e-06 | t=0.4414s
    trss | MR=1ch | seed=1 | MAE=4.9389e-07 | t=0.4524s

Completed: 2026-04-16T14:54:36.283724+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.