# Integration Log: it150_014
Started: 2026-04-15T00:24:01.797615+00:00
Description: Bulk normalized run it150_014 dataset=physionet_real graph=knn miss=[0.1] mode=base

## Dataset: physionet_eegmmidb_real | rows=42
  Graph: knn__k5 built OK
    mean | MR=0.1 | seed=0 | MAE=3.9669e-02 | t=0.0030s
    nearest | MR=0.1 | seed=0 | MAE=4.4949e-02 | t=0.0037s
    tikhonov | MR=0.1 | seed=0 | MAE=1.1840e-01 | t=0.0076s
    tv | MR=0.1 | seed=0 | MAE=3.9418e-02 | t=0.2081s
    trss | MR=0.1 | seed=0 | MAE=1.9266e-02 | t=0.0186s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=2.4921e-01 | t=0.0112s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=6.0714e-01 | t=2.3468s
    mean | MR=0.1 | seed=1 | MAE=3.8639e-02 | t=0.0025s
    nearest | MR=0.1 | seed=1 | MAE=4.3518e-02 | t=0.0031s
    tikhonov | MR=0.1 | seed=1 | MAE=1.1790e-01 | t=0.0088s
    tv | MR=0.1 | seed=1 | MAE=3.8402e-02 | t=0.2023s
    trss | MR=0.1 | seed=1 | MAE=1.8433e-02 | t=0.0185s

Completed: 2026-04-15T00:24:01.798616+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.