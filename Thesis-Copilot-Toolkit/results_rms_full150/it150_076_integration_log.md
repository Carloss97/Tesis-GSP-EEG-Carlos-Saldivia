# Integration Log: it150_076
Started: 2026-04-15T00:35:57.475185+00:00
Description: Bulk normalized run it150_076 dataset=bci_iv2a_real_s2 graph=vknng miss=[0.1] mode=base

## Dataset: bci_iv2a_real_s2 | rows=42
  Graph: vknng built OK
    mean | MR=0.1 | seed=0 | MAE=1.3831e-02 | t=0.0027s
    nearest | MR=0.1 | seed=0 | MAE=1.3215e-02 | t=0.0033s
    tikhonov | MR=0.1 | seed=0 | MAE=4.6306e-02 | t=0.0084s
    tv | MR=0.1 | seed=0 | MAE=1.3832e-02 | t=0.1830s
    trss | MR=0.1 | seed=0 | MAE=1.2170e-02 | t=0.0191s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=1.8177e-01 | t=0.0142s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=4.4643e-01 | t=1.7630s
    mean | MR=0.1 | seed=1 | MAE=1.4351e-02 | t=0.0028s
    nearest | MR=0.1 | seed=1 | MAE=1.2774e-02 | t=0.0032s
    tikhonov | MR=0.1 | seed=1 | MAE=4.6510e-02 | t=0.0072s
    tv | MR=0.1 | seed=1 | MAE=1.4351e-02 | t=0.1947s
    trss | MR=0.1 | seed=1 | MAE=1.2516e-02 | t=0.0193s

Completed: 2026-04-15T00:35:57.475941+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.