# Integration Log: scr_00567
Started: 2026-04-16T14:18:35.202503+00:00
Description: Screening scr_00567 ds=bci_iv2a_real_s1 graph=knn miss=[0.3] mode=base

## Dataset: bci_iv2a_real_s1 | rows=14
  Graph: knn__k7 built OK
    mean | MR=0.3 | seed=0 | MAE=4.4732e-06 | t=0.0247s
    nearest | MR=0.3 | seed=0 | MAE=4.7753e-06 | t=0.0105s
    tikhonov | MR=0.3 | seed=0 | MAE=8.8549e-06 | t=0.0099s
    tv | MR=0.3 | seed=0 | MAE=4.4729e-06 | t=0.7002s
    trss | MR=0.3 | seed=0 | MAE=3.1355e-06 | t=0.3242s
    graph_time_tikhonov | MR=0.3 | seed=0 | MAE=1.2412e-05 | t=0.0116s
    temporal_laplacian | MR=0.3 | seed=0 | MAE=1.7869e-05 | t=25.1019s
    mean | MR=0.3 | seed=1 | MAE=4.4548e-06 | t=0.0031s
    nearest | MR=0.3 | seed=1 | MAE=4.6851e-06 | t=0.0103s
    tikhonov | MR=0.3 | seed=1 | MAE=8.7954e-06 | t=0.0095s
    tv | MR=0.3 | seed=1 | MAE=4.4545e-06 | t=0.7821s
    trss | MR=0.3 | seed=1 | MAE=3.1364e-06 | t=0.2422s

Completed: 2026-04-16T14:18:35.203360+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.