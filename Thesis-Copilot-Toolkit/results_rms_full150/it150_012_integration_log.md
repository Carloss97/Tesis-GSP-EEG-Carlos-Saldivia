# Integration Log: it150_012
Started: 2026-04-15T00:46:11.420362+00:00
Description: Bulk normalized run it150_012 dataset=synthetic_16ch graph=knn miss=[0.1] mode=base

## Dataset: synthetic_16ch | rows=14
  Graph: knn__k3 built OK
    mean | MR=0.1 | seed=0 | MAE=4.3607e-02 | t=0.0046s
    nearest | MR=0.1 | seed=0 | MAE=5.6541e-02 | t=0.0189s
    tikhonov | MR=0.1 | seed=0 | MAE=2.1041e-01 | t=0.0133s
    tv | MR=0.1 | seed=0 | MAE=4.6585e-02 | t=0.3724s
    trss | MR=0.1 | seed=0 | MAE=3.5594e-02 | t=0.0174s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=4.1985e-01 | t=0.0103s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=6.3388e-01 | t=1.2990s
    mean | MR=0.1 | seed=1 | MAE=4.3636e-02 | t=0.0032s
    nearest | MR=0.1 | seed=1 | MAE=5.7009e-02 | t=0.0028s
    tikhonov | MR=0.1 | seed=1 | MAE=2.0888e-01 | t=0.0071s
    tv | MR=0.1 | seed=1 | MAE=4.5909e-02 | t=0.1912s
    trss | MR=0.1 | seed=1 | MAE=3.4278e-02 | t=0.0165s

Completed: 2026-04-15T00:46:11.421249+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.