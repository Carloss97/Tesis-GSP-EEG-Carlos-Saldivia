# Integration Log: it150_095
Started: 2026-04-15T00:53:32.662043+00:00
Description: Bulk normalized run it150_095 dataset=synthetic_broad graph=aew miss=[0.1] mode=base

## Dataset: synthetic_broad | rows=14
  Graph: aew built OK
    mean | MR=0.1 | seed=0 | MAE=5.4881e-02 | t=0.0174s
    nearest | MR=0.1 | seed=0 | MAE=7.5105e-02 | t=0.0152s
    tikhonov | MR=0.1 | seed=0 | MAE=1.0636e-01 | t=0.0097s
    tv | MR=0.1 | seed=0 | MAE=5.2368e-02 | t=0.2198s
    trss | MR=0.1 | seed=0 | MAE=3.5335e-02 | t=0.0206s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=2.4302e-01 | t=0.0112s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=4.7330e-01 | t=2.1948s
    mean | MR=0.1 | seed=1 | MAE=5.4906e-02 | t=0.0028s
    nearest | MR=0.1 | seed=1 | MAE=7.4297e-02 | t=0.0050s
    tikhonov | MR=0.1 | seed=1 | MAE=1.0590e-01 | t=0.0072s
    tv | MR=0.1 | seed=1 | MAE=5.2283e-02 | t=0.2176s
    trss | MR=0.1 | seed=1 | MAE=3.4586e-02 | t=0.0204s

Completed: 2026-04-15T00:53:32.667533+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.