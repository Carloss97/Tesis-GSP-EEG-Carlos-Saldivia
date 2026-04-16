# Integration Log: it150_101
Started: 2026-04-15T00:40:19.771262+00:00
Description: Bulk normalized run it150_101 dataset=bci_iv2a_real_s3 graph=knn miss=[0.2] mode=base

## Dataset: bci_iv2a_real_s3 | rows=42
  Graph: knn__k3 built OK
    mean | MR=0.2 | seed=0 | MAE=6.5815e-02 | t=0.0022s
    nearest | MR=0.2 | seed=0 | MAE=6.1045e-02 | t=0.0049s
    tikhonov | MR=0.2 | seed=0 | MAE=1.6477e-01 | t=0.0088s
    tv | MR=0.2 | seed=0 | MAE=6.5819e-02 | t=0.1862s
    trss | MR=0.2 | seed=0 | MAE=6.0806e-02 | t=0.0201s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.9111e-01 | t=0.0105s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=5.6222e-01 | t=1.9929s
    mean | MR=0.2 | seed=1 | MAE=6.8917e-02 | t=0.0026s
    nearest | MR=0.2 | seed=1 | MAE=5.9347e-02 | t=0.0054s
    tikhonov | MR=0.2 | seed=1 | MAE=1.6649e-01 | t=0.0077s
    tv | MR=0.2 | seed=1 | MAE=6.8921e-02 | t=0.1855s
    trss | MR=0.2 | seed=1 | MAE=6.2594e-02 | t=0.0199s

Completed: 2026-04-15T00:40:19.772021+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.