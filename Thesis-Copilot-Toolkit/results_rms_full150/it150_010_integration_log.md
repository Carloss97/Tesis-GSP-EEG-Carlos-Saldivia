# Integration Log: it150_010
Started: 2026-04-15T00:45:45.291845+00:00
Description: Bulk normalized run it150_010 dataset=synthetic_beta graph=knn miss=[0.1] mode=base

## Dataset: synthetic_beta | rows=14
  Graph: knn__k3 built OK
    mean | MR=0.1 | seed=0 | MAE=4.3607e-02 | t=0.0040s
    nearest | MR=0.1 | seed=0 | MAE=5.6541e-02 | t=0.0036s
    tikhonov | MR=0.1 | seed=0 | MAE=2.1041e-01 | t=0.0465s
    tv | MR=0.1 | seed=0 | MAE=4.6585e-02 | t=0.6066s
    trss | MR=0.1 | seed=0 | MAE=3.5594e-02 | t=0.2858s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=4.1985e-01 | t=0.0124s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=6.3388e-01 | t=2.3606s
    mean | MR=0.1 | seed=1 | MAE=4.3636e-02 | t=0.0024s
    nearest | MR=0.1 | seed=1 | MAE=5.7009e-02 | t=0.0036s
    tikhonov | MR=0.1 | seed=1 | MAE=2.0888e-01 | t=0.0083s
    tv | MR=0.1 | seed=1 | MAE=4.5909e-02 | t=0.2104s
    trss | MR=0.1 | seed=1 | MAE=3.4278e-02 | t=0.0190s

Completed: 2026-04-15T00:45:45.292908+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.