# Integration Log: it150_039
Started: 2026-04-15T00:28:57.636398+00:00
Description: Bulk normalized run it150_039 dataset=bci_iv2a_real_s1 graph=gaussian miss=[0.1] mode=base

## Dataset: bci_iv2a_real_s1 | rows=42
  Graph: gaussian__sigma0.6 built OK
    mean | MR=0.1 | seed=0 | MAE=3.5667e-02 | t=0.0019s
    nearest | MR=0.1 | seed=0 | MAE=3.1361e-02 | t=0.0029s
    tikhonov | MR=0.1 | seed=0 | MAE=2.8344e-01 | t=0.0085s
    tv | MR=0.1 | seed=0 | MAE=3.5667e-02 | t=0.2363s
    trss | MR=0.1 | seed=0 | MAE=2.4354e-02 | t=0.0172s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=3.6447e-01 | t=0.0096s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=6.0592e-01 | t=1.8128s
    mean | MR=0.1 | seed=1 | MAE=3.3709e-02 | t=0.0030s
    nearest | MR=0.1 | seed=1 | MAE=3.1289e-02 | t=0.0043s
    tikhonov | MR=0.1 | seed=1 | MAE=2.8427e-01 | t=0.0077s
    tv | MR=0.1 | seed=1 | MAE=3.3709e-02 | t=0.2343s
    trss | MR=0.1 | seed=1 | MAE=2.2962e-02 | t=0.0170s

Completed: 2026-04-15T00:28:57.637275+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.