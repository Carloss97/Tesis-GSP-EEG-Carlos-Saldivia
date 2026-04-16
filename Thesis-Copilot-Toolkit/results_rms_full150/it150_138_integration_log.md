# Integration Log: it150_138
Started: 2026-04-15T00:57:12.480918+00:00
Description: Bulk normalized run it150_138 dataset=iv100hz_mat graph=gaussian miss=[0.2] mode=base

## Dataset: iv100hz_mat | rows=14
  Graph: gaussian__sigma0.6 built OK
    mean | MR=0.2 | seed=0 | MAE=1.6829e-02 | t=0.0023s
    nearest | MR=0.2 | seed=0 | MAE=2.5741e-02 | t=0.0054s
    tikhonov | MR=0.2 | seed=0 | MAE=4.7156e-02 | t=0.0078s
    tv | MR=0.2 | seed=0 | MAE=1.0980e-02 | t=0.2331s
    trss | MR=0.2 | seed=0 | MAE=1.2634e-02 | t=0.0214s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=7.6422e-02 | t=0.0100s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=9.3154e-02 | t=1.8087s
    mean | MR=0.2 | seed=1 | MAE=1.6767e-02 | t=0.0020s
    nearest | MR=0.2 | seed=1 | MAE=2.5796e-02 | t=0.0050s
    tikhonov | MR=0.2 | seed=1 | MAE=4.7225e-02 | t=0.0076s
    tv | MR=0.2 | seed=1 | MAE=1.1340e-02 | t=0.2390s
    trss | MR=0.2 | seed=1 | MAE=1.2776e-02 | t=0.0204s

Completed: 2026-04-15T00:57:12.481994+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.