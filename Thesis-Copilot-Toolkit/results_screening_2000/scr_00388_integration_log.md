# Integration Log: scr_00388
Started: 2026-04-16T13:14:08.591539+00:00
Description: Screening scr_00388 ds=bci_iv2a_real_s2 graph=kalofolias miss=[0.1] mode=base

## Dataset: bci_iv2a_real_s2 | rows=14
  Graph: kalofolias built OK
    mean | MR=0.1 | seed=0 | MAE=3.3429e-07 | t=0.0030s
    nearest | MR=0.1 | seed=0 | MAE=3.2237e-07 | t=0.0052s
    tikhonov | MR=0.1 | seed=0 | MAE=1.8559e-06 | t=0.0149s
    tv | MR=0.1 | seed=0 | MAE=3.3429e-07 | t=0.7677s
    trss | MR=0.1 | seed=0 | MAE=2.3794e-07 | t=0.3633s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=4.9271e-06 | t=0.0079s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=1.4727e-05 | t=14.4372s
    mean | MR=0.1 | seed=1 | MAE=3.4821e-07 | t=0.0031s
    nearest | MR=0.1 | seed=1 | MAE=3.1417e-07 | t=0.0043s
    tikhonov | MR=0.1 | seed=1 | MAE=1.8665e-06 | t=0.0308s
    tv | MR=0.1 | seed=1 | MAE=3.4821e-07 | t=0.8355s
    trss | MR=0.1 | seed=1 | MAE=2.5203e-07 | t=0.2763s

Completed: 2026-04-16T13:14:08.592470+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.