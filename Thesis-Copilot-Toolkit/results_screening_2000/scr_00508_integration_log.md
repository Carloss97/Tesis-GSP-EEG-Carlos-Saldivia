# Integration Log: scr_00508
Started: 2026-04-16T13:54:44.116151+00:00
Description: Screening scr_00508 ds=bci_iv2a_real_s2 graph=knng miss=[0.2] mode=base

## Dataset: bci_iv2a_real_s2 | rows=14
  Graph: knng built OK
    mean | MR=0.2 | seed=0 | MAE=8.7638e-07 | t=0.0020s
    nearest | MR=0.2 | seed=0 | MAE=8.0037e-07 | t=0.0056s
    tikhonov | MR=0.2 | seed=0 | MAE=1.9900e-06 | t=0.0057s
    tv | MR=0.2 | seed=0 | MAE=8.7643e-07 | t=0.1520s
    trss | MR=0.2 | seed=0 | MAE=7.6834e-07 | t=0.0189s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=4.8418e-06 | t=0.0079s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.4226e-05 | t=15.9349s
    mean | MR=0.2 | seed=1 | MAE=9.0508e-07 | t=0.0032s
    nearest | MR=0.2 | seed=1 | MAE=8.8678e-07 | t=0.0078s
    tikhonov | MR=0.2 | seed=1 | MAE=2.0023e-06 | t=0.0111s
    tv | MR=0.2 | seed=1 | MAE=9.0511e-07 | t=0.2803s
    trss | MR=0.2 | seed=1 | MAE=7.9152e-07 | t=0.0423s

Completed: 2026-04-16T13:54:44.117174+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.