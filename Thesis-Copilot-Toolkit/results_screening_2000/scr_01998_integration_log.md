# Integration Log: scr_01998
Started: 2026-04-16T10:07:18.703988+00:00
Description: Screening scr_01998 ds=iv100hz_mat graph=gaussian miss=[0.2] mode=noise

## Dataset: iv100hz_mat | rows=42
  Graph: gaussian__sigma0.6 built OK
    mean | MR=0.2 | seed=0 | MAE=1.6885e-02 | t=0.0020s
    nearest | MR=0.2 | seed=0 | MAE=2.5789e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=0 | MAE=4.7261e-02 | t=0.0057s
    tv | MR=0.2 | seed=0 | MAE=1.2611e-02 | t=0.1856s
    trss | MR=0.2 | seed=0 | MAE=1.2743e-02 | t=0.0204s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=7.6587e-02 | t=0.0083s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=9.3303e-02 | t=1.3227s
    mean | MR=0.2 | seed=1 | MAE=1.6813e-02 | t=0.0020s
    nearest | MR=0.2 | seed=1 | MAE=2.5845e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=1 | MAE=4.7318e-02 | t=0.0062s
    tv | MR=0.2 | seed=1 | MAE=1.0753e-02 | t=0.1848s
    trss | MR=0.2 | seed=1 | MAE=1.2807e-02 | t=0.0222s

Completed: 2026-04-16T10:07:18.704738+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.