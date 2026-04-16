# Integration Log: scr_00495
Started: 2026-04-16T13:49:31.866348+00:00
Description: Screening scr_00495 ds=bci_iv2a_real_s1 graph=kalofolias miss=[0.2] mode=base

## Dataset: bci_iv2a_real_s1 | rows=14
  Graph: kalofolias built OK
    mean | MR=0.2 | seed=0 | MAE=3.0357e-06 | t=0.0031s
    nearest | MR=0.2 | seed=0 | MAE=3.2140e-06 | t=0.0077s
    tikhonov | MR=0.2 | seed=0 | MAE=7.7041e-06 | t=0.0120s
    tv | MR=0.2 | seed=0 | MAE=3.0357e-06 | t=0.6446s
    trss | MR=0.2 | seed=0 | MAE=2.1670e-06 | t=0.4612s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.1894e-05 | t=0.0466s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.7120e-05 | t=14.7836s
    mean | MR=0.2 | seed=1 | MAE=3.3734e-06 | t=0.0022s
    nearest | MR=0.2 | seed=1 | MAE=3.5344e-06 | t=0.0089s
    tikhonov | MR=0.2 | seed=1 | MAE=7.8429e-06 | t=0.0111s
    tv | MR=0.2 | seed=1 | MAE=3.3734e-06 | t=0.3897s
    trss | MR=0.2 | seed=1 | MAE=2.4631e-06 | t=0.0251s

Completed: 2026-04-16T13:49:31.867996+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.