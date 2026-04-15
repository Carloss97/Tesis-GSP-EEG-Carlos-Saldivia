# Integration Log: it150_053
Started: 2026-04-15T00:31:43.139150+00:00
Description: Bulk normalized run it150_053 dataset=bci_iv2a_real_s3 graph=kalofolias miss=[0.1] mode=base

## Dataset: bci_iv2a_real_s3 | rows=42
  Graph: kalofolias built OK
    mean | MR=0.1 | seed=0 | MAE=3.5550e-02 | t=0.0022s
    nearest | MR=0.1 | seed=0 | MAE=2.9251e-02 | t=0.0035s
    tikhonov | MR=0.1 | seed=0 | MAE=1.8484e-01 | t=0.0075s
    tv | MR=0.1 | seed=0 | MAE=3.5550e-02 | t=0.2622s
    trss | MR=0.1 | seed=0 | MAE=2.5335e-02 | t=0.0191s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=3.2781e-01 | t=0.0114s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=6.3018e-01 | t=2.1918s
    mean | MR=0.1 | seed=1 | MAE=3.3104e-02 | t=0.0027s
    nearest | MR=0.1 | seed=1 | MAE=2.9433e-02 | t=0.0040s
    tikhonov | MR=0.1 | seed=1 | MAE=1.8354e-01 | t=0.0077s
    tv | MR=0.1 | seed=1 | MAE=3.3104e-02 | t=0.2514s
    trss | MR=0.1 | seed=1 | MAE=2.3608e-02 | t=0.0190s

Completed: 2026-04-15T00:31:43.140013+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.