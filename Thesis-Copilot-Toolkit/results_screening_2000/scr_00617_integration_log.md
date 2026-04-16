# Integration Log: scr_00617
Started: 2026-04-16T14:44:21.857565+00:00
Description: Screening scr_00617 ds=bci_iv2a_real_s3 graph=knng miss=[0.3] mode=base

## Dataset: bci_iv2a_real_s3 | rows=14
  Graph: knng built OK
    mean | MR=0.3 | seed=0 | MAE=1.0520e-06 | t=0.0030s
    nearest | MR=0.3 | seed=0 | MAE=9.1472e-07 | t=0.0909s
    tikhonov | MR=0.3 | seed=0 | MAE=1.9138e-06 | t=0.0087s
    tv | MR=0.3 | seed=0 | MAE=1.0521e-06 | t=0.5806s
    trss | MR=0.3 | seed=0 | MAE=9.4286e-07 | t=0.2635s
    graph_time_tikhonov | MR=0.3 | seed=0 | MAE=2.8116e-06 | t=0.0125s
    temporal_laplacian | MR=0.3 | seed=0 | MAE=5.6951e-06 | t=21.5895s
    mean | MR=0.3 | seed=1 | MAE=1.0248e-06 | t=0.0020s
    nearest | MR=0.3 | seed=1 | MAE=9.0879e-07 | t=0.0065s
    tikhonov | MR=0.3 | seed=1 | MAE=1.9065e-06 | t=0.0150s
    tv | MR=0.3 | seed=1 | MAE=1.0249e-06 | t=0.1994s
    trss | MR=0.3 | seed=1 | MAE=9.4321e-07 | t=0.4427s

Completed: 2026-04-16T14:44:21.858433+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.