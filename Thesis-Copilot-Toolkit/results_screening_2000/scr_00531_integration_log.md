# Integration Log: scr_00531
Started: 2026-04-16T14:03:21.656962+00:00
Description: Screening scr_00531 ds=bci_iv2a_real_s1 graph=aew miss=[0.2] mode=base

## Dataset: bci_iv2a_real_s1 | rows=14
  Graph: aew built OK
    mean | MR=0.2 | seed=0 | MAE=3.0357e-06 | t=0.0030s
    nearest | MR=0.2 | seed=0 | MAE=3.2140e-06 | t=0.0080s
    tikhonov | MR=0.2 | seed=0 | MAE=4.9109e-06 | t=0.0160s
    tv | MR=0.2 | seed=0 | MAE=3.0304e-06 | t=0.3458s
    trss | MR=0.2 | seed=0 | MAE=2.2223e-06 | t=0.0341s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=8.2815e-06 | t=0.0170s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.4651e-05 | t=18.4079s
    mean | MR=0.2 | seed=1 | MAE=3.3734e-06 | t=0.0032s
    nearest | MR=0.2 | seed=1 | MAE=3.5344e-06 | t=0.0279s
    tikhonov | MR=0.2 | seed=1 | MAE=5.2222e-06 | t=0.0094s
    tv | MR=0.2 | seed=1 | MAE=3.3689e-06 | t=0.3910s
    trss | MR=0.2 | seed=1 | MAE=2.5347e-06 | t=0.6651s

Completed: 2026-04-16T14:03:21.657837+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.