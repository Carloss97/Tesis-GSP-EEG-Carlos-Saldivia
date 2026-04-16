# Integration Log: it150_123
Started: 2026-04-15T00:44:53.467864+00:00
Description: Bulk normalized run it150_123 dataset=bci_iv2a_real_s1 graph=gaussian miss=[0.2] mode=base

## Dataset: bci_iv2a_real_s1 | rows=42
  Graph: gaussian__sigma1.0 built OK
    mean | MR=0.2 | seed=0 | MAE=6.9320e-02 | t=0.0023s
    nearest | MR=0.2 | seed=0 | MAE=6.3326e-02 | t=0.0048s
    tikhonov | MR=0.2 | seed=0 | MAE=3.0215e-01 | t=0.0086s
    tv | MR=0.2 | seed=0 | MAE=6.9320e-02 | t=0.2788s
    trss | MR=0.2 | seed=0 | MAE=4.8399e-02 | t=0.0212s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=3.7510e-01 | t=0.0123s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=6.1306e-01 | t=2.8588s
    mean | MR=0.2 | seed=1 | MAE=6.8278e-02 | t=0.0030s
    nearest | MR=0.2 | seed=1 | MAE=6.1642e-02 | t=0.0053s
    tikhonov | MR=0.2 | seed=1 | MAE=2.9806e-01 | t=0.0076s
    tv | MR=0.2 | seed=1 | MAE=6.8278e-02 | t=0.2650s
    trss | MR=0.2 | seed=1 | MAE=4.8018e-02 | t=0.0197s

Completed: 2026-04-15T00:44:53.469058+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.