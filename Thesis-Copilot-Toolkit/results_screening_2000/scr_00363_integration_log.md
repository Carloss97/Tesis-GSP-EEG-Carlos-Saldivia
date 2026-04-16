# Integration Log: scr_00363
Started: 2026-04-16T13:08:41.470945+00:00
Description: Screening scr_00363 ds=bci_iv2a_real_s1 graph=gaussian miss=[0.1] mode=base

## Dataset: bci_iv2a_real_s1 | rows=14
  Graph: gaussian__sigma1.0 built OK
    mean | MR=0.1 | seed=0 | MAE=1.3025e-06 | t=0.0020s
    nearest | MR=0.1 | seed=0 | MAE=1.3708e-06 | t=0.0027s
    tikhonov | MR=0.1 | seed=0 | MAE=1.0252e-05 | t=0.0057s
    tv | MR=0.1 | seed=0 | MAE=1.3025e-06 | t=0.1962s
    trss | MR=0.1 | seed=0 | MAE=8.8942e-07 | t=0.0218s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=1.3119e-05 | t=0.0083s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=1.8943e-05 | t=7.7367s
    mean | MR=0.1 | seed=1 | MAE=1.2372e-06 | t=0.0020s
    nearest | MR=0.1 | seed=1 | MAE=1.2545e-06 | t=0.0028s
    tikhonov | MR=0.1 | seed=1 | MAE=1.0262e-05 | t=0.0064s
    tv | MR=0.1 | seed=1 | MAE=1.2372e-06 | t=0.1842s
    trss | MR=0.1 | seed=1 | MAE=8.3377e-07 | t=0.0167s

Completed: 2026-04-16T13:08:41.471778+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.