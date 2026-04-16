# Integration Log: it150_013
Started: 2026-04-15T00:46:27.107902+00:00
Description: Bulk normalized run it150_013 dataset=mne_sample graph=knn miss=[0.1] mode=base

## Dataset: mne_sample | rows=14
  Graph: knn__k5 built OK
    mean | MR=0.1 | seed=0 | MAE=7.9366e-02 | t=0.0050s
    nearest | MR=0.1 | seed=0 | MAE=1.0002e-01 | t=0.0076s
    tikhonov | MR=0.1 | seed=0 | MAE=3.6625e-01 | t=0.0206s
    tv | MR=0.1 | seed=0 | MAE=7.9383e-02 | t=0.2172s
    trss | MR=0.1 | seed=0 | MAE=5.1952e-02 | t=0.0190s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=6.5183e-01 | t=0.0111s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=7.2750e-01 | t=4.4291s
    mean | MR=0.1 | seed=1 | MAE=7.8687e-02 | t=0.0053s
    nearest | MR=0.1 | seed=1 | MAE=1.0381e-01 | t=0.0065s
    tikhonov | MR=0.1 | seed=1 | MAE=3.6646e-01 | t=0.0360s
    tv | MR=0.1 | seed=1 | MAE=7.8736e-02 | t=0.3652s
    trss | MR=0.1 | seed=1 | MAE=5.0945e-02 | t=0.0199s

Completed: 2026-04-15T00:46:27.110413+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.