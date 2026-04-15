# Integration Log: it150_136
Started: 2026-04-15T00:56:56.542988+00:00
Description: Bulk normalized run it150_136 dataset=bci_iv2a_real_s2 graph=gaussian miss=[0.2] mode=base

## Dataset: bci_iv2a_real_s2 | rows=14
  Graph: gaussian__sigma0.6 built OK
    mean | MR=0.2 | seed=0 | MAE=2.9528e-02 | t=0.0024s
    nearest | MR=0.2 | seed=0 | MAE=2.7159e-02 | t=0.0055s
    tikhonov | MR=0.2 | seed=0 | MAE=1.2533e-01 | t=0.0065s
    tv | MR=0.2 | seed=0 | MAE=2.9528e-02 | t=0.2419s
    trss | MR=0.2 | seed=0 | MAE=2.1299e-02 | t=0.0200s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.2060e-01 | t=0.0110s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=7.2735e-01 | t=2.7181s
    mean | MR=0.2 | seed=1 | MAE=2.8797e-02 | t=0.0021s
    nearest | MR=0.2 | seed=1 | MAE=2.8346e-02 | t=0.0078s
    tikhonov | MR=0.2 | seed=1 | MAE=1.2523e-01 | t=0.0075s
    tv | MR=0.2 | seed=1 | MAE=2.8797e-02 | t=0.2487s
    trss | MR=0.2 | seed=1 | MAE=2.1400e-02 | t=0.0199s

Completed: 2026-04-15T00:56:56.543961+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.