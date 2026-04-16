# Integration Log: scr_00304
Started: 2026-04-16T15:22:23.128711+00:00
Description: Screening scr_00304 ds=bci_iv2a_real_s2 graph=vknng miss=3ch mode=base

## Dataset: bci_iv2a_real_s2 | rows=14
  Graph: vknng built OK
    mean | MR=3ch | seed=0 | MAE=5.2945e-07 | t=0.0033s
    nearest | MR=3ch | seed=0 | MAE=5.1829e-07 | t=0.0085s
    tikhonov | MR=3ch | seed=0 | MAE=1.2737e-06 | t=0.0202s
    tv | MR=3ch | seed=0 | MAE=5.2946e-07 | t=0.6434s
    trss | MR=3ch | seed=0 | MAE=4.6627e-07 | t=0.2928s
    graph_time_tikhonov | MR=3ch | seed=0 | MAE=4.4008e-06 | t=0.0469s
    temporal_laplacian | MR=3ch | seed=0 | MAE=1.0877e-05 | t=10.5624s
    mean | MR=3ch | seed=1 | MAE=5.2909e-07 | t=0.0036s
    nearest | MR=3ch | seed=1 | MAE=4.9473e-07 | t=0.0272s
    tikhonov | MR=3ch | seed=1 | MAE=1.2836e-06 | t=0.0386s
    tv | MR=3ch | seed=1 | MAE=5.2911e-07 | t=0.3839s
    trss | MR=3ch | seed=1 | MAE=4.6934e-07 | t=0.1212s

Completed: 2026-04-16T15:22:23.129989+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.