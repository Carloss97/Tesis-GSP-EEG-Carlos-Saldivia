# Integration Log: it150_126
Started: 2026-04-15T00:55:49.385971+00:00
Description: Bulk normalized run it150_126 dataset=iv100hz_mat graph=gaussian miss=[0.2] mode=base

## Dataset: iv100hz_mat | rows=14
  Graph: gaussian__sigma1.0 built OK
    mean | MR=0.2 | seed=0 | MAE=1.6829e-02 | t=0.0025s
    nearest | MR=0.2 | seed=0 | MAE=2.5741e-02 | t=0.0049s
    tikhonov | MR=0.2 | seed=0 | MAE=5.8990e-02 | t=0.0085s
    tv | MR=0.2 | seed=0 | MAE=1.0751e-02 | t=0.2353s
    trss | MR=0.2 | seed=0 | MAE=1.1964e-02 | t=0.0206s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=8.4887e-02 | t=0.0108s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.0822e-01 | t=1.8818s
    mean | MR=0.2 | seed=1 | MAE=1.6767e-02 | t=0.0020s
    nearest | MR=0.2 | seed=1 | MAE=2.5796e-02 | t=0.0049s
    tikhonov | MR=0.2 | seed=1 | MAE=5.8994e-02 | t=0.0087s
    tv | MR=0.2 | seed=1 | MAE=1.0718e-02 | t=0.2339s
    trss | MR=0.2 | seed=1 | MAE=1.2038e-02 | t=0.0205s

Completed: 2026-04-15T00:55:49.387202+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.