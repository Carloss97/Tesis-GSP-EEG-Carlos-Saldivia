# Integration Log: scr_01613
Started: 2026-04-16T09:12:28.442405+00:00
Description: Screening scr_01613 ds=bci_iv2a_real_s3 graph=aew miss=1ch mode=noise

## Dataset: bci_iv2a_real_s3 | rows=42
  Graph: aew built OK
    mean | MR=0.2 | seed=0 | MAE=6.5964e-02 | t=0.0020s
    nearest | MR=0.2 | seed=0 | MAE=6.1958e-02 | t=0.0041s
    tikhonov | MR=0.2 | seed=0 | MAE=1.5528e-01 | t=0.0063s
    tv | MR=0.2 | seed=0 | MAE=6.5962e-02 | t=0.1504s
    trss | MR=0.2 | seed=0 | MAE=5.8282e-02 | t=0.0198s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.7682e-01 | t=0.0080s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=5.5935e-01 | t=1.2730s
    mean | MR=0.2 | seed=1 | MAE=6.8819e-02 | t=0.0020s
    nearest | MR=0.2 | seed=1 | MAE=6.0295e-02 | t=0.0041s
    tikhonov | MR=0.2 | seed=1 | MAE=1.5756e-01 | t=0.0057s
    tv | MR=0.2 | seed=1 | MAE=6.8821e-02 | t=0.1507s
    trss | MR=0.2 | seed=1 | MAE=6.1539e-02 | t=0.0198s

Completed: 2026-04-16T09:12:28.443257+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.