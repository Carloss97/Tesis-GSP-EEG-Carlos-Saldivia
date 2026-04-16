# Integration Log: scr_00604
Started: 2026-04-16T14:37:26.029829+00:00
Description: Screening scr_00604 ds=bci_iv2a_real_s2 graph=kalofolias miss=[0.3] mode=base

## Dataset: bci_iv2a_real_s2 | rows=14
  Graph: kalofolias built OK
    mean | MR=0.3 | seed=0 | MAE=1.2424e-06 | t=0.0030s
    nearest | MR=0.3 | seed=0 | MAE=1.2061e-06 | t=0.1058s
    tikhonov | MR=0.3 | seed=0 | MAE=2.4047e-06 | t=0.0087s
    tv | MR=0.3 | seed=0 | MAE=1.2424e-06 | t=0.4936s
    trss | MR=0.3 | seed=0 | MAE=9.6068e-07 | t=0.0201s
    graph_time_tikhonov | MR=0.3 | seed=0 | MAE=5.0833e-06 | t=0.0096s
    temporal_laplacian | MR=0.3 | seed=0 | MAE=1.5566e-05 | t=12.9544s
    mean | MR=0.3 | seed=1 | MAE=1.2418e-06 | t=0.0032s
    nearest | MR=0.3 | seed=1 | MAE=1.1920e-06 | t=0.0109s
    tikhonov | MR=0.3 | seed=1 | MAE=2.4179e-06 | t=0.0094s
    tv | MR=0.3 | seed=1 | MAE=1.2418e-06 | t=1.0996s
    trss | MR=0.3 | seed=1 | MAE=9.5377e-07 | t=0.3233s

Completed: 2026-04-16T14:37:26.030689+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.