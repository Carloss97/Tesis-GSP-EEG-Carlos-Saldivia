# Integration Log: it150_124
Started: 2026-04-15T00:55:32.363293+00:00
Description: Bulk normalized run it150_124 dataset=bci_iv2a_real_s2 graph=gaussian miss=[0.2] mode=base

## Dataset: bci_iv2a_real_s2 | rows=14
  Graph: gaussian__sigma1.0 built OK
    mean | MR=0.2 | seed=0 | MAE=2.9528e-02 | t=0.0020s
    nearest | MR=0.2 | seed=0 | MAE=2.7159e-02 | t=0.0044s
    tikhonov | MR=0.2 | seed=0 | MAE=1.2533e-01 | t=0.0067s
    tv | MR=0.2 | seed=0 | MAE=2.9528e-02 | t=0.2294s
    trss | MR=0.2 | seed=0 | MAE=2.1299e-02 | t=0.0201s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.2060e-01 | t=0.0096s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=7.2735e-01 | t=1.8401s
    mean | MR=0.2 | seed=1 | MAE=2.8797e-02 | t=0.0024s
    nearest | MR=0.2 | seed=1 | MAE=2.8346e-02 | t=0.0053s
    tikhonov | MR=0.2 | seed=1 | MAE=1.2523e-01 | t=0.0067s
    tv | MR=0.2 | seed=1 | MAE=2.8797e-02 | t=0.2231s
    trss | MR=0.2 | seed=1 | MAE=2.1400e-02 | t=0.0193s

Completed: 2026-04-15T00:55:32.364239+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.