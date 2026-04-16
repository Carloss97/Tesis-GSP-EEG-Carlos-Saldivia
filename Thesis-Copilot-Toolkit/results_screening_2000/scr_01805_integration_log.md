# Integration Log: scr_01805
Started: 2026-04-16T09:39:35.466422+00:00
Description: Screening scr_01805 ds=bci_iv2a_real_s3 graph=knng miss=3ch mode=noise

## Dataset: bci_iv2a_real_s3 | rows=42
  Graph: knng built OK
    mean | MR=0.2 | seed=0 | MAE=6.5964e-02 | t=0.0020s
    nearest | MR=0.2 | seed=0 | MAE=6.1958e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=0 | MAE=1.8750e-01 | t=0.0057s
    tv | MR=0.2 | seed=0 | MAE=6.5968e-02 | t=0.1494s
    trss | MR=0.2 | seed=0 | MAE=5.9177e-02 | t=0.0207s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=3.1453e-01 | t=0.0080s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=6.1825e-01 | t=2.6518s
    mean | MR=0.2 | seed=1 | MAE=6.8819e-02 | t=0.0020s
    nearest | MR=0.2 | seed=1 | MAE=6.0295e-02 | t=0.0043s
    tikhonov | MR=0.2 | seed=1 | MAE=1.8942e-01 | t=0.0067s
    tv | MR=0.2 | seed=1 | MAE=6.8824e-02 | t=0.1508s
    trss | MR=0.2 | seed=1 | MAE=6.2587e-02 | t=0.0198s

Completed: 2026-04-16T09:39:35.467125+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.