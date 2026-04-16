# Integration Log: it150_097
Started: 2026-04-15T00:54:01.383369+00:00
Description: Bulk normalized run it150_097 dataset=mne_sample graph=knn miss=[0.2] mode=base

## Dataset: mne_sample | rows=14
  Graph: knn__k3 built OK
    mean | MR=0.2 | seed=0 | MAE=1.5569e-01 | t=0.0027s
    nearest | MR=0.2 | seed=0 | MAE=2.0800e-01 | t=0.0090s
    tikhonov | MR=0.2 | seed=0 | MAE=3.6924e-01 | t=0.0312s
    tv | MR=0.2 | seed=0 | MAE=1.5566e-01 | t=0.2830s
    trss | MR=0.2 | seed=0 | MAE=1.2340e-01 | t=0.0202s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=6.0178e-01 | t=0.0116s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=6.8029e-01 | t=5.6959s
    mean | MR=0.2 | seed=1 | MAE=1.5761e-01 | t=0.0078s
    nearest | MR=0.2 | seed=1 | MAE=2.1365e-01 | t=0.0218s
    tikhonov | MR=0.2 | seed=1 | MAE=3.7220e-01 | t=0.0135s
    tv | MR=0.2 | seed=1 | MAE=1.5774e-01 | t=0.2218s
    trss | MR=0.2 | seed=1 | MAE=1.2913e-01 | t=0.0200s

Completed: 2026-04-15T00:54:01.384779+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.