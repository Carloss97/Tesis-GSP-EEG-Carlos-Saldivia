# Integration Log: scr_01827
Started: 2026-04-16T09:42:28.024136+00:00
Description: Screening scr_01827 ds=bci_iv2a_real_s1 graph=aew miss=3ch mode=noise

## Dataset: bci_iv2a_real_s1 | rows=42
  Graph: aew built OK
    mean | MR=0.2 | seed=0 | MAE=7.0461e-02 | t=0.0020s
    nearest | MR=0.2 | seed=0 | MAE=6.6301e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=0 | MAE=1.4152e-01 | t=0.0057s
    tv | MR=0.2 | seed=0 | MAE=7.0298e-02 | t=0.1534s
    trss | MR=0.2 | seed=0 | MAE=5.2901e-02 | t=0.0214s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.5006e-01 | t=0.0080s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=4.4687e-01 | t=2.9348s
    mean | MR=0.2 | seed=1 | MAE=6.9165e-02 | t=0.0020s
    nearest | MR=0.2 | seed=1 | MAE=6.3510e-02 | t=0.0041s
    tikhonov | MR=0.2 | seed=1 | MAE=1.3956e-01 | t=0.0064s
    tv | MR=0.2 | seed=1 | MAE=6.8993e-02 | t=0.1506s
    trss | MR=0.2 | seed=1 | MAE=5.2632e-02 | t=0.0206s

Completed: 2026-04-16T09:42:28.024994+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.