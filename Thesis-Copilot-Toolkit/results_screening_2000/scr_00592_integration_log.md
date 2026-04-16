# Integration Log: scr_00592
Started: 2026-04-16T14:31:20.309620+00:00
Description: Screening scr_00592 ds=bci_iv2a_real_s2 graph=gaussian miss=[0.3] mode=base

## Dataset: bci_iv2a_real_s2 | rows=14
  Graph: gaussian__sigma0.6 built OK
    mean | MR=0.3 | seed=0 | MAE=1.2424e-06 | t=0.0031s
    nearest | MR=0.3 | seed=0 | MAE=1.2061e-06 | t=0.0353s
    tikhonov | MR=0.3 | seed=0 | MAE=3.2213e-06 | t=0.0092s
    tv | MR=0.3 | seed=0 | MAE=1.2424e-06 | t=0.5689s
    trss | MR=0.3 | seed=0 | MAE=9.6068e-07 | t=0.2471s
    graph_time_tikhonov | MR=0.3 | seed=0 | MAE=5.3664e-06 | t=0.0257s
    temporal_laplacian | MR=0.3 | seed=0 | MAE=1.7424e-05 | t=33.3160s
    mean | MR=0.3 | seed=1 | MAE=1.2418e-06 | t=0.0030s
    nearest | MR=0.3 | seed=1 | MAE=1.1920e-06 | t=0.0102s
    tikhonov | MR=0.3 | seed=1 | MAE=3.2441e-06 | t=0.0409s
    tv | MR=0.3 | seed=1 | MAE=1.2418e-06 | t=0.4434s
    trss | MR=0.3 | seed=1 | MAE=9.5377e-07 | t=0.1671s

Completed: 2026-04-16T14:31:20.310721+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.