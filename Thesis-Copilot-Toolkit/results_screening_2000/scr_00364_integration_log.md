# Integration Log: scr_00364
Started: 2026-04-16T13:09:04.453974+00:00
Description: Screening scr_00364 ds=bci_iv2a_real_s2 graph=gaussian miss=[0.1] mode=base

## Dataset: bci_iv2a_real_s2 | rows=14
  Graph: gaussian__sigma1.0 built OK
    mean | MR=0.1 | seed=0 | MAE=3.3429e-07 | t=0.0030s
    nearest | MR=0.1 | seed=0 | MAE=3.2237e-07 | t=0.0043s
    tikhonov | MR=0.1 | seed=0 | MAE=2.9248e-06 | t=0.0085s
    tv | MR=0.1 | seed=0 | MAE=3.3429e-07 | t=0.3340s
    trss | MR=0.1 | seed=0 | MAE=2.3794e-07 | t=0.1524s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=5.2994e-06 | t=0.0098s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=1.7103e-05 | t=10.2210s
    mean | MR=0.1 | seed=1 | MAE=3.4821e-07 | t=0.0021s
    nearest | MR=0.1 | seed=1 | MAE=3.1417e-07 | t=0.0028s
    tikhonov | MR=0.1 | seed=1 | MAE=2.9331e-06 | t=0.0057s
    tv | MR=0.1 | seed=1 | MAE=3.4821e-07 | t=0.1969s
    trss | MR=0.1 | seed=1 | MAE=2.5203e-07 | t=0.0171s

Completed: 2026-04-16T13:09:04.455062+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.