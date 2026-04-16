# Integration Log: scr_00160
Started: 2026-04-16T15:34:05.863963+00:00
Description: Screening scr_00160 ds=bci_iv2a_real_s2 graph=gaussian miss=2ch mode=base

## Dataset: bci_iv2a_real_s2 | rows=14
  Graph: gaussian__sigma0.6 built OK
    mean | MR=2ch | seed=0 | MAE=3.3429e-07 | t=0.0049s
    nearest | MR=2ch | seed=0 | MAE=3.2237e-07 | t=0.0052s
    tikhonov | MR=2ch | seed=0 | MAE=2.9248e-06 | t=0.0210s
    tv | MR=2ch | seed=0 | MAE=3.3429e-07 | t=0.7474s
    trss | MR=2ch | seed=0 | MAE=2.3794e-07 | t=0.1362s
    graph_time_tikhonov | MR=2ch | seed=0 | MAE=5.2994e-06 | t=0.0131s
    temporal_laplacian | MR=2ch | seed=0 | MAE=1.7103e-05 | t=17.6718s
    mean | MR=2ch | seed=1 | MAE=3.4821e-07 | t=0.0469s
    nearest | MR=2ch | seed=1 | MAE=3.1417e-07 | t=0.0054s
    tikhonov | MR=2ch | seed=1 | MAE=2.9331e-06 | t=0.0091s
    tv | MR=2ch | seed=1 | MAE=3.4821e-07 | t=0.8910s
    trss | MR=2ch | seed=1 | MAE=2.5203e-07 | t=0.2955s

Completed: 2026-04-16T15:34:05.865532+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.