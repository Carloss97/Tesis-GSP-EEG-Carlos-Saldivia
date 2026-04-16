# Integration Log: scr_00148
Started: 2026-04-16T15:27:54.496066+00:00
Description: Screening scr_00148 ds=bci_iv2a_real_s2 graph=gaussian miss=2ch mode=base

## Dataset: bci_iv2a_real_s2 | rows=14
  Graph: gaussian__sigma1.0 built OK
    mean | MR=2ch | seed=0 | MAE=3.3429e-07 | t=0.0044s
    nearest | MR=2ch | seed=0 | MAE=3.2237e-07 | t=0.0049s
    tikhonov | MR=2ch | seed=0 | MAE=2.9248e-06 | t=0.0450s
    tv | MR=2ch | seed=0 | MAE=3.3429e-07 | t=1.3438s
    trss | MR=2ch | seed=0 | MAE=2.3794e-07 | t=0.1240s
    graph_time_tikhonov | MR=2ch | seed=0 | MAE=5.2994e-06 | t=0.0243s
    temporal_laplacian | MR=2ch | seed=0 | MAE=1.7103e-05 | t=28.5671s
    mean | MR=2ch | seed=1 | MAE=3.4821e-07 | t=0.0033s
    nearest | MR=2ch | seed=1 | MAE=3.1417e-07 | t=0.0044s
    tikhonov | MR=2ch | seed=1 | MAE=2.9331e-06 | t=0.0118s
    tv | MR=2ch | seed=1 | MAE=3.4821e-07 | t=1.1155s
    trss | MR=2ch | seed=1 | MAE=2.5203e-07 | t=0.3941s

Completed: 2026-04-16T15:27:54.496976+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.