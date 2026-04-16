# Integration Log: scr_00520
Started: 2026-04-16T13:59:23.083343+00:00
Description: Screening scr_00520 ds=bci_iv2a_real_s2 graph=vknng miss=[0.2] mode=base

## Dataset: bci_iv2a_real_s2 | rows=14
  Graph: vknng built OK
    mean | MR=0.2 | seed=0 | MAE=8.7638e-07 | t=0.0030s
    nearest | MR=0.2 | seed=0 | MAE=8.0037e-07 | t=0.0079s
    tikhonov | MR=0.2 | seed=0 | MAE=1.5706e-06 | t=0.0092s
    tv | MR=0.2 | seed=0 | MAE=8.7645e-07 | t=0.4380s
    trss | MR=0.2 | seed=0 | MAE=8.1409e-07 | t=0.2003s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=4.5078e-06 | t=0.0122s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.1483e-05 | t=24.8713s
    mean | MR=0.2 | seed=1 | MAE=9.0508e-07 | t=0.0021s
    nearest | MR=0.2 | seed=1 | MAE=8.8678e-07 | t=0.0060s
    tikhonov | MR=0.2 | seed=1 | MAE=1.5874e-06 | t=0.0058s
    tv | MR=0.2 | seed=1 | MAE=9.0511e-07 | t=0.1444s
    trss | MR=0.2 | seed=1 | MAE=8.3347e-07 | t=0.0189s

Completed: 2026-04-16T13:59:23.084117+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.