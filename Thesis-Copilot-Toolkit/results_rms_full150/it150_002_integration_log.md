# Integration Log: it150_002
Started: 2026-04-15T00:21:44.878700+00:00
Description: Bulk normalized run it150_002 dataset=physionet_real graph=knn miss=[0.1] mode=base

## Dataset: physionet_eegmmidb_real | rows=42
  Graph: knn__k3 built OK
    mean | MR=0.1 | seed=0 | MAE=3.9669e-02 | t=0.0025s
    nearest | MR=0.1 | seed=0 | MAE=4.4949e-02 | t=0.0032s
    tikhonov | MR=0.1 | seed=0 | MAE=8.7521e-02 | t=0.0088s
    tv | MR=0.1 | seed=0 | MAE=3.8597e-02 | t=0.2064s
    trss | MR=0.1 | seed=0 | MAE=1.9006e-02 | t=0.0192s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=1.9233e-01 | t=0.0110s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=5.3374e-01 | t=2.6901s
    mean | MR=0.1 | seed=1 | MAE=3.8639e-02 | t=0.0027s
    nearest | MR=0.1 | seed=1 | MAE=4.3518e-02 | t=0.0032s
    tikhonov | MR=0.1 | seed=1 | MAE=8.6735e-02 | t=0.0075s
    tv | MR=0.1 | seed=1 | MAE=3.7556e-02 | t=0.2009s
    trss | MR=0.1 | seed=1 | MAE=1.8084e-02 | t=0.0192s

Completed: 2026-04-15T00:21:44.879881+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.