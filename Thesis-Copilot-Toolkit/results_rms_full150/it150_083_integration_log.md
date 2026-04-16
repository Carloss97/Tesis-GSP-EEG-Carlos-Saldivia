# Integration Log: it150_083
Started: 2026-04-15T00:52:28.889977+00:00
Description: Bulk normalized run it150_083 dataset=synthetic_broad graph=vknng miss=[0.1] mode=base

## Dataset: synthetic_broad | rows=14
  Graph: vknng built OK
    mean | MR=0.1 | seed=0 | MAE=5.4881e-02 | t=0.0028s
    nearest | MR=0.1 | seed=0 | MAE=7.5105e-02 | t=0.0035s
    tikhonov | MR=0.1 | seed=0 | MAE=2.3317e-01 | t=0.0090s
    tv | MR=0.1 | seed=0 | MAE=5.6504e-02 | t=0.2040s
    trss | MR=0.1 | seed=0 | MAE=4.2167e-02 | t=0.0287s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=4.3747e-01 | t=0.0148s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=6.3170e-01 | t=4.9513s
    mean | MR=0.1 | seed=1 | MAE=5.4906e-02 | t=0.0025s
    nearest | MR=0.1 | seed=1 | MAE=7.4297e-02 | t=0.0041s
    tikhonov | MR=0.1 | seed=1 | MAE=2.3317e-01 | t=0.0077s
    tv | MR=0.1 | seed=1 | MAE=5.6504e-02 | t=0.2330s
    trss | MR=0.1 | seed=1 | MAE=4.0961e-02 | t=0.0200s

Completed: 2026-04-15T00:52:28.891106+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.