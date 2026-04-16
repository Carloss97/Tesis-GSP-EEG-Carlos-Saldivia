# Integration Log: scr_00639
Started: 2026-04-16T14:54:37.827580+00:00
Description: Screening scr_00639 ds=bci_iv2a_real_s1 graph=aew miss=[0.3] mode=base

## Dataset: bci_iv2a_real_s1 | rows=14
  Graph: aew built OK
    mean | MR=0.3 | seed=0 | MAE=4.4732e-06 | t=0.0336s
    nearest | MR=0.3 | seed=0 | MAE=4.7753e-06 | t=0.1394s
    tikhonov | MR=0.3 | seed=0 | MAE=6.0142e-06 | t=0.0087s
    tv | MR=0.3 | seed=0 | MAE=4.4659e-06 | t=0.3478s
    trss | MR=0.3 | seed=0 | MAE=3.3419e-06 | t=0.3798s
    graph_time_tikhonov | MR=0.3 | seed=0 | MAE=9.0401e-06 | t=0.0240s
    temporal_laplacian | MR=0.3 | seed=0 | MAE=1.5199e-05 | t=24.8135s
    mean | MR=0.3 | seed=1 | MAE=4.4548e-06 | t=0.0030s
    nearest | MR=0.3 | seed=1 | MAE=4.6851e-06 | t=0.0122s
    tikhonov | MR=0.3 | seed=1 | MAE=5.9941e-06 | t=0.0147s
    tv | MR=0.3 | seed=1 | MAE=4.4475e-06 | t=0.9477s
    trss | MR=0.3 | seed=1 | MAE=3.3323e-06 | t=0.0211s

Completed: 2026-04-16T14:54:37.828451+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.