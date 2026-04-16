# Integration Log: scr_00412
Started: 2026-04-16T13:21:49.127980+00:00
Description: Screening scr_00412 ds=bci_iv2a_real_s2 graph=vknng miss=[0.1] mode=base

## Dataset: bci_iv2a_real_s2 | rows=14
  Graph: vknng built OK
    mean | MR=0.1 | seed=0 | MAE=3.3429e-07 | t=0.0032s
    nearest | MR=0.1 | seed=0 | MAE=3.2237e-07 | t=0.0043s
    tikhonov | MR=0.1 | seed=0 | MAE=1.1172e-06 | t=0.0114s
    tv | MR=0.1 | seed=0 | MAE=3.3429e-07 | t=0.8646s
    trss | MR=0.1 | seed=0 | MAE=2.9132e-07 | t=0.3982s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=4.3405e-06 | t=0.0080s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=1.0601e-05 | t=17.3934s
    mean | MR=0.1 | seed=1 | MAE=3.4821e-07 | t=0.0030s
    nearest | MR=0.1 | seed=1 | MAE=3.1417e-07 | t=0.0042s
    tikhonov | MR=0.1 | seed=1 | MAE=1.1236e-06 | t=0.0283s
    tv | MR=0.1 | seed=1 | MAE=3.4820e-07 | t=0.1481s
    trss | MR=0.1 | seed=1 | MAE=3.0153e-07 | t=0.0180s

Completed: 2026-04-16T13:21:49.129221+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.