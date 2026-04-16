# Integration Log: it150_017
Started: 2026-04-15T00:25:02.369909+00:00
Description: Bulk normalized run it150_017 dataset=bci_iv2a_real_s3 graph=knn miss=[0.1] mode=base

## Dataset: bci_iv2a_real_s3 | rows=42
  Graph: knn__k5 built OK
    mean | MR=0.1 | seed=0 | MAE=3.5550e-02 | t=0.0027s
    nearest | MR=0.1 | seed=0 | MAE=2.9251e-02 | t=0.0036s
    tikhonov | MR=0.1 | seed=0 | MAE=1.8687e-01 | t=0.0066s
    tv | MR=0.1 | seed=0 | MAE=3.5554e-02 | t=0.1940s
    trss | MR=0.1 | seed=0 | MAE=3.0725e-02 | t=0.0190s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=3.2102e-01 | t=0.0106s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=6.2253e-01 | t=1.7867s
    mean | MR=0.1 | seed=1 | MAE=3.3104e-02 | t=0.0023s
    nearest | MR=0.1 | seed=1 | MAE=2.9433e-02 | t=0.0031s
    tikhonov | MR=0.1 | seed=1 | MAE=1.8495e-01 | t=0.0071s
    tv | MR=0.1 | seed=1 | MAE=3.3106e-02 | t=0.1859s
    trss | MR=0.1 | seed=1 | MAE=2.9154e-02 | t=0.0183s

Completed: 2026-04-15T00:25:02.371388+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.