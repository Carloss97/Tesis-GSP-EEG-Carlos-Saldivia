# Integration Log: scr_00605
Started: 2026-04-16T14:38:21.044125+00:00
Description: Screening scr_00605 ds=bci_iv2a_real_s3 graph=kalofolias miss=[0.3] mode=base

## Dataset: bci_iv2a_real_s3 | rows=14
  Graph: kalofolias built OK
    mean | MR=0.3 | seed=0 | MAE=1.0520e-06 | t=0.0036s
    nearest | MR=0.3 | seed=0 | MAE=9.1472e-07 | t=0.0102s
    tikhonov | MR=0.3 | seed=0 | MAE=2.0215e-06 | t=0.0086s
    tv | MR=0.3 | seed=0 | MAE=1.0520e-06 | t=0.2618s
    trss | MR=0.3 | seed=0 | MAE=8.2030e-07 | t=0.0182s
    graph_time_tikhonov | MR=0.3 | seed=0 | MAE=2.9596e-06 | t=0.0078s
    temporal_laplacian | MR=0.3 | seed=0 | MAE=5.8918e-06 | t=20.9467s
    mean | MR=0.3 | seed=1 | MAE=1.0248e-06 | t=0.0032s
    nearest | MR=0.3 | seed=1 | MAE=9.0879e-07 | t=0.0461s
    tikhonov | MR=0.3 | seed=1 | MAE=2.0039e-06 | t=0.0739s
    tv | MR=0.3 | seed=1 | MAE=1.0248e-06 | t=0.8136s
    trss | MR=0.3 | seed=1 | MAE=7.9718e-07 | t=0.9899s

Completed: 2026-04-16T14:38:21.045836+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.