# Integration Log: scr_00038
Started: 2026-04-16T15:33:55.819914+00:00
Description: Screening scr_00038 ds=physionet_real graph=gaussian miss=1ch mode=base

## Dataset: physionet_eegmmidb_real | rows=14
  Graph: gaussian__sigma1.0 built OK
    mean | MR=1ch | seed=0 | MAE=9.6765e-07 | t=0.0031s
    nearest | MR=1ch | seed=0 | MAE=1.0997e-06 | t=0.0068s
    tikhonov | MR=1ch | seed=0 | MAE=1.6876e-05 | t=0.0230s
    tv | MR=1ch | seed=0 | MAE=9.6764e-07 | t=0.6551s
    trss | MR=1ch | seed=0 | MAE=6.7814e-07 | t=0.0915s
    graph_time_tikhonov | MR=1ch | seed=0 | MAE=2.1902e-05 | t=0.0185s
    temporal_laplacian | MR=1ch | seed=0 | MAE=3.8587e-05 | t=3.7688s
    mean | MR=1ch | seed=1 | MAE=1.0229e-06 | t=0.0100s
    nearest | MR=1ch | seed=1 | MAE=1.1352e-06 | t=0.0058s
    tikhonov | MR=1ch | seed=1 | MAE=1.6890e-05 | t=0.0171s
    tv | MR=1ch | seed=1 | MAE=1.0229e-06 | t=0.6673s
    trss | MR=1ch | seed=1 | MAE=7.1862e-07 | t=0.4081s

Completed: 2026-04-16T15:33:55.821213+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.