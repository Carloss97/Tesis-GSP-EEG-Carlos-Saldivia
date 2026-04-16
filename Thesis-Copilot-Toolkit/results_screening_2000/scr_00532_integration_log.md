# Integration Log: scr_00532
Started: 2026-04-16T14:03:55.284588+00:00
Description: Screening scr_00532 ds=bci_iv2a_real_s2 graph=aew miss=[0.2] mode=base

## Dataset: bci_iv2a_real_s2 | rows=14
  Graph: aew built OK
    mean | MR=0.2 | seed=0 | MAE=8.7638e-07 | t=0.0031s
    nearest | MR=0.2 | seed=0 | MAE=8.0037e-07 | t=0.0079s
    tikhonov | MR=0.2 | seed=0 | MAE=1.8692e-06 | t=0.0120s
    tv | MR=0.2 | seed=0 | MAE=8.7636e-07 | t=0.3264s
    trss | MR=0.2 | seed=0 | MAE=7.6557e-07 | t=0.2644s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=4.7231e-06 | t=0.0440s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.3890e-05 | t=12.5807s
    mean | MR=0.2 | seed=1 | MAE=9.0508e-07 | t=0.0021s
    nearest | MR=0.2 | seed=1 | MAE=8.8678e-07 | t=0.0076s
    tikhonov | MR=0.2 | seed=1 | MAE=1.8857e-06 | t=0.0057s
    tv | MR=0.2 | seed=1 | MAE=9.0503e-07 | t=0.1772s
    trss | MR=0.2 | seed=1 | MAE=7.8787e-07 | t=0.0206s

Completed: 2026-04-16T14:03:55.297612+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.