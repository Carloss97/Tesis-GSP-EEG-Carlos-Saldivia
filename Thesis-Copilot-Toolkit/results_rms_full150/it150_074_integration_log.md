# Integration Log: it150_074
Started: 2026-04-15T00:35:18.407335+00:00
Description: Bulk normalized run it150_074 dataset=physionet_real graph=vknng miss=[0.1] mode=base

## Dataset: physionet_eegmmidb_real | rows=42
  Graph: vknng built OK
    mean | MR=0.1 | seed=0 | MAE=3.9669e-02 | t=0.0023s
    nearest | MR=0.1 | seed=0 | MAE=4.4949e-02 | t=0.0029s
    tikhonov | MR=0.1 | seed=0 | MAE=1.0606e-01 | t=0.0075s
    tv | MR=0.1 | seed=0 | MAE=3.9228e-02 | t=0.1906s
    trss | MR=0.1 | seed=0 | MAE=1.9941e-02 | t=0.0194s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=2.2628e-01 | t=0.0087s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=5.7147e-01 | t=1.7421s
    mean | MR=0.1 | seed=1 | MAE=3.8639e-02 | t=0.0029s
    nearest | MR=0.1 | seed=1 | MAE=4.3518e-02 | t=0.0032s
    tikhonov | MR=0.1 | seed=1 | MAE=1.0528e-01 | t=0.0110s
    tv | MR=0.1 | seed=1 | MAE=3.8208e-02 | t=0.2082s
    trss | MR=0.1 | seed=1 | MAE=1.9228e-02 | t=0.0192s

Completed: 2026-04-15T00:35:18.408082+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.