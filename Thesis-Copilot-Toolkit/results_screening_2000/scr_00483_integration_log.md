# Integration Log: scr_00483
Started: 2026-04-16T13:45:41.616270+00:00
Description: Screening scr_00483 ds=bci_iv2a_real_s1 graph=gaussian miss=[0.2] mode=base

## Dataset: bci_iv2a_real_s1 | rows=14
  Graph: gaussian__sigma0.6 built OK
    mean | MR=0.2 | seed=0 | MAE=3.0357e-06 | t=0.0023s
    nearest | MR=0.2 | seed=0 | MAE=3.2140e-06 | t=0.0053s
    tikhonov | MR=0.2 | seed=0 | MAE=1.0984e-05 | t=0.0058s
    tv | MR=0.2 | seed=0 | MAE=3.0357e-06 | t=0.2192s
    trss | MR=0.2 | seed=0 | MAE=2.1670e-06 | t=0.0211s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.3469e-05 | t=0.0172s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.9229e-05 | t=15.2993s
    mean | MR=0.2 | seed=1 | MAE=3.3734e-06 | t=0.0030s
    nearest | MR=0.2 | seed=1 | MAE=3.5344e-06 | t=0.0088s
    tikhonov | MR=0.2 | seed=1 | MAE=1.0983e-05 | t=0.0117s
    tv | MR=0.2 | seed=1 | MAE=3.3734e-06 | t=0.4149s
    trss | MR=0.2 | seed=1 | MAE=2.4631e-06 | t=0.3800s

Completed: 2026-04-16T13:45:41.617241+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.