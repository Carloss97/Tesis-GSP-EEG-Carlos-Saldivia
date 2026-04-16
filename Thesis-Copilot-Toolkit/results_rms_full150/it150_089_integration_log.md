# Integration Log: it150_089
Started: 2026-04-15T00:38:17.854641+00:00
Description: Bulk normalized run it150_089 dataset=bci_iv2a_real_s3 graph=aew miss=[0.1] mode=base

## Dataset: bci_iv2a_real_s3 | rows=42
  Graph: aew built OK
    mean | MR=0.1 | seed=0 | MAE=3.5550e-02 | t=0.0027s
    nearest | MR=0.1 | seed=0 | MAE=2.9251e-02 | t=0.0047s
    tikhonov | MR=0.1 | seed=0 | MAE=1.3118e-01 | t=0.0083s
    tv | MR=0.1 | seed=0 | MAE=3.5551e-02 | t=0.1949s
    trss | MR=0.1 | seed=0 | MAE=3.0797e-02 | t=0.0187s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=2.6343e-01 | t=0.0106s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=5.4003e-01 | t=1.7511s
    mean | MR=0.1 | seed=1 | MAE=3.3104e-02 | t=0.0026s
    nearest | MR=0.1 | seed=1 | MAE=2.9433e-02 | t=0.0036s
    tikhonov | MR=0.1 | seed=1 | MAE=1.2854e-01 | t=0.0072s
    tv | MR=0.1 | seed=1 | MAE=3.3102e-02 | t=0.2397s
    trss | MR=0.1 | seed=1 | MAE=2.9250e-02 | t=0.0190s

Completed: 2026-04-15T00:38:17.855607+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.