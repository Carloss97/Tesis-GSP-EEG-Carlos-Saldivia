# Integration Log: it150_135
Started: 2026-04-15T00:56:47.238562+00:00
Description: Bulk normalized run it150_135 dataset=bci_iv2a_real_s1 graph=gaussian miss=[0.2] mode=base

## Dataset: bci_iv2a_real_s1 | rows=14
  Graph: gaussian__sigma0.6 built OK
    mean | MR=0.2 | seed=0 | MAE=6.9320e-02 | t=0.0026s
    nearest | MR=0.2 | seed=0 | MAE=6.3326e-02 | t=0.0048s
    tikhonov | MR=0.2 | seed=0 | MAE=3.0215e-01 | t=0.0069s
    tv | MR=0.2 | seed=0 | MAE=6.9320e-02 | t=0.2304s
    trss | MR=0.2 | seed=0 | MAE=4.8399e-02 | t=0.0205s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=3.7510e-01 | t=0.0100s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=6.1306e-01 | t=1.7639s
    mean | MR=0.2 | seed=1 | MAE=6.8278e-02 | t=0.0023s
    nearest | MR=0.2 | seed=1 | MAE=6.1642e-02 | t=0.0053s
    tikhonov | MR=0.2 | seed=1 | MAE=2.9806e-01 | t=0.0083s
    tv | MR=0.2 | seed=1 | MAE=6.8278e-02 | t=0.2340s
    trss | MR=0.2 | seed=1 | MAE=4.8018e-02 | t=0.0199s

Completed: 2026-04-15T00:56:47.239381+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.