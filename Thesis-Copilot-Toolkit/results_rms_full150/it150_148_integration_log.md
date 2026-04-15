# Integration Log: it150_148
Started: 2026-04-15T00:58:19.440008+00:00
Description: Bulk normalized run it150_148 dataset=bci_iv2a_real_s2 graph=kalofolias miss=[0.2] mode=base

## Dataset: bci_iv2a_real_s2 | rows=14
  Graph: kalofolias built OK
    mean | MR=0.2 | seed=0 | MAE=2.9528e-02 | t=0.0021s
    nearest | MR=0.2 | seed=0 | MAE=2.7159e-02 | t=0.0048s
    tikhonov | MR=0.2 | seed=0 | MAE=8.5802e-02 | t=0.0080s
    tv | MR=0.2 | seed=0 | MAE=2.9528e-02 | t=0.2610s
    trss | MR=0.2 | seed=0 | MAE=2.1299e-02 | t=0.0196s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.0703e-01 | t=0.0088s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=6.3533e-01 | t=1.8885s
    mean | MR=0.2 | seed=1 | MAE=2.8797e-02 | t=0.0022s
    nearest | MR=0.2 | seed=1 | MAE=2.8346e-02 | t=0.0050s
    tikhonov | MR=0.2 | seed=1 | MAE=8.5439e-02 | t=0.0087s
    tv | MR=0.2 | seed=1 | MAE=2.8797e-02 | t=0.2256s
    trss | MR=0.2 | seed=1 | MAE=2.1400e-02 | t=0.0196s

Completed: 2026-04-15T00:58:19.440749+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.