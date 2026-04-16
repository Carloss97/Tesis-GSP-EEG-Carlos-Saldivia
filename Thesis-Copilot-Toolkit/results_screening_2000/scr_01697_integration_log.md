# Integration Log: scr_01697
Started: 2026-04-16T09:24:19.597990+00:00
Description: Screening scr_01697 ds=bci_iv2a_real_s3 graph=knng miss=2ch mode=noise

## Dataset: bci_iv2a_real_s3 | rows=42
  Graph: knng built OK
    mean | MR=0.2 | seed=0 | MAE=6.5964e-02 | t=0.0020s
    nearest | MR=0.2 | seed=0 | MAE=6.1958e-02 | t=0.0047s
    tikhonov | MR=0.2 | seed=0 | MAE=1.8750e-01 | t=0.0057s
    tv | MR=0.2 | seed=0 | MAE=6.5968e-02 | t=0.1542s
    trss | MR=0.2 | seed=0 | MAE=5.9177e-02 | t=0.0198s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=3.1453e-01 | t=0.0081s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=6.1825e-01 | t=2.7439s
    mean | MR=0.2 | seed=1 | MAE=6.8819e-02 | t=0.0020s
    nearest | MR=0.2 | seed=1 | MAE=6.0295e-02 | t=0.0041s
    tikhonov | MR=0.2 | seed=1 | MAE=1.8942e-01 | t=0.0058s
    tv | MR=0.2 | seed=1 | MAE=6.8824e-02 | t=0.1558s
    trss | MR=0.2 | seed=1 | MAE=6.2587e-02 | t=0.0203s

Completed: 2026-04-16T09:24:19.598881+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.