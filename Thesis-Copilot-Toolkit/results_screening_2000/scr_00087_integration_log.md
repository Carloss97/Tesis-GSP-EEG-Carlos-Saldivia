# Integration Log: scr_00087
Started: 2026-04-16T14:55:23.919749+00:00
Description: Screening scr_00087 ds=bci_iv2a_real_s1 graph=vknng miss=1ch mode=base

## Dataset: bci_iv2a_real_s1 | rows=14
  Graph: vknng built OK
    mean | MR=1ch | seed=0 | MAE=6.8694e-07 | t=0.0036s
    nearest | MR=1ch | seed=0 | MAE=6.7972e-07 | t=0.0099s
    tikhonov | MR=1ch | seed=0 | MAE=3.2814e-06 | t=0.0124s
    tv | MR=1ch | seed=0 | MAE=6.8690e-07 | t=0.5038s
    trss | MR=1ch | seed=0 | MAE=4.9441e-07 | t=0.2468s
    graph_time_tikhonov | MR=1ch | seed=0 | MAE=7.8140e-06 | t=0.0136s
    temporal_laplacian | MR=1ch | seed=0 | MAE=1.2460e-05 | t=19.2305s
    mean | MR=1ch | seed=1 | MAE=6.0230e-07 | t=0.0040s
    nearest | MR=1ch | seed=1 | MAE=6.3859e-07 | t=0.0035s
    tikhonov | MR=1ch | seed=1 | MAE=3.2226e-06 | t=0.0096s
    tv | MR=1ch | seed=1 | MAE=6.0226e-07 | t=0.9671s
    trss | MR=1ch | seed=1 | MAE=4.3285e-07 | t=0.4327s

Completed: 2026-04-16T14:55:23.920642+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.