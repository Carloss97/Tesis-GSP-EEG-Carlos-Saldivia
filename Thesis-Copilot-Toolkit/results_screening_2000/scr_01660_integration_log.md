# Integration Log: scr_01660
Started: 2026-04-16T09:19:00.510396+00:00
Description: Screening scr_01660 ds=bci_iv2a_real_s2 graph=gaussian miss=2ch mode=noise

## Dataset: bci_iv2a_real_s2 | rows=42
  Graph: gaussian__sigma1.0 built OK
    mean | MR=0.2 | seed=0 | MAE=3.0783e-02 | t=0.0020s
    nearest | MR=0.2 | seed=0 | MAE=3.0054e-02 | t=0.0043s
    tikhonov | MR=0.2 | seed=0 | MAE=1.3053e-01 | t=0.0057s
    tv | MR=0.2 | seed=0 | MAE=3.0783e-02 | t=0.1900s
    trss | MR=0.2 | seed=0 | MAE=2.3194e-02 | t=0.0193s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.2471e-01 | t=0.0086s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=7.2714e-01 | t=1.3603s
    mean | MR=0.2 | seed=1 | MAE=3.0057e-02 | t=0.0020s
    nearest | MR=0.2 | seed=1 | MAE=3.0917e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=1 | MAE=1.3065e-01 | t=0.0064s
    tv | MR=0.2 | seed=1 | MAE=3.0057e-02 | t=0.1886s
    trss | MR=0.2 | seed=1 | MAE=2.3001e-02 | t=0.0196s

Completed: 2026-04-16T09:19:00.511264+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.