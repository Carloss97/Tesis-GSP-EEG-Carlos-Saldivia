# Integration Log: scr_01634
Started: 2026-04-16T09:15:04.323120+00:00
Description: Screening scr_01634 ds=physionet_real graph=knn miss=2ch mode=noise

## Dataset: physionet_eegmmidb_real | rows=42
  Graph: knn__k5 built OK
    mean | MR=0.2 | seed=0 | MAE=7.8230e-02 | t=0.0020s
    nearest | MR=0.2 | seed=0 | MAE=9.0465e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=0 | MAE=1.3776e-01 | t=0.0057s
    tv | MR=0.2 | seed=0 | MAE=7.7815e-02 | t=0.1490s
    trss | MR=0.2 | seed=0 | MAE=3.9396e-02 | t=0.0191s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.6342e-01 | t=0.0080s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=6.2369e-01 | t=1.3434s
    mean | MR=0.2 | seed=1 | MAE=7.8011e-02 | t=0.0020s
    nearest | MR=0.2 | seed=1 | MAE=8.9030e-02 | t=0.0041s
    tikhonov | MR=0.2 | seed=1 | MAE=1.3801e-01 | t=0.0092s
    tv | MR=0.2 | seed=1 | MAE=7.7596e-02 | t=0.1487s
    trss | MR=0.2 | seed=1 | MAE=3.9132e-02 | t=0.0198s

Completed: 2026-04-16T09:15:04.324011+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.