# Integration Log: it150_088
Started: 2026-04-15T00:37:59.303554+00:00
Description: Bulk normalized run it150_088 dataset=bci_iv2a_real_s2 graph=aew miss=[0.1] mode=base

## Dataset: bci_iv2a_real_s2 | rows=42
  Graph: aew built OK
    mean | MR=0.1 | seed=0 | MAE=1.3831e-02 | t=0.0025s
    nearest | MR=0.1 | seed=0 | MAE=1.3215e-02 | t=0.0033s
    tikhonov | MR=0.1 | seed=0 | MAE=6.1494e-02 | t=0.0063s
    tv | MR=0.1 | seed=0 | MAE=1.3830e-02 | t=0.2084s
    trss | MR=0.1 | seed=0 | MAE=1.1505e-02 | t=0.0193s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=1.9213e-01 | t=0.0096s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=5.5822e-01 | t=1.8368s
    mean | MR=0.1 | seed=1 | MAE=1.4351e-02 | t=0.0021s
    nearest | MR=0.1 | seed=1 | MAE=1.2774e-02 | t=0.0038s
    tikhonov | MR=0.1 | seed=1 | MAE=6.1667e-02 | t=0.0070s
    tv | MR=0.1 | seed=1 | MAE=1.4350e-02 | t=0.1918s
    trss | MR=0.1 | seed=1 | MAE=1.1688e-02 | t=0.0190s

Completed: 2026-04-15T00:37:59.304512+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.