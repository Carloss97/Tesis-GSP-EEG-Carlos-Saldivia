# Integration Log: it150_109
Started: 2026-04-15T00:54:52.859802+00:00
Description: Bulk normalized run it150_109 dataset=mne_sample graph=knn miss=[0.2] mode=base

## Dataset: mne_sample | rows=14
  Graph: knn__k5 built OK
    mean | MR=0.2 | seed=0 | MAE=1.5569e-01 | t=0.0026s
    nearest | MR=0.2 | seed=0 | MAE=2.0800e-01 | t=0.0076s
    tikhonov | MR=0.2 | seed=0 | MAE=4.1540e-01 | t=0.0081s
    tv | MR=0.2 | seed=0 | MAE=1.5570e-01 | t=0.1810s
    trss | MR=0.2 | seed=0 | MAE=1.0733e-01 | t=0.0200s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=6.7226e-01 | t=0.0095s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=7.4328e-01 | t=1.7148s
    mean | MR=0.2 | seed=1 | MAE=1.5761e-01 | t=0.0021s
    nearest | MR=0.2 | seed=1 | MAE=2.1365e-01 | t=0.0054s
    tikhonov | MR=0.2 | seed=1 | MAE=4.1752e-01 | t=0.0070s
    tv | MR=0.2 | seed=1 | MAE=1.5768e-01 | t=0.1801s
    trss | MR=0.2 | seed=1 | MAE=1.1128e-01 | t=0.0197s

Completed: 2026-04-15T00:54:52.860814+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.