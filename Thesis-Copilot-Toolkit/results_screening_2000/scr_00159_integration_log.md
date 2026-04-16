# Integration Log: scr_00159
Started: 2026-04-16T15:33:23.263315+00:00
Description: Screening scr_00159 ds=bci_iv2a_real_s1 graph=gaussian miss=2ch mode=base

## Dataset: bci_iv2a_real_s1 | rows=14
  Graph: gaussian__sigma0.6 built OK
    mean | MR=2ch | seed=0 | MAE=1.3025e-06 | t=0.0033s
    nearest | MR=2ch | seed=0 | MAE=1.3708e-06 | t=0.0115s
    tikhonov | MR=2ch | seed=0 | MAE=1.0252e-05 | t=0.0152s
    tv | MR=2ch | seed=0 | MAE=1.3025e-06 | t=0.7437s
    trss | MR=2ch | seed=0 | MAE=8.8942e-07 | t=0.1087s
    graph_time_tikhonov | MR=2ch | seed=0 | MAE=1.3119e-05 | t=0.0260s
    temporal_laplacian | MR=2ch | seed=0 | MAE=1.8943e-05 | t=20.5008s
    mean | MR=2ch | seed=1 | MAE=1.2372e-06 | t=0.0572s
    nearest | MR=2ch | seed=1 | MAE=1.2545e-06 | t=0.0249s
    tikhonov | MR=2ch | seed=1 | MAE=1.0262e-05 | t=0.0282s
    tv | MR=2ch | seed=1 | MAE=1.2372e-06 | t=0.9427s
    trss | MR=2ch | seed=1 | MAE=8.3377e-07 | t=0.2575s

Completed: 2026-04-16T15:33:23.264432+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.