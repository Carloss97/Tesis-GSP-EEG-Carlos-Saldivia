# Integration Log: it150_009
Started: 2026-04-15T00:45:32.923046+00:00
Description: Bulk normalized run it150_009 dataset=synthetic_alpha graph=knn miss=[0.1] mode=base

## Dataset: synthetic_alpha | rows=14
  Graph: knn__k3 built OK
    mean | MR=0.1 | seed=0 | MAE=4.3607e-02 | t=0.0023s
    nearest | MR=0.1 | seed=0 | MAE=5.6541e-02 | t=0.0045s
    tikhonov | MR=0.1 | seed=0 | MAE=2.1041e-01 | t=0.0105s
    tv | MR=0.1 | seed=0 | MAE=4.6585e-02 | t=0.3613s
    trss | MR=0.1 | seed=0 | MAE=3.5594e-02 | t=0.0751s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=4.1985e-01 | t=0.0220s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=6.3388e-01 | t=5.7558s
    mean | MR=0.1 | seed=1 | MAE=4.3636e-02 | t=0.0027s
    nearest | MR=0.1 | seed=1 | MAE=5.7009e-02 | t=0.0029s
    tikhonov | MR=0.1 | seed=1 | MAE=2.0888e-01 | t=0.0087s
    tv | MR=0.1 | seed=1 | MAE=4.5909e-02 | t=0.2141s
    trss | MR=0.1 | seed=1 | MAE=3.4278e-02 | t=0.0182s

Completed: 2026-04-15T00:45:32.924191+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.