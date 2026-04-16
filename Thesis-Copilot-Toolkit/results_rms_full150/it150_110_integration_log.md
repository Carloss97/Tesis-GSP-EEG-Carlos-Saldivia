# Integration Log: it150_110
Started: 2026-04-15T00:41:22.962033+00:00
Description: Bulk normalized run it150_110 dataset=physionet_real graph=knn miss=[0.2] mode=base

## Dataset: physionet_eegmmidb_real | rows=42
  Graph: knn__k5 built OK
    mean | MR=0.2 | seed=0 | MAE=7.8019e-02 | t=0.0025s
    nearest | MR=0.2 | seed=0 | MAE=8.9975e-02 | t=0.0099s
    tikhonov | MR=0.2 | seed=0 | MAE=1.3636e-01 | t=0.0073s
    tv | MR=0.2 | seed=0 | MAE=7.7598e-02 | t=0.1892s
    trss | MR=0.2 | seed=0 | MAE=3.8537e-02 | t=0.0202s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.6166e-01 | t=0.0105s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=6.2348e-01 | t=1.6632s
    mean | MR=0.2 | seed=1 | MAE=7.7313e-02 | t=0.0027s
    nearest | MR=0.2 | seed=1 | MAE=8.7931e-02 | t=0.0045s
    tikhonov | MR=0.2 | seed=1 | MAE=1.3625e-01 | t=0.0076s
    tv | MR=0.2 | seed=1 | MAE=7.6893e-02 | t=0.1936s
    trss | MR=0.2 | seed=1 | MAE=3.7956e-02 | t=0.0226s

Completed: 2026-04-15T00:41:22.962739+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.