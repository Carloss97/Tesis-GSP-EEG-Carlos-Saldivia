# Integration Log: it150_111
Started: 2026-04-15T00:41:53.985871+00:00
Description: Bulk normalized run it150_111 dataset=bci_iv2a_real_s1 graph=knn miss=[0.2] mode=base

## Dataset: bci_iv2a_real_s1 | rows=42
  Graph: knn__k5 built OK
    mean | MR=0.2 | seed=0 | MAE=6.9320e-02 | t=0.0020s
    nearest | MR=0.2 | seed=0 | MAE=6.3326e-02 | t=0.0059s
    tikhonov | MR=0.2 | seed=0 | MAE=1.9565e-01 | t=0.0079s
    tv | MR=0.2 | seed=0 | MAE=6.9314e-02 | t=0.2153s
    trss | MR=0.2 | seed=0 | MAE=4.8752e-02 | t=0.0189s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=3.1786e-01 | t=0.0112s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=5.2067e-01 | t=3.7731s
    mean | MR=0.2 | seed=1 | MAE=6.8278e-02 | t=0.0052s
    nearest | MR=0.2 | seed=1 | MAE=6.1642e-02 | t=0.0066s
    tikhonov | MR=0.2 | seed=1 | MAE=1.9320e-01 | t=0.0076s
    tv | MR=0.2 | seed=1 | MAE=6.8274e-02 | t=0.2257s
    trss | MR=0.2 | seed=1 | MAE=4.9043e-02 | t=0.0205s

Completed: 2026-04-15T00:41:53.986981+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.