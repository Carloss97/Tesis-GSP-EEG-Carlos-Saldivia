# Integration Log: it150_015
Started: 2026-04-15T00:24:23.008345+00:00
Description: Bulk normalized run it150_015 dataset=bci_iv2a_real_s1 graph=knn miss=[0.1] mode=base

## Dataset: bci_iv2a_real_s1 | rows=42
  Graph: knn__k5 built OK
    mean | MR=0.1 | seed=0 | MAE=3.5667e-02 | t=0.0020s
    nearest | MR=0.1 | seed=0 | MAE=3.1361e-02 | t=0.0040s
    tikhonov | MR=0.1 | seed=0 | MAE=1.7221e-01 | t=0.0087s
    tv | MR=0.1 | seed=0 | MAE=3.5666e-02 | t=0.2683s
    trss | MR=0.1 | seed=0 | MAE=2.5809e-02 | t=0.0180s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=3.0375e-01 | t=0.0115s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=5.0684e-01 | t=3.5200s
    mean | MR=0.1 | seed=1 | MAE=3.3709e-02 | t=0.0028s
    nearest | MR=0.1 | seed=1 | MAE=3.1289e-02 | t=0.0047s
    tikhonov | MR=0.1 | seed=1 | MAE=1.7088e-01 | t=0.0098s
    tv | MR=0.1 | seed=1 | MAE=3.3707e-02 | t=0.2016s
    trss | MR=0.1 | seed=1 | MAE=2.3412e-02 | t=0.0193s

Completed: 2026-04-15T00:24:23.010340+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.