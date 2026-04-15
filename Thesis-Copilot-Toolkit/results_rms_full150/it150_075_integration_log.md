# Integration Log: it150_075
Started: 2026-04-15T00:35:38.560579+00:00
Description: Bulk normalized run it150_075 dataset=bci_iv2a_real_s1 graph=vknng miss=[0.1] mode=base

## Dataset: bci_iv2a_real_s1 | rows=42
  Graph: vknng built OK
    mean | MR=0.1 | seed=0 | MAE=3.5667e-02 | t=0.0020s
    nearest | MR=0.1 | seed=0 | MAE=3.1361e-02 | t=0.0038s
    tikhonov | MR=0.1 | seed=0 | MAE=1.0920e-01 | t=0.0078s
    tv | MR=0.1 | seed=0 | MAE=3.5665e-02 | t=0.1888s
    trss | MR=0.1 | seed=0 | MAE=2.8741e-02 | t=0.0188s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=2.3142e-01 | t=0.0123s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=3.9095e-01 | t=1.6909s
    mean | MR=0.1 | seed=1 | MAE=3.3709e-02 | t=0.0021s
    nearest | MR=0.1 | seed=1 | MAE=3.1289e-02 | t=0.0030s
    tikhonov | MR=0.1 | seed=1 | MAE=1.0710e-01 | t=0.0077s
    tv | MR=0.1 | seed=1 | MAE=3.3707e-02 | t=0.1856s
    trss | MR=0.1 | seed=1 | MAE=2.6200e-02 | t=0.0191s

Completed: 2026-04-15T00:35:38.561508+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.