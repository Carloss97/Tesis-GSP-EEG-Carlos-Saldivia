# Integration Log: scr_00256
Started: 2026-04-16T14:56:33.134860+00:00
Description: Screening scr_00256 ds=bci_iv2a_real_s2 graph=gaussian miss=3ch mode=base

## Dataset: bci_iv2a_real_s2 | rows=14
  Graph: gaussian__sigma1.0 built OK
    mean | MR=3ch | seed=0 | MAE=5.2945e-07 | t=0.0046s
    nearest | MR=3ch | seed=0 | MAE=5.1829e-07 | t=0.0064s
    tikhonov | MR=3ch | seed=0 | MAE=2.9925e-06 | t=0.0515s
    tv | MR=3ch | seed=0 | MAE=5.2945e-07 | t=0.9554s
    trss | MR=3ch | seed=0 | MAE=3.8275e-07 | t=0.4350s
    graph_time_tikhonov | MR=3ch | seed=0 | MAE=5.3107e-06 | t=0.0414s
    temporal_laplacian | MR=3ch | seed=0 | MAE=1.7165e-05 | t=25.0660s
    mean | MR=3ch | seed=1 | MAE=5.2909e-07 | t=0.0048s
    nearest | MR=3ch | seed=1 | MAE=4.9473e-07 | t=0.0054s
    tikhonov | MR=3ch | seed=1 | MAE=2.9910e-06 | t=0.0460s
    tv | MR=3ch | seed=1 | MAE=5.2909e-07 | t=0.6549s
    trss | MR=3ch | seed=1 | MAE=3.8330e-07 | t=0.5636s

Completed: 2026-04-16T14:56:33.135882+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.