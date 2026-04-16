# Integration Log: it150_125
Started: 2026-04-15T00:55:41.326991+00:00
Description: Bulk normalized run it150_125 dataset=bci_iv2a_real_s3 graph=gaussian miss=[0.2] mode=base

## Dataset: bci_iv2a_real_s3 | rows=14
  Graph: gaussian__sigma1.0 built OK
    mean | MR=0.2 | seed=0 | MAE=6.5815e-02 | t=0.0022s
    nearest | MR=0.2 | seed=0 | MAE=6.1045e-02 | t=0.0048s
    tikhonov | MR=0.2 | seed=0 | MAE=2.9914e-01 | t=0.0095s
    tv | MR=0.2 | seed=0 | MAE=6.5815e-02 | t=0.2351s
    trss | MR=0.2 | seed=0 | MAE=4.8316e-02 | t=0.0193s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=3.7966e-01 | t=0.0106s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=7.3605e-01 | t=2.1054s
    mean | MR=0.2 | seed=1 | MAE=6.8917e-02 | t=0.0023s
    nearest | MR=0.2 | seed=1 | MAE=5.9347e-02 | t=0.0046s
    tikhonov | MR=0.2 | seed=1 | MAE=3.0000e-01 | t=0.0096s
    tv | MR=0.2 | seed=1 | MAE=6.8917e-02 | t=0.2538s
    trss | MR=0.2 | seed=1 | MAE=5.1312e-02 | t=0.0210s

Completed: 2026-04-15T00:55:41.328222+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.