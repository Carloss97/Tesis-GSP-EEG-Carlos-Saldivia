# Integration Log: scr_00171
Started: 2026-04-16T15:39:25.436873+00:00
Description: Screening scr_00171 ds=bci_iv2a_real_s1 graph=kalofolias miss=2ch mode=base

## Dataset: bci_iv2a_real_s1 | rows=14
  Graph: kalofolias built OK
    mean | MR=2ch | seed=0 | MAE=1.3025e-06 | t=0.0042s
    nearest | MR=2ch | seed=0 | MAE=1.3708e-06 | t=0.0150s
    tikhonov | MR=2ch | seed=0 | MAE=6.5591e-06 | t=0.1081s
    tv | MR=2ch | seed=0 | MAE=1.3025e-06 | t=2.0432s
    trss | MR=2ch | seed=0 | MAE=8.8942e-07 | t=0.1312s
    graph_time_tikhonov | MR=2ch | seed=0 | MAE=1.1339e-05 | t=0.0920s
    temporal_laplacian | MR=2ch | seed=0 | MAE=1.6525e-05 | t=15.7085s
    mean | MR=2ch | seed=1 | MAE=1.2372e-06 | t=0.0040s
    nearest | MR=2ch | seed=1 | MAE=1.2545e-06 | t=0.0054s
    tikhonov | MR=2ch | seed=1 | MAE=6.5380e-06 | t=0.0484s
    tv | MR=2ch | seed=1 | MAE=1.2372e-06 | t=1.1161s
    trss | MR=2ch | seed=1 | MAE=8.3377e-07 | t=0.0795s

Completed: 2026-04-16T15:39:25.438633+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.