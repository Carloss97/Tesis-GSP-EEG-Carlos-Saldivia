# Integration Log: it150_077
Started: 2026-04-15T00:36:18.342843+00:00
Description: Bulk normalized run it150_077 dataset=bci_iv2a_real_s3 graph=vknng miss=[0.1] mode=base

## Dataset: bci_iv2a_real_s3 | rows=42
  Graph: vknng built OK
    mean | MR=0.1 | seed=0 | MAE=3.5550e-02 | t=0.0031s
    nearest | MR=0.1 | seed=0 | MAE=2.9251e-02 | t=0.0030s
    tikhonov | MR=0.1 | seed=0 | MAE=1.1576e-01 | t=0.0070s
    tv | MR=0.1 | seed=0 | MAE=3.5553e-02 | t=0.1804s
    trss | MR=0.1 | seed=0 | MAE=3.2831e-02 | t=0.0189s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=2.4685e-01 | t=0.0107s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=4.6518e-01 | t=1.8507s
    mean | MR=0.1 | seed=1 | MAE=3.3104e-02 | t=0.0022s
    nearest | MR=0.1 | seed=1 | MAE=2.9433e-02 | t=0.0030s
    tikhonov | MR=0.1 | seed=1 | MAE=1.1378e-01 | t=0.0075s
    tv | MR=0.1 | seed=1 | MAE=3.3106e-02 | t=0.1927s
    trss | MR=0.1 | seed=1 | MAE=3.1419e-02 | t=0.0188s

Completed: 2026-04-15T00:36:18.343933+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.