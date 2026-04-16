# Integration Log: scr_00147
Started: 2026-04-16T15:26:39.458943+00:00
Description: Screening scr_00147 ds=bci_iv2a_real_s1 graph=gaussian miss=2ch mode=base

## Dataset: bci_iv2a_real_s1 | rows=14
  Graph: gaussian__sigma1.0 built OK
    mean | MR=2ch | seed=0 | MAE=1.3025e-06 | t=0.0033s
    nearest | MR=2ch | seed=0 | MAE=1.3708e-06 | t=0.0385s
    tikhonov | MR=2ch | seed=0 | MAE=1.0252e-05 | t=0.0322s
    tv | MR=2ch | seed=0 | MAE=1.3025e-06 | t=0.6935s
    trss | MR=2ch | seed=0 | MAE=8.8942e-07 | t=0.2424s
    graph_time_tikhonov | MR=2ch | seed=0 | MAE=1.3119e-05 | t=0.0489s
    temporal_laplacian | MR=2ch | seed=0 | MAE=1.8943e-05 | t=15.6768s
    mean | MR=2ch | seed=1 | MAE=1.2372e-06 | t=0.0038s
    nearest | MR=2ch | seed=1 | MAE=1.2545e-06 | t=0.0055s
    tikhonov | MR=2ch | seed=1 | MAE=1.0262e-05 | t=0.0097s
    tv | MR=2ch | seed=1 | MAE=1.2372e-06 | t=0.9420s
    trss | MR=2ch | seed=1 | MAE=8.3377e-07 | t=0.1054s

Completed: 2026-04-16T15:26:39.460402+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.