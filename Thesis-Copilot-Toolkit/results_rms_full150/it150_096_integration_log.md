# Integration Log: it150_096
Started: 2026-04-15T00:53:44.108746+00:00
Description: Bulk normalized run it150_096 dataset=synthetic_16ch graph=aew miss=[0.1] mode=base

## Dataset: synthetic_16ch | rows=14
  Graph: aew built OK
    mean | MR=0.1 | seed=0 | MAE=4.3607e-02 | t=0.0061s
    nearest | MR=0.1 | seed=0 | MAE=5.6541e-02 | t=0.0037s
    tikhonov | MR=0.1 | seed=0 | MAE=9.2359e-02 | t=0.0145s
    tv | MR=0.1 | seed=0 | MAE=4.1017e-02 | t=0.4190s
    trss | MR=0.1 | seed=0 | MAE=2.6438e-02 | t=0.0178s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=2.3313e-01 | t=0.0091s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=5.0661e-01 | t=1.0937s
    mean | MR=0.1 | seed=1 | MAE=4.3636e-02 | t=0.0029s
    nearest | MR=0.1 | seed=1 | MAE=5.7009e-02 | t=0.0027s
    tikhonov | MR=0.1 | seed=1 | MAE=9.3350e-02 | t=0.0088s
    tv | MR=0.1 | seed=1 | MAE=4.1426e-02 | t=0.1908s
    trss | MR=0.1 | seed=1 | MAE=2.7094e-02 | t=0.0197s

Completed: 2026-04-15T00:53:44.109698+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.