# Integration Log: it150_100
Started: 2026-04-15T00:40:00.089160+00:00
Description: Bulk normalized run it150_100 dataset=bci_iv2a_real_s2 graph=knn miss=[0.2] mode=base

## Dataset: bci_iv2a_real_s2 | rows=42
  Graph: knn__k3 built OK
    mean | MR=0.2 | seed=0 | MAE=2.9528e-02 | t=0.0023s
    nearest | MR=0.2 | seed=0 | MAE=2.7159e-02 | t=0.0049s
    tikhonov | MR=0.2 | seed=0 | MAE=6.9107e-02 | t=0.0071s
    tv | MR=0.2 | seed=0 | MAE=2.9529e-02 | t=0.1823s
    trss | MR=0.2 | seed=0 | MAE=2.5467e-02 | t=0.0197s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.9410e-01 | t=0.0113s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=5.4660e-01 | t=1.8002s
    mean | MR=0.2 | seed=1 | MAE=2.8797e-02 | t=0.0033s
    nearest | MR=0.2 | seed=1 | MAE=2.8346e-02 | t=0.0046s
    tikhonov | MR=0.2 | seed=1 | MAE=6.8441e-02 | t=0.0078s
    tv | MR=0.2 | seed=1 | MAE=2.8797e-02 | t=0.2324s
    trss | MR=0.2 | seed=1 | MAE=2.4699e-02 | t=0.0203s

Completed: 2026-04-15T00:40:00.089950+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.