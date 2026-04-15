# Integration Log: it150_016
Started: 2026-04-15T00:24:42.908159+00:00
Description: Bulk normalized run it150_016 dataset=bci_iv2a_real_s2 graph=knn miss=[0.1] mode=base

## Dataset: bci_iv2a_real_s2 | rows=42
  Graph: knn__k5 built OK
    mean | MR=0.1 | seed=0 | MAE=1.3831e-02 | t=0.0023s
    nearest | MR=0.1 | seed=0 | MAE=1.3215e-02 | t=0.0034s
    tikhonov | MR=0.1 | seed=0 | MAE=7.4636e-02 | t=0.0072s
    tv | MR=0.1 | seed=0 | MAE=1.3832e-02 | t=0.1995s
    trss | MR=0.1 | seed=0 | MAE=1.1213e-02 | t=0.0185s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=2.0184e-01 | t=0.0116s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=6.0615e-01 | t=1.7791s
    mean | MR=0.1 | seed=1 | MAE=1.4351e-02 | t=0.0026s
    nearest | MR=0.1 | seed=1 | MAE=1.2774e-02 | t=0.0040s
    tikhonov | MR=0.1 | seed=1 | MAE=7.4907e-02 | t=0.0073s
    tv | MR=0.1 | seed=1 | MAE=1.4351e-02 | t=0.2010s
    trss | MR=0.1 | seed=1 | MAE=1.1359e-02 | t=0.0191s

Completed: 2026-04-15T00:24:42.909216+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.