# Integration Log: it150_147
Started: 2026-04-15T00:58:11.300245+00:00
Description: Bulk normalized run it150_147 dataset=bci_iv2a_real_s1 graph=kalofolias miss=[0.2] mode=base

## Dataset: bci_iv2a_real_s1 | rows=14
  Graph: kalofolias built OK
    mean | MR=0.2 | seed=0 | MAE=6.9320e-02 | t=0.0024s
    nearest | MR=0.2 | seed=0 | MAE=6.3326e-02 | t=0.0062s
    tikhonov | MR=0.2 | seed=0 | MAE=2.0608e-01 | t=0.0076s
    tv | MR=0.2 | seed=0 | MAE=6.9320e-02 | t=0.2685s
    trss | MR=0.2 | seed=0 | MAE=4.8399e-02 | t=0.0209s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=3.2957e-01 | t=0.0195s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=5.3769e-01 | t=3.0590s
    mean | MR=0.2 | seed=1 | MAE=6.8278e-02 | t=0.0022s
    nearest | MR=0.2 | seed=1 | MAE=6.1642e-02 | t=0.0049s
    tikhonov | MR=0.2 | seed=1 | MAE=2.0325e-01 | t=0.0079s
    tv | MR=0.2 | seed=1 | MAE=6.8278e-02 | t=0.2410s
    trss | MR=0.2 | seed=1 | MAE=4.8018e-02 | t=0.0201s

Completed: 2026-04-15T00:58:11.301275+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.