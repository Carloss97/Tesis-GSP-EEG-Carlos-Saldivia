# Integration Log: it150_098
Started: 2026-04-15T00:39:20.920103+00:00
Description: Bulk normalized run it150_098 dataset=physionet_real graph=knn miss=[0.2] mode=base

## Dataset: physionet_eegmmidb_real | rows=42
  Graph: knn__k3 built OK
    mean | MR=0.2 | seed=0 | MAE=7.8019e-02 | t=0.0023s
    nearest | MR=0.2 | seed=0 | MAE=8.9975e-02 | t=0.0049s
    tikhonov | MR=0.2 | seed=0 | MAE=1.0630e-01 | t=0.0075s
    tv | MR=0.2 | seed=0 | MAE=7.6202e-02 | t=0.1903s
    trss | MR=0.2 | seed=0 | MAE=3.8252e-02 | t=0.0196s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.0466e-01 | t=0.0094s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=5.5443e-01 | t=2.0652s
    mean | MR=0.2 | seed=1 | MAE=7.7313e-02 | t=0.0020s
    nearest | MR=0.2 | seed=1 | MAE=8.7931e-02 | t=0.0051s
    tikhonov | MR=0.2 | seed=1 | MAE=1.0612e-01 | t=0.0118s
    tv | MR=0.2 | seed=1 | MAE=7.5449e-02 | t=0.1792s
    trss | MR=0.2 | seed=1 | MAE=3.8157e-02 | t=0.0205s

Completed: 2026-04-15T00:39:20.921068+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.