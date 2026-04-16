# Integration Log: it150_093
Started: 2026-04-15T00:53:07.104474+00:00
Description: Bulk normalized run it150_093 dataset=synthetic_alpha graph=aew miss=[0.1] mode=base

## Dataset: synthetic_alpha | rows=14
  Graph: aew built OK
    mean | MR=0.1 | seed=0 | MAE=4.3607e-02 | t=0.0117s
    nearest | MR=0.1 | seed=0 | MAE=5.6541e-02 | t=0.0032s
    tikhonov | MR=0.1 | seed=0 | MAE=9.2359e-02 | t=0.0121s
    tv | MR=0.1 | seed=0 | MAE=4.1017e-02 | t=0.4375s
    trss | MR=0.1 | seed=0 | MAE=2.6438e-02 | t=0.0730s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=2.3313e-01 | t=0.0094s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=5.0661e-01 | t=1.1407s
    mean | MR=0.1 | seed=1 | MAE=4.3636e-02 | t=0.0034s
    nearest | MR=0.1 | seed=1 | MAE=5.7009e-02 | t=0.0027s
    tikhonov | MR=0.1 | seed=1 | MAE=9.3350e-02 | t=0.0090s
    tv | MR=0.1 | seed=1 | MAE=4.1426e-02 | t=0.1863s
    trss | MR=0.1 | seed=1 | MAE=2.7094e-02 | t=0.0182s

Completed: 2026-04-15T00:53:07.105392+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.