# Integration Log: it150_051
Started: 2026-04-15T00:30:58.126312+00:00
Description: Bulk normalized run it150_051 dataset=bci_iv2a_real_s1 graph=kalofolias miss=[0.1] mode=base

## Dataset: bci_iv2a_real_s1 | rows=42
  Graph: kalofolias built OK
    mean | MR=0.1 | seed=0 | MAE=3.5667e-02 | t=0.0024s
    nearest | MR=0.1 | seed=0 | MAE=3.1361e-02 | t=0.0087s
    tikhonov | MR=0.1 | seed=0 | MAE=1.8120e-01 | t=0.0099s
    tv | MR=0.1 | seed=0 | MAE=3.5667e-02 | t=0.2695s
    trss | MR=0.1 | seed=0 | MAE=2.4354e-02 | t=0.0201s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=3.1572e-01 | t=0.0096s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=5.2436e-01 | t=2.2524s
    mean | MR=0.1 | seed=1 | MAE=3.3709e-02 | t=0.0027s
    nearest | MR=0.1 | seed=1 | MAE=3.1289e-02 | t=0.0049s
    tikhonov | MR=0.1 | seed=1 | MAE=1.8088e-01 | t=0.0102s
    tv | MR=0.1 | seed=1 | MAE=3.3709e-02 | t=0.2670s
    trss | MR=0.1 | seed=1 | MAE=2.2962e-02 | t=0.0200s

Completed: 2026-04-15T00:30:58.127122+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.