# Integration Log: scr_00641
Started: 2026-04-16T14:56:38.091164+00:00
Description: Screening scr_00641 ds=bci_iv2a_real_s3 graph=aew miss=[0.3] mode=base

## Dataset: bci_iv2a_real_s3 | rows=14
  Graph: aew built OK
    mean | MR=0.3 | seed=0 | MAE=1.0520e-06 | t=0.0031s
    nearest | MR=0.3 | seed=0 | MAE=9.1472e-07 | t=0.0429s
    tikhonov | MR=0.3 | seed=0 | MAE=1.6915e-06 | t=0.0397s
    tv | MR=0.3 | seed=0 | MAE=1.0520e-06 | t=0.5662s
    trss | MR=0.3 | seed=0 | MAE=9.2744e-07 | t=0.2800s
    graph_time_tikhonov | MR=0.3 | seed=0 | MAE=2.5563e-06 | t=0.0126s
    temporal_laplacian | MR=0.3 | seed=0 | MAE=5.2299e-06 | t=26.8714s
    mean | MR=0.3 | seed=1 | MAE=1.0248e-06 | t=0.0036s
    nearest | MR=0.3 | seed=1 | MAE=9.0879e-07 | t=0.0134s
    tikhonov | MR=0.3 | seed=1 | MAE=1.6855e-06 | t=0.0118s
    tv | MR=0.3 | seed=1 | MAE=1.0248e-06 | t=0.3630s
    trss | MR=0.3 | seed=1 | MAE=9.2681e-07 | t=0.8314s

Completed: 2026-04-16T14:56:38.092399+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.