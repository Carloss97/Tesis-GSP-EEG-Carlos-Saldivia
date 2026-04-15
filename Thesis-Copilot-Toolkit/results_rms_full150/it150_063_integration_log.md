# Integration Log: it150_063
Started: 2026-04-15T00:33:20.886226+00:00
Description: Bulk normalized run it150_063 dataset=bci_iv2a_real_s1 graph=knng miss=[0.1] mode=base

## Dataset: bci_iv2a_real_s1 | rows=42
  Graph: knng built OK
    mean | MR=0.1 | seed=0 | MAE=3.5667e-02 | t=0.0028s
    nearest | MR=0.1 | seed=0 | MAE=3.1361e-02 | t=0.0050s
    tikhonov | MR=0.1 | seed=0 | MAE=1.5596e-01 | t=0.0087s
    tv | MR=0.1 | seed=0 | MAE=3.5667e-02 | t=0.2348s
    trss | MR=0.1 | seed=0 | MAE=2.7735e-02 | t=0.0207s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=2.8832e-01 | t=0.0130s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=4.8208e-01 | t=2.4126s
    mean | MR=0.1 | seed=1 | MAE=3.3709e-02 | t=0.0031s
    nearest | MR=0.1 | seed=1 | MAE=3.1289e-02 | t=0.0039s
    tikhonov | MR=0.1 | seed=1 | MAE=1.5428e-01 | t=0.0080s
    tv | MR=0.1 | seed=1 | MAE=3.3709e-02 | t=0.2128s
    trss | MR=0.1 | seed=1 | MAE=2.5426e-02 | t=0.0196s

Completed: 2026-04-15T00:33:20.887648+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.