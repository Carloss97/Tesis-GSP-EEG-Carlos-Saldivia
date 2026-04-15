# Integration Log: it150_001
Started: 2026-04-15T00:45:18.802858+00:00
Description: Bulk normalized run it150_001 dataset=mne_sample graph=knn miss=[0.1] mode=base

## Dataset: mne_sample | rows=14
  Graph: knn__k3 built OK
    mean | MR=0.1 | seed=0 | MAE=7.9366e-02 | t=0.0033s
    nearest | MR=0.1 | seed=0 | MAE=1.0002e-01 | t=0.0046s
    tikhonov | MR=0.1 | seed=0 | MAE=3.0906e-01 | t=0.0115s
    tv | MR=0.1 | seed=0 | MAE=7.9381e-02 | t=0.4913s
    trss | MR=0.1 | seed=0 | MAE=5.8188e-02 | t=0.0709s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=5.7401e-01 | t=0.0182s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=6.5872e-01 | t=4.4459s
    mean | MR=0.1 | seed=1 | MAE=7.8687e-02 | t=0.0032s
    nearest | MR=0.1 | seed=1 | MAE=1.0381e-01 | t=0.0063s
    tikhonov | MR=0.1 | seed=1 | MAE=3.0941e-01 | t=0.0134s
    tv | MR=0.1 | seed=1 | MAE=7.8785e-02 | t=0.4363s
    trss | MR=0.1 | seed=1 | MAE=5.8820e-02 | t=0.0485s

Completed: 2026-04-15T00:45:18.806561+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.