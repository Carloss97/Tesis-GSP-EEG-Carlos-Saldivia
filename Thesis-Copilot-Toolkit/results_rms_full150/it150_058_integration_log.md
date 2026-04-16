# Integration Log: it150_058
Started: 2026-04-15T00:50:06.139749+00:00
Description: Bulk normalized run it150_058 dataset=synthetic_beta graph=kalofolias miss=[0.1] mode=base

## Dataset: synthetic_beta | rows=14
  Graph: kalofolias built OK
    mean | MR=0.1 | seed=0 | MAE=4.3607e-02 | t=0.0037s
    nearest | MR=0.1 | seed=0 | MAE=5.6541e-02 | t=0.0033s
    tikhonov | MR=0.1 | seed=0 | MAE=6.3170e-01 | t=0.0133s
    tv | MR=0.1 | seed=0 | MAE=4.3608e-02 | t=0.4617s
    trss | MR=0.1 | seed=0 | MAE=4.2793e-02 | t=0.0168s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=6.3419e-01 | t=0.0080s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=8.8943e-01 | t=1.2038s
    mean | MR=0.1 | seed=1 | MAE=4.3636e-02 | t=0.0038s
    nearest | MR=0.1 | seed=1 | MAE=5.7009e-02 | t=0.0034s
    tikhonov | MR=0.1 | seed=1 | MAE=6.3089e-01 | t=0.0088s
    tv | MR=0.1 | seed=1 | MAE=4.3637e-02 | t=0.1757s
    trss | MR=0.1 | seed=1 | MAE=4.1501e-02 | t=0.0189s

Completed: 2026-04-15T00:50:06.140957+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.