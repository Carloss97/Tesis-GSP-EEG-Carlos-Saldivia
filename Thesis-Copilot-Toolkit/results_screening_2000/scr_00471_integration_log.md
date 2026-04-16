# Integration Log: scr_00471
Started: 2026-04-16T13:41:43.478200+00:00
Description: Screening scr_00471 ds=bci_iv2a_real_s1 graph=gaussian miss=[0.2] mode=base

## Dataset: bci_iv2a_real_s1 | rows=14
  Graph: gaussian__sigma1.0 built OK
    mean | MR=0.2 | seed=0 | MAE=3.0357e-06 | t=0.0030s
    nearest | MR=0.2 | seed=0 | MAE=3.2140e-06 | t=0.0077s
    tikhonov | MR=0.2 | seed=0 | MAE=1.0984e-05 | t=0.0158s
    tv | MR=0.2 | seed=0 | MAE=3.0357e-06 | t=0.6201s
    trss | MR=0.2 | seed=0 | MAE=2.1670e-06 | t=0.1386s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.3469e-05 | t=0.0331s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.9229e-05 | t=10.3981s
    mean | MR=0.2 | seed=1 | MAE=3.3734e-06 | t=0.0020s
    nearest | MR=0.2 | seed=1 | MAE=3.5344e-06 | t=0.0050s
    tikhonov | MR=0.2 | seed=1 | MAE=1.0983e-05 | t=0.0057s
    tv | MR=0.2 | seed=1 | MAE=3.3734e-06 | t=0.2506s
    trss | MR=0.2 | seed=1 | MAE=2.4631e-06 | t=0.1474s

Completed: 2026-04-16T13:41:43.479103+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.