# Integration Log: scr_00497
Started: 2026-04-16T13:50:55.838074+00:00
Description: Screening scr_00497 ds=bci_iv2a_real_s3 graph=kalofolias miss=[0.2] mode=base

## Dataset: bci_iv2a_real_s3 | rows=14
  Graph: kalofolias built OK
    mean | MR=0.2 | seed=0 | MAE=7.3135e-07 | t=0.0020s
    nearest | MR=0.2 | seed=0 | MAE=6.4516e-07 | t=0.0055s
    tikhonov | MR=0.2 | seed=0 | MAE=1.8319e-06 | t=0.0057s
    tv | MR=0.2 | seed=0 | MAE=7.3135e-07 | t=0.1923s
    trss | MR=0.2 | seed=0 | MAE=5.4944e-07 | t=0.0177s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.8951e-06 | t=0.0078s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=5.7707e-06 | t=13.6722s
    mean | MR=0.2 | seed=1 | MAE=7.3458e-07 | t=0.0030s
    nearest | MR=0.2 | seed=1 | MAE=6.4235e-07 | t=0.0086s
    tikhonov | MR=0.2 | seed=1 | MAE=1.8316e-06 | t=0.0312s
    tv | MR=0.2 | seed=1 | MAE=7.3458e-07 | t=0.3064s
    trss | MR=0.2 | seed=1 | MAE=5.5970e-07 | t=0.0201s

Completed: 2026-04-16T13:50:55.838905+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.