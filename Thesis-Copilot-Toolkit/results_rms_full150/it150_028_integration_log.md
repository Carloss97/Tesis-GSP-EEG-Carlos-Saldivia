# Integration Log: it150_028
Started: 2026-04-15T00:27:01.471909+00:00
Description: Bulk normalized run it150_028 dataset=bci_iv2a_real_s2 graph=gaussian miss=[0.1] mode=base

## Dataset: bci_iv2a_real_s2 | rows=42
  Graph: gaussian__sigma1.0 built OK
    mean | MR=0.1 | seed=0 | MAE=1.3831e-02 | t=0.0029s
    nearest | MR=0.1 | seed=0 | MAE=1.3215e-02 | t=0.0053s
    tikhonov | MR=0.1 | seed=0 | MAE=1.2026e-01 | t=0.0100s
    tv | MR=0.1 | seed=0 | MAE=1.3831e-02 | t=0.2930s
    trss | MR=0.1 | seed=0 | MAE=9.8599e-03 | t=0.0198s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=2.2033e-01 | t=0.0115s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=7.2193e-01 | t=2.3709s
    mean | MR=0.1 | seed=1 | MAE=1.4351e-02 | t=0.0033s
    nearest | MR=0.1 | seed=1 | MAE=1.2774e-02 | t=0.0030s
    tikhonov | MR=0.1 | seed=1 | MAE=1.2058e-01 | t=0.0100s
    tv | MR=0.1 | seed=1 | MAE=1.4351e-02 | t=0.2838s
    trss | MR=0.1 | seed=1 | MAE=1.0391e-02 | t=0.0193s

Completed: 2026-04-15T00:27:01.473073+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.