# Integration Log: scr_01661
Started: 2026-04-16T09:19:16.170934+00:00
Description: Screening scr_01661 ds=bci_iv2a_real_s3 graph=gaussian miss=2ch mode=noise

## Dataset: bci_iv2a_real_s3 | rows=42
  Graph: gaussian__sigma1.0 built OK
    mean | MR=0.2 | seed=0 | MAE=6.5964e-02 | t=0.0020s
    nearest | MR=0.2 | seed=0 | MAE=6.1958e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=0 | MAE=2.9997e-01 | t=0.0057s
    tv | MR=0.2 | seed=0 | MAE=6.5964e-02 | t=0.1921s
    trss | MR=0.2 | seed=0 | MAE=4.8650e-02 | t=0.0196s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=3.8100e-01 | t=0.0082s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=7.3544e-01 | t=2.5130s
    mean | MR=0.2 | seed=1 | MAE=6.8819e-02 | t=0.0020s
    nearest | MR=0.2 | seed=1 | MAE=6.0295e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=1 | MAE=3.0179e-01 | t=0.0073s
    tv | MR=0.2 | seed=1 | MAE=6.8819e-02 | t=0.1923s
    trss | MR=0.2 | seed=1 | MAE=5.1583e-02 | t=0.0193s

Completed: 2026-04-16T09:19:16.171864+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.