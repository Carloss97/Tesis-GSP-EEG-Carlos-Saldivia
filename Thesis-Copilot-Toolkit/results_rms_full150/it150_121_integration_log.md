# Integration Log: it150_121
Started: 2026-04-15T00:55:24.760082+00:00
Description: Bulk normalized run it150_121 dataset=mne_sample graph=gaussian miss=[0.2] mode=base

## Dataset: mne_sample | rows=14
  Graph: gaussian__sigma1.0 built OK
    mean | MR=0.2 | seed=0 | MAE=1.5569e-01 | t=0.0026s
    nearest | MR=0.2 | seed=0 | MAE=2.0800e-01 | t=0.0052s
    tikhonov | MR=0.2 | seed=0 | MAE=6.7867e-01 | t=0.0073s
    tv | MR=0.2 | seed=0 | MAE=1.5569e-01 | t=0.2387s
    trss | MR=0.2 | seed=0 | MAE=1.0632e-01 | t=0.0199s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=8.4000e-01 | t=0.0111s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=8.4537e-01 | t=1.7186s
    mean | MR=0.2 | seed=1 | MAE=1.5761e-01 | t=0.0029s
    nearest | MR=0.2 | seed=1 | MAE=2.1365e-01 | t=0.0054s
    tikhonov | MR=0.2 | seed=1 | MAE=6.7893e-01 | t=0.0078s
    tv | MR=0.2 | seed=1 | MAE=1.5761e-01 | t=0.2391s
    trss | MR=0.2 | seed=1 | MAE=1.0851e-01 | t=0.0195s

Completed: 2026-04-15T00:55:24.760838+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.