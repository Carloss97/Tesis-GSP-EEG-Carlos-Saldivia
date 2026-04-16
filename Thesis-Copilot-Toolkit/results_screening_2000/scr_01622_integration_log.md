# Integration Log: scr_01622
Started: 2026-04-16T09:13:25.160926+00:00
Description: Screening scr_01622 ds=physionet_real graph=knn miss=2ch mode=noise

## Dataset: physionet_eegmmidb_real | rows=42
  Graph: knn__k3 built OK
    mean | MR=0.2 | seed=0 | MAE=7.8230e-02 | t=0.0020s
    nearest | MR=0.2 | seed=0 | MAE=9.0465e-02 | t=0.0041s
    tikhonov | MR=0.2 | seed=0 | MAE=1.0823e-01 | t=0.0058s
    tv | MR=0.2 | seed=0 | MAE=7.6434e-02 | t=0.1544s
    trss | MR=0.2 | seed=0 | MAE=3.9504e-02 | t=0.0213s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.0720e-01 | t=0.0150s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=5.5461e-01 | t=2.8090s
    mean | MR=0.2 | seed=1 | MAE=7.8011e-02 | t=0.0021s
    nearest | MR=0.2 | seed=1 | MAE=8.9030e-02 | t=0.0044s
    tikhonov | MR=0.2 | seed=1 | MAE=1.0819e-01 | t=0.0058s
    tv | MR=0.2 | seed=1 | MAE=7.6172e-02 | t=0.1511s
    trss | MR=0.2 | seed=1 | MAE=3.9500e-02 | t=0.0200s

Completed: 2026-04-16T09:13:25.161810+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.