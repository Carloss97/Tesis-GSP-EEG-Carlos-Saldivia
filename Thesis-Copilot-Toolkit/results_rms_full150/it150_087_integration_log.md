# Integration Log: it150_087
Started: 2026-04-15T00:37:39.564224+00:00
Description: Bulk normalized run it150_087 dataset=bci_iv2a_real_s1 graph=aew miss=[0.1] mode=base

## Dataset: bci_iv2a_real_s1 | rows=42
  Graph: aew built OK
    mean | MR=0.1 | seed=0 | MAE=3.5667e-02 | t=0.0031s
    nearest | MR=0.1 | seed=0 | MAE=3.1361e-02 | t=0.0032s
    tikhonov | MR=0.1 | seed=0 | MAE=1.1494e-01 | t=0.0096s
    tv | MR=0.1 | seed=0 | MAE=3.5590e-02 | t=0.2052s
    trss | MR=0.1 | seed=0 | MAE=2.7095e-02 | t=0.0193s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=2.2871e-01 | t=0.0097s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=4.2676e-01 | t=2.7427s
    mean | MR=0.1 | seed=1 | MAE=3.3709e-02 | t=0.0022s
    nearest | MR=0.1 | seed=1 | MAE=3.1289e-02 | t=0.0035s
    tikhonov | MR=0.1 | seed=1 | MAE=1.1256e-01 | t=0.0069s
    tv | MR=0.1 | seed=1 | MAE=3.3639e-02 | t=0.1867s
    trss | MR=0.1 | seed=1 | MAE=2.5218e-02 | t=0.0190s

Completed: 2026-04-15T00:37:39.565213+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.