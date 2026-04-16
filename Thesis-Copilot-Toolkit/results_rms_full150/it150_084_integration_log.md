# Integration Log: it150_084
Started: 2026-04-15T00:52:41.359554+00:00
Description: Bulk normalized run it150_084 dataset=synthetic_16ch graph=vknng miss=[0.1] mode=base

## Dataset: synthetic_16ch | rows=14
  Graph: vknng built OK
    mean | MR=0.1 | seed=0 | MAE=4.3607e-02 | t=0.0035s
    nearest | MR=0.1 | seed=0 | MAE=5.6541e-02 | t=0.0032s
    tikhonov | MR=0.1 | seed=0 | MAE=2.3456e-01 | t=0.0087s
    tv | MR=0.1 | seed=0 | MAE=4.5028e-02 | t=0.1789s
    trss | MR=0.1 | seed=0 | MAE=3.3477e-02 | t=0.0164s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=4.5125e-01 | t=0.0093s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=6.7957e-01 | t=1.7452s
    mean | MR=0.1 | seed=1 | MAE=4.3636e-02 | t=0.0053s
    nearest | MR=0.1 | seed=1 | MAE=5.7009e-02 | t=0.0032s
    tikhonov | MR=0.1 | seed=1 | MAE=2.3349e-01 | t=0.0121s
    tv | MR=0.1 | seed=1 | MAE=4.4669e-02 | t=0.3652s
    trss | MR=0.1 | seed=1 | MAE=3.2515e-02 | t=0.0836s

Completed: 2026-04-15T00:52:41.360267+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.