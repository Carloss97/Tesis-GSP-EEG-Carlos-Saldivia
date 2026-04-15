# Integration Log: it150_073
Started: 2026-04-15T00:51:52.416730+00:00
Description: Bulk normalized run it150_073 dataset=mne_sample graph=vknng miss=[0.1] mode=base

## Dataset: mne_sample | rows=14
  Graph: vknng built OK
    mean | MR=0.1 | seed=0 | MAE=7.9366e-02 | t=0.0033s
    nearest | MR=0.1 | seed=0 | MAE=1.0002e-01 | t=0.0045s
    tikhonov | MR=0.1 | seed=0 | MAE=3.6272e-01 | t=0.0076s
    tv | MR=0.1 | seed=0 | MAE=7.9386e-02 | t=0.2306s
    trss | MR=0.1 | seed=0 | MAE=6.0004e-02 | t=0.0191s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=6.3977e-01 | t=0.0126s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=6.9248e-01 | t=6.6738s
    mean | MR=0.1 | seed=1 | MAE=7.8687e-02 | t=0.0020s
    nearest | MR=0.1 | seed=1 | MAE=1.0381e-01 | t=0.0042s
    tikhonov | MR=0.1 | seed=1 | MAE=3.6224e-01 | t=0.0087s
    tv | MR=0.1 | seed=1 | MAE=7.8729e-02 | t=0.2403s
    trss | MR=0.1 | seed=1 | MAE=5.8475e-02 | t=0.0187s

Completed: 2026-04-15T00:51:52.417488+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.