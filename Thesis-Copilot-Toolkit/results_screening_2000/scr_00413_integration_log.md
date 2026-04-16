# Integration Log: scr_00413
Started: 2026-04-16T13:22:28.029930+00:00
Description: Screening scr_00413 ds=bci_iv2a_real_s3 graph=vknng miss=[0.1] mode=base

## Dataset: bci_iv2a_real_s3 | rows=14
  Graph: vknng built OK
    mean | MR=0.1 | seed=0 | MAE=3.0419e-07 | t=0.0030s
    nearest | MR=0.1 | seed=0 | MAE=2.4876e-07 | t=0.0043s
    tikhonov | MR=0.1 | seed=0 | MAE=9.9585e-07 | t=0.0087s
    tv | MR=0.1 | seed=0 | MAE=3.0422e-07 | t=0.3215s
    trss | MR=0.1 | seed=0 | MAE=2.8468e-07 | t=0.2377s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=2.1139e-06 | t=0.0128s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=4.1087e-06 | t=19.7210s
    mean | MR=0.1 | seed=1 | MAE=2.8472e-07 | t=0.0030s
    nearest | MR=0.1 | seed=1 | MAE=2.5230e-07 | t=0.0049s
    tikhonov | MR=0.1 | seed=1 | MAE=9.7938e-07 | t=0.0092s
    tv | MR=0.1 | seed=1 | MAE=2.8474e-07 | t=0.2925s
    trss | MR=0.1 | seed=1 | MAE=2.7221e-07 | t=0.0385s

Completed: 2026-04-16T13:22:28.031191+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.