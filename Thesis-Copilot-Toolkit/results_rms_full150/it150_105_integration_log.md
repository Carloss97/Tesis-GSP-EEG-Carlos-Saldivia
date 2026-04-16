# Integration Log: it150_105
Started: 2026-04-15T00:54:13.032696+00:00
Description: Bulk normalized run it150_105 dataset=synthetic_alpha graph=knn miss=[0.2] mode=base

## Dataset: synthetic_alpha | rows=14
  Graph: knn__k3 built OK
    mean | MR=0.2 | seed=0 | MAE=1.2957e-01 | t=0.0046s
    nearest | MR=0.2 | seed=0 | MAE=1.6337e-01 | t=0.0047s
    tikhonov | MR=0.2 | seed=0 | MAE=2.8022e-01 | t=0.0090s
    tv | MR=0.2 | seed=0 | MAE=1.3599e-01 | t=0.1973s
    trss | MR=0.2 | seed=0 | MAE=1.0839e-01 | t=0.0188s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=4.5345e-01 | t=0.0120s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=6.6816e-01 | t=1.2744s
    mean | MR=0.2 | seed=1 | MAE=1.2838e-01 | t=0.0034s
    nearest | MR=0.2 | seed=1 | MAE=1.7359e-01 | t=0.0051s
    tikhonov | MR=0.2 | seed=1 | MAE=2.8113e-01 | t=0.0072s
    tv | MR=0.2 | seed=1 | MAE=1.3511e-01 | t=0.1920s
    trss | MR=0.2 | seed=1 | MAE=1.1177e-01 | t=0.0184s

Completed: 2026-04-15T00:54:13.034094+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.