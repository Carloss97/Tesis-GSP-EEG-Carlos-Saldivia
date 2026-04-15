# Integration Log: it150_064
Started: 2026-04-15T00:33:44.057652+00:00
Description: Bulk normalized run it150_064 dataset=bci_iv2a_real_s2 graph=knng miss=[0.1] mode=base

## Dataset: bci_iv2a_real_s2 | rows=42
  Graph: knng built OK
    mean | MR=0.1 | seed=0 | MAE=1.3831e-02 | t=0.0026s
    nearest | MR=0.1 | seed=0 | MAE=1.3215e-02 | t=0.0029s
    tikhonov | MR=0.1 | seed=0 | MAE=6.6714e-02 | t=0.0080s
    tv | MR=0.1 | seed=0 | MAE=1.3832e-02 | t=0.2119s
    trss | MR=0.1 | seed=0 | MAE=1.1552e-02 | t=0.0198s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=1.9715e-01 | t=0.0100s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=5.7395e-01 | t=2.2866s
    mean | MR=0.1 | seed=1 | MAE=1.4351e-02 | t=0.0028s
    nearest | MR=0.1 | seed=1 | MAE=1.2774e-02 | t=0.0036s
    tikhonov | MR=0.1 | seed=1 | MAE=6.6930e-02 | t=0.0091s
    tv | MR=0.1 | seed=1 | MAE=1.4351e-02 | t=0.2108s
    trss | MR=0.1 | seed=1 | MAE=1.1750e-02 | t=0.0191s

Completed: 2026-04-15T00:33:44.058679+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.