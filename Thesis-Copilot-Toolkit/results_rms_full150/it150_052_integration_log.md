# Integration Log: it150_052
Started: 2026-04-15T00:31:21.800086+00:00
Description: Bulk normalized run it150_052 dataset=bci_iv2a_real_s2 graph=kalofolias miss=[0.1] mode=base

## Dataset: bci_iv2a_real_s2 | rows=42
  Graph: kalofolias built OK
    mean | MR=0.1 | seed=0 | MAE=1.3831e-02 | t=0.0036s
    nearest | MR=0.1 | seed=0 | MAE=1.3215e-02 | t=0.0043s
    tikhonov | MR=0.1 | seed=0 | MAE=7.6346e-02 | t=0.0090s
    tv | MR=0.1 | seed=0 | MAE=1.3831e-02 | t=0.2572s
    trss | MR=0.1 | seed=0 | MAE=9.8599e-03 | t=0.0199s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=2.0525e-01 | t=0.0112s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=6.2147e-01 | t=2.7274s
    mean | MR=0.1 | seed=1 | MAE=1.4351e-02 | t=0.0023s
    nearest | MR=0.1 | seed=1 | MAE=1.2774e-02 | t=0.0029s
    tikhonov | MR=0.1 | seed=1 | MAE=7.6749e-02 | t=0.0079s
    tv | MR=0.1 | seed=1 | MAE=1.4351e-02 | t=0.3185s
    trss | MR=0.1 | seed=1 | MAE=1.0391e-02 | t=0.0199s

Completed: 2026-04-15T00:31:21.801623+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.