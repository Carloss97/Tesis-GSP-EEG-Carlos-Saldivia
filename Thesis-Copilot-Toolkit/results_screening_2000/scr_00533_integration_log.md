# Integration Log: scr_00533
Started: 2026-04-16T14:04:31.594127+00:00
Description: Screening scr_00533 ds=bci_iv2a_real_s3 graph=aew miss=[0.2] mode=base

## Dataset: bci_iv2a_real_s3 | rows=14
  Graph: aew built OK
    mean | MR=0.2 | seed=0 | MAE=7.3135e-07 | t=0.0041s
    nearest | MR=0.2 | seed=0 | MAE=6.4516e-07 | t=0.0079s
    tikhonov | MR=0.2 | seed=0 | MAE=1.4653e-06 | t=0.0060s
    tv | MR=0.2 | seed=0 | MAE=7.3133e-07 | t=0.6018s
    trss | MR=0.2 | seed=0 | MAE=6.5165e-07 | t=0.2727s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.4425e-06 | t=0.0645s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=5.0503e-06 | t=18.1216s
    mean | MR=0.2 | seed=1 | MAE=7.3458e-07 | t=0.0031s
    nearest | MR=0.2 | seed=1 | MAE=6.4235e-07 | t=0.0152s
    tikhonov | MR=0.2 | seed=1 | MAE=1.4636e-06 | t=0.0085s
    tv | MR=0.2 | seed=1 | MAE=7.3456e-07 | t=0.1565s
    trss | MR=0.2 | seed=1 | MAE=6.5991e-07 | t=0.0182s

Completed: 2026-04-16T14:04:31.595448+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.