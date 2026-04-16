# Integration Log: scr_00580
Started: 2026-04-16T14:25:24.691344+00:00
Description: Screening scr_00580 ds=bci_iv2a_real_s2 graph=gaussian miss=[0.3] mode=base

## Dataset: bci_iv2a_real_s2 | rows=14
  Graph: gaussian__sigma1.0 built OK
    mean | MR=0.3 | seed=0 | MAE=1.2424e-06 | t=0.0038s
    nearest | MR=0.3 | seed=0 | MAE=1.2061e-06 | t=0.0148s
    tikhonov | MR=0.3 | seed=0 | MAE=3.2213e-06 | t=0.1079s
    tv | MR=0.3 | seed=0 | MAE=1.2424e-06 | t=1.2440s
    trss | MR=0.3 | seed=0 | MAE=9.6068e-07 | t=0.9410s
    graph_time_tikhonov | MR=0.3 | seed=0 | MAE=5.3664e-06 | t=0.0154s
    temporal_laplacian | MR=0.3 | seed=0 | MAE=1.7424e-05 | t=19.0305s
    mean | MR=0.3 | seed=1 | MAE=1.2418e-06 | t=0.0026s
    nearest | MR=0.3 | seed=1 | MAE=1.1920e-06 | t=0.0070s
    tikhonov | MR=0.3 | seed=1 | MAE=3.2441e-06 | t=0.0057s
    tv | MR=0.3 | seed=1 | MAE=1.2418e-06 | t=0.1963s
    trss | MR=0.3 | seed=1 | MAE=9.5377e-07 | t=0.0210s

Completed: 2026-04-16T14:25:24.692624+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.