# Integration Log: scr_00400
Started: 2026-04-16T13:17:46.081116+00:00
Description: Screening scr_00400 ds=bci_iv2a_real_s2 graph=knng miss=[0.1] mode=base

## Dataset: bci_iv2a_real_s2 | rows=14
  Graph: knng built OK
    mean | MR=0.1 | seed=0 | MAE=3.3429e-07 | t=0.0030s
    nearest | MR=0.1 | seed=0 | MAE=3.2237e-07 | t=0.0042s
    tikhonov | MR=0.1 | seed=0 | MAE=1.6128e-06 | t=0.0085s
    tv | MR=0.1 | seed=0 | MAE=3.3430e-07 | t=0.4304s
    trss | MR=0.1 | seed=0 | MAE=2.7686e-07 | t=0.3316s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=4.7229e-06 | t=0.0125s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=1.3609e-05 | t=8.2005s
    mean | MR=0.1 | seed=1 | MAE=3.4821e-07 | t=0.0021s
    nearest | MR=0.1 | seed=1 | MAE=3.1417e-07 | t=0.0029s
    tikhonov | MR=0.1 | seed=1 | MAE=1.6192e-06 | t=0.0069s
    tv | MR=0.1 | seed=1 | MAE=3.4820e-07 | t=0.1516s
    trss | MR=0.1 | seed=1 | MAE=2.8357e-07 | t=0.2246s

Completed: 2026-04-16T13:17:46.081967+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.