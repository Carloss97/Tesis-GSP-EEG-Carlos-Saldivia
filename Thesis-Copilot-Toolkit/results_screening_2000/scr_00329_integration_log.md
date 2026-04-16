# Integration Log: scr_00329
Started: 2026-04-16T15:37:06.226443+00:00
Description: Screening scr_00329 ds=bci_iv2a_real_s3 graph=knn miss=[0.1] mode=base

## Dataset: bci_iv2a_real_s3 | rows=14
  Graph: knn__k3 built OK
    mean | MR=0.1 | seed=0 | MAE=3.0419e-07 | t=0.0032s
    nearest | MR=0.1 | seed=0 | MAE=2.4876e-07 | t=0.0326s
    tikhonov | MR=0.1 | seed=0 | MAE=1.2245e-06 | t=0.0408s
    tv | MR=0.1 | seed=0 | MAE=3.0422e-07 | t=0.5493s
    trss | MR=0.1 | seed=0 | MAE=2.7490e-07 | t=0.2348s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=2.4018e-06 | t=0.0423s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=4.7930e-06 | t=33.8208s
    mean | MR=0.1 | seed=1 | MAE=2.8472e-07 | t=0.0035s
    nearest | MR=0.1 | seed=1 | MAE=2.5230e-07 | t=0.0030s
    tikhonov | MR=0.1 | seed=1 | MAE=1.2060e-06 | t=0.0111s
    tv | MR=0.1 | seed=1 | MAE=2.8474e-07 | t=0.2780s
    trss | MR=0.1 | seed=1 | MAE=2.6659e-07 | t=0.2629s

Completed: 2026-04-16T15:37:06.227755+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.