# Integration Log: it150_057
Started: 2026-04-15T00:49:54.881571+00:00
Description: Bulk normalized run it150_057 dataset=synthetic_alpha graph=kalofolias miss=[0.1] mode=base

## Dataset: synthetic_alpha | rows=14
  Graph: kalofolias built OK
    mean | MR=0.1 | seed=0 | MAE=4.3607e-02 | t=0.0052s
    nearest | MR=0.1 | seed=0 | MAE=5.6541e-02 | t=0.0056s
    tikhonov | MR=0.1 | seed=0 | MAE=6.3170e-01 | t=0.0176s
    tv | MR=0.1 | seed=0 | MAE=4.3608e-02 | t=0.1861s
    trss | MR=0.1 | seed=0 | MAE=4.2793e-02 | t=0.0164s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=6.3419e-01 | t=0.0101s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=8.8943e-01 | t=1.0741s
    mean | MR=0.1 | seed=1 | MAE=4.3636e-02 | t=0.0032s
    nearest | MR=0.1 | seed=1 | MAE=5.7009e-02 | t=0.0035s
    tikhonov | MR=0.1 | seed=1 | MAE=6.3089e-01 | t=0.0067s
    tv | MR=0.1 | seed=1 | MAE=4.3637e-02 | t=0.2081s
    trss | MR=0.1 | seed=1 | MAE=4.1501e-02 | t=0.0204s

Completed: 2026-04-15T00:49:54.882740+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.