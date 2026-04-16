# Integration Log: scr_01419
Started: 2026-04-16T08:46:14.745230+00:00
Description: Screening scr_01419 ds=bci_iv2a_real_s1 graph=knn miss=[0.4] mode=lambda

## Dataset: bci_iv2a_real_s1 | rows=24
  Graph: knn__k5 built OK
    tv | MR=0.2 | seed=0 | MAE=6.9295e-02 | t=0.1537s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.6344e-01 | t=0.0081s
    trss | MR=0.2 | seed=0 | MAE=1.7096e-02 | t=0.0194s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.8026e-01 | t=1.3367s
    tv | MR=0.2 | seed=1 | MAE=6.8260e-02 | t=0.1538s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=1.6177e-01 | t=0.0081s
    trss | MR=0.2 | seed=1 | MAE=1.7229e-02 | t=0.0197s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=2.8037e-01 | t=1.2975s
    tv | MR=0.2 | seed=0 | MAE=6.9307e-02 | t=0.1522s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.0520e-01 | t=0.0081s
    trss | MR=0.2 | seed=0 | MAE=2.2070e-02 | t=0.0197s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=3.4443e-01 | t=1.3066s

Completed: 2026-04-16T08:46:14.745968+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.