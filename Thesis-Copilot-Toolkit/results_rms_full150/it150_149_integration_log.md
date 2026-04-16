# Integration Log: it150_149
Started: 2026-04-15T00:58:27.169070+00:00
Description: Bulk normalized run it150_149 dataset=bci_iv2a_real_s3 graph=kalofolias miss=[0.2] mode=base

## Dataset: bci_iv2a_real_s3 | rows=14
  Graph: kalofolias built OK
    mean | MR=0.2 | seed=0 | MAE=6.5815e-02 | t=0.0022s
    nearest | MR=0.2 | seed=0 | MAE=6.1045e-02 | t=0.0047s
    tikhonov | MR=0.2 | seed=0 | MAE=2.0287e-01 | t=0.0078s
    tv | MR=0.2 | seed=0 | MAE=6.5815e-02 | t=0.2327s
    trss | MR=0.2 | seed=0 | MAE=4.8316e-02 | t=0.0203s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=3.3450e-01 | t=0.0091s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=6.4508e-01 | t=1.8901s
    mean | MR=0.2 | seed=1 | MAE=6.8917e-02 | t=0.0028s
    nearest | MR=0.2 | seed=1 | MAE=5.9347e-02 | t=0.0066s
    tikhonov | MR=0.2 | seed=1 | MAE=2.0465e-01 | t=0.0079s
    tv | MR=0.2 | seed=1 | MAE=6.8917e-02 | t=0.2336s
    trss | MR=0.2 | seed=1 | MAE=5.1312e-02 | t=0.0196s

Completed: 2026-04-15T00:58:27.169863+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.