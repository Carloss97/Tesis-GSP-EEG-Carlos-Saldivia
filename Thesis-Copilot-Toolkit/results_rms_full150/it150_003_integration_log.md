# Integration Log: it150_003
Started: 2026-04-15T00:22:06.293758+00:00
Description: Bulk normalized run it150_003 dataset=bci_iv2a_real_s1 graph=knn miss=[0.1] mode=base

## Dataset: bci_iv2a_real_s1 | rows=42
  Graph: knn__k3 built OK
    mean | MR=0.1 | seed=0 | MAE=3.5667e-02 | t=0.0022s
    nearest | MR=0.1 | seed=0 | MAE=3.1361e-02 | t=0.0037s
    tikhonov | MR=0.1 | seed=0 | MAE=1.3106e-01 | t=0.0080s
    tv | MR=0.1 | seed=0 | MAE=3.5664e-02 | t=0.2045s
    trss | MR=0.1 | seed=0 | MAE=2.5778e-02 | t=0.0197s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=2.6389e-01 | t=0.0116s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=4.4274e-01 | t=2.1834s
    mean | MR=0.1 | seed=1 | MAE=3.3709e-02 | t=0.0027s
    nearest | MR=0.1 | seed=1 | MAE=3.1289e-02 | t=0.0034s
    tikhonov | MR=0.1 | seed=1 | MAE=1.2965e-01 | t=0.0075s
    tv | MR=0.1 | seed=1 | MAE=3.3707e-02 | t=0.2027s
    trss | MR=0.1 | seed=1 | MAE=2.3537e-02 | t=0.0192s

Completed: 2026-04-15T00:22:06.294542+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.