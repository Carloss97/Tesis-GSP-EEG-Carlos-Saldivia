# Integration Log: it150_113
Started: 2026-04-15T00:42:52.975065+00:00
Description: Bulk normalized run it150_113 dataset=bci_iv2a_real_s3 graph=knn miss=[0.2] mode=base

## Dataset: bci_iv2a_real_s3 | rows=42
  Graph: knn__k5 built OK
    mean | MR=0.2 | seed=0 | MAE=6.5815e-02 | t=0.0030s
    nearest | MR=0.2 | seed=0 | MAE=6.1045e-02 | t=0.0072s
    tikhonov | MR=0.2 | seed=0 | MAE=2.0588e-01 | t=0.0088s
    tv | MR=0.2 | seed=0 | MAE=6.5819e-02 | t=0.2250s
    trss | MR=0.2 | seed=0 | MAE=5.6722e-02 | t=0.0205s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=3.2886e-01 | t=0.0125s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=6.3747e-01 | t=2.5523s
    mean | MR=0.2 | seed=1 | MAE=6.8917e-02 | t=0.0026s
    nearest | MR=0.2 | seed=1 | MAE=5.9347e-02 | t=0.0058s
    tikhonov | MR=0.2 | seed=1 | MAE=2.0697e-01 | t=0.0072s
    tv | MR=0.2 | seed=1 | MAE=6.8921e-02 | t=0.2253s
    trss | MR=0.2 | seed=1 | MAE=5.9458e-02 | t=0.0202s

Completed: 2026-04-15T00:42:52.976050+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.