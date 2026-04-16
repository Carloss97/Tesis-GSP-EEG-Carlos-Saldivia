# Integration Log: scr_00581
Started: 2026-04-16T14:26:24.927642+00:00
Description: Screening scr_00581 ds=bci_iv2a_real_s3 graph=gaussian miss=[0.3] mode=base

## Dataset: bci_iv2a_real_s3 | rows=14
  Graph: gaussian__sigma1.0 built OK
    mean | MR=0.3 | seed=0 | MAE=1.0520e-06 | t=0.0032s
    nearest | MR=0.3 | seed=0 | MAE=9.1472e-07 | t=0.0361s
    tikhonov | MR=0.3 | seed=0 | MAE=2.7025e-06 | t=0.0101s
    tv | MR=0.3 | seed=0 | MAE=1.0520e-06 | t=0.8051s
    trss | MR=0.3 | seed=0 | MAE=8.2030e-07 | t=0.7557s
    graph_time_tikhonov | MR=0.3 | seed=0 | MAE=3.2777e-06 | t=0.0142s
    temporal_laplacian | MR=0.3 | seed=0 | MAE=6.5849e-06 | t=21.8422s
    mean | MR=0.3 | seed=1 | MAE=1.0248e-06 | t=0.0031s
    nearest | MR=0.3 | seed=1 | MAE=9.0879e-07 | t=0.0389s
    tikhonov | MR=0.3 | seed=1 | MAE=2.6917e-06 | t=0.0096s
    tv | MR=0.3 | seed=1 | MAE=1.0248e-06 | t=0.4494s
    trss | MR=0.3 | seed=1 | MAE=7.9718e-07 | t=0.2143s

Completed: 2026-04-16T14:26:24.928533+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.