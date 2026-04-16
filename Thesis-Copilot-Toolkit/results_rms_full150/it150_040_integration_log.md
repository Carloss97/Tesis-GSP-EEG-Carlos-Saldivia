# Integration Log: it150_040
Started: 2026-04-15T00:29:17.976680+00:00
Description: Bulk normalized run it150_040 dataset=bci_iv2a_real_s2 graph=gaussian miss=[0.1] mode=base

## Dataset: bci_iv2a_real_s2 | rows=42
  Graph: gaussian__sigma0.6 built OK
    mean | MR=0.1 | seed=0 | MAE=1.3831e-02 | t=0.0023s
    nearest | MR=0.1 | seed=0 | MAE=1.3215e-02 | t=0.0038s
    tikhonov | MR=0.1 | seed=0 | MAE=1.2026e-01 | t=0.0071s
    tv | MR=0.1 | seed=0 | MAE=1.3831e-02 | t=0.2262s
    trss | MR=0.1 | seed=0 | MAE=9.8599e-03 | t=0.0175s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=2.2033e-01 | t=0.0095s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=7.2193e-01 | t=1.7012s
    mean | MR=0.1 | seed=1 | MAE=1.4351e-02 | t=0.0032s
    nearest | MR=0.1 | seed=1 | MAE=1.2774e-02 | t=0.0035s
    tikhonov | MR=0.1 | seed=1 | MAE=1.2058e-01 | t=0.0076s
    tv | MR=0.1 | seed=1 | MAE=1.4351e-02 | t=0.2306s
    trss | MR=0.1 | seed=1 | MAE=1.0391e-02 | t=0.0184s

Completed: 2026-04-15T00:29:17.977727+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.