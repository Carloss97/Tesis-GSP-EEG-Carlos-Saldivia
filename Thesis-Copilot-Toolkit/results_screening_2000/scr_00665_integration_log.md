# Integration Log: scr_00665
Started: 2026-04-16T15:08:49.334884+00:00
Description: Screening scr_00665 ds=bci_iv2a_real_s3 graph=knn miss=[0.4] mode=base

## Dataset: bci_iv2a_real_s3 | rows=14
  Graph: knn__k5 built OK
    mean | MR=0.4 | seed=0 | MAE=1.4549e-06 | t=0.0048s
    nearest | MR=0.4 | seed=0 | MAE=1.3679e-06 | t=0.0138s
    tikhonov | MR=0.4 | seed=0 | MAE=2.2977e-06 | t=0.0090s
    tv | MR=0.4 | seed=0 | MAE=1.4549e-06 | t=0.6818s
    trss | MR=0.4 | seed=0 | MAE=1.3335e-06 | t=0.2523s
    graph_time_tikhonov | MR=0.4 | seed=0 | MAE=3.0267e-06 | t=0.0384s
    temporal_laplacian | MR=0.4 | seed=0 | MAE=6.0477e-06 | t=26.6512s
    mean | MR=0.4 | seed=1 | MAE=1.4638e-06 | t=0.0188s
    nearest | MR=0.4 | seed=1 | MAE=1.3378e-06 | t=0.0511s
    tikhonov | MR=0.4 | seed=1 | MAE=2.3062e-06 | t=0.0094s
    tv | MR=0.4 | seed=1 | MAE=1.4638e-06 | t=0.6513s
    trss | MR=0.4 | seed=1 | MAE=1.3409e-06 | t=0.6873s

Completed: 2026-04-16T15:08:49.335756+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.