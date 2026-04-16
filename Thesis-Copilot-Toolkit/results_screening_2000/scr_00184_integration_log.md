# Integration Log: scr_00184
Started: 2026-04-16T14:19:36.272210+00:00
Description: Screening scr_00184 ds=bci_iv2a_real_s2 graph=knng miss=2ch mode=base

## Dataset: bci_iv2a_real_s2 | rows=14
  Graph: knng built OK
    mean | MR=2ch | seed=0 | MAE=3.3429e-07 | t=0.0062s
    nearest | MR=2ch | seed=0 | MAE=3.2237e-07 | t=0.0043s
    tikhonov | MR=2ch | seed=0 | MAE=1.6128e-06 | t=0.0738s
    tv | MR=2ch | seed=0 | MAE=3.3430e-07 | t=0.3467s
    trss | MR=2ch | seed=0 | MAE=2.7686e-07 | t=0.6519s
    graph_time_tikhonov | MR=2ch | seed=0 | MAE=4.7229e-06 | t=0.0701s
    temporal_laplacian | MR=2ch | seed=0 | MAE=1.3609e-05 | t=27.8961s
    mean | MR=2ch | seed=1 | MAE=3.4821e-07 | t=0.0033s
    nearest | MR=2ch | seed=1 | MAE=3.1417e-07 | t=0.0166s
    tikhonov | MR=2ch | seed=1 | MAE=1.6192e-06 | t=0.0109s
    tv | MR=2ch | seed=1 | MAE=3.4820e-07 | t=0.4800s
    trss | MR=2ch | seed=1 | MAE=2.8357e-07 | t=0.4440s

Completed: 2026-04-16T14:19:36.273180+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.