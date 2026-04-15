# Integration Log: it150_099
Started: 2026-04-15T00:39:39.740667+00:00
Description: Bulk normalized run it150_099 dataset=bci_iv2a_real_s1 graph=knn miss=[0.2] mode=base

## Dataset: bci_iv2a_real_s1 | rows=42
  Graph: knn__k3 built OK
    mean | MR=0.2 | seed=0 | MAE=6.9320e-02 | t=0.0020s
    nearest | MR=0.2 | seed=0 | MAE=6.3326e-02 | t=0.0053s
    tikhonov | MR=0.2 | seed=0 | MAE=1.5644e-01 | t=0.0080s
    tv | MR=0.2 | seed=0 | MAE=6.9312e-02 | t=0.1922s
    trss | MR=0.2 | seed=0 | MAE=4.8425e-02 | t=0.0197s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.8044e-01 | t=0.0114s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=4.6048e-01 | t=1.9305s
    mean | MR=0.2 | seed=1 | MAE=6.8278e-02 | t=0.0032s
    nearest | MR=0.2 | seed=1 | MAE=6.1642e-02 | t=0.0044s
    tikhonov | MR=0.2 | seed=1 | MAE=1.5474e-01 | t=0.0075s
    tv | MR=0.2 | seed=1 | MAE=6.8271e-02 | t=0.1856s
    trss | MR=0.2 | seed=1 | MAE=4.8623e-02 | t=0.0198s

Completed: 2026-04-15T00:39:39.742536+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.