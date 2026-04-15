# Integration Log: it150_005
Started: 2026-04-15T00:22:49.564949+00:00
Description: Bulk normalized run it150_005 dataset=bci_iv2a_real_s3 graph=knn miss=[0.1] mode=base

## Dataset: bci_iv2a_real_s3 | rows=42
  Graph: knn__k3 built OK
    mean | MR=0.1 | seed=0 | MAE=3.5550e-02 | t=0.0035s
    nearest | MR=0.1 | seed=0 | MAE=2.9251e-02 | t=0.0034s
    tikhonov | MR=0.1 | seed=0 | MAE=1.4204e-01 | t=0.0065s
    tv | MR=0.1 | seed=0 | MAE=3.5553e-02 | t=0.1980s
    trss | MR=0.1 | seed=0 | MAE=3.1940e-02 | t=0.0194s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=2.8034e-01 | t=0.0106s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=5.4176e-01 | t=1.9354s
    mean | MR=0.1 | seed=1 | MAE=3.3104e-02 | t=0.0028s
    nearest | MR=0.1 | seed=1 | MAE=2.9433e-02 | t=0.0046s
    tikhonov | MR=0.1 | seed=1 | MAE=1.3981e-01 | t=0.0079s
    tv | MR=0.1 | seed=1 | MAE=3.3106e-02 | t=0.1984s
    trss | MR=0.1 | seed=1 | MAE=3.0925e-02 | t=0.0184s

Completed: 2026-04-15T00:22:49.565946+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.