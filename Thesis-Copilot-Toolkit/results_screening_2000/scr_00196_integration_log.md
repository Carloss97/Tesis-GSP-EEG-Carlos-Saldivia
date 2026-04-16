# Integration Log: scr_00196
Started: 2026-04-16T14:25:48.968094+00:00
Description: Screening scr_00196 ds=bci_iv2a_real_s2 graph=vknng miss=2ch mode=base

## Dataset: bci_iv2a_real_s2 | rows=14
  Graph: vknng built OK
    mean | MR=2ch | seed=0 | MAE=3.3429e-07 | t=0.0031s
    nearest | MR=2ch | seed=0 | MAE=3.2237e-07 | t=0.0043s
    tikhonov | MR=2ch | seed=0 | MAE=1.1172e-06 | t=0.0086s
    tv | MR=2ch | seed=0 | MAE=3.3429e-07 | t=0.4287s
    trss | MR=2ch | seed=0 | MAE=2.9132e-07 | t=0.6248s
    graph_time_tikhonov | MR=2ch | seed=0 | MAE=4.3405e-06 | t=0.0777s
    temporal_laplacian | MR=2ch | seed=0 | MAE=1.0601e-05 | t=24.4832s
    mean | MR=2ch | seed=1 | MAE=3.4821e-07 | t=0.0023s
    nearest | MR=2ch | seed=1 | MAE=3.1417e-07 | t=0.0034s
    tikhonov | MR=2ch | seed=1 | MAE=1.1236e-06 | t=0.0100s
    tv | MR=2ch | seed=1 | MAE=3.4820e-07 | t=0.4237s
    trss | MR=2ch | seed=1 | MAE=3.0153e-07 | t=0.2088s

Completed: 2026-04-16T14:25:48.968964+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.