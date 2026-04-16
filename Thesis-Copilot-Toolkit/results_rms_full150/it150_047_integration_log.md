# Integration Log: it150_047
Started: 2026-04-15T00:49:12.850613+00:00
Description: Bulk normalized run it150_047 dataset=synthetic_broad graph=gaussian miss=[0.1] mode=base

## Dataset: synthetic_broad | rows=14
  Graph: gaussian__sigma0.6 built OK
    mean | MR=0.1 | seed=0 | MAE=5.4881e-02 | t=0.0031s
    nearest | MR=0.1 | seed=0 | MAE=7.5105e-02 | t=0.0053s
    tikhonov | MR=0.1 | seed=0 | MAE=2.5984e-01 | t=0.0103s
    tv | MR=0.1 | seed=0 | MAE=5.4519e-02 | t=0.3107s
    trss | MR=0.1 | seed=0 | MAE=3.9763e-02 | t=0.0195s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=4.6972e-01 | t=0.0124s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=6.9395e-01 | t=7.6226s
    mean | MR=0.1 | seed=1 | MAE=5.4906e-02 | t=0.0039s
    nearest | MR=0.1 | seed=1 | MAE=7.4297e-02 | t=0.0050s
    tikhonov | MR=0.1 | seed=1 | MAE=2.6028e-01 | t=0.0112s
    tv | MR=0.1 | seed=1 | MAE=5.4641e-02 | t=0.2936s
    trss | MR=0.1 | seed=1 | MAE=3.9652e-02 | t=0.0195s

Completed: 2026-04-15T00:49:12.851920+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.