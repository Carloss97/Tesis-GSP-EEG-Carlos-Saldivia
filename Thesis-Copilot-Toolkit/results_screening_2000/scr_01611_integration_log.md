# Integration Log: scr_01611
Started: 2026-04-16T09:11:56.935223+00:00
Description: Screening scr_01611 ds=bci_iv2a_real_s1 graph=aew miss=1ch mode=noise

## Dataset: bci_iv2a_real_s1 | rows=42
  Graph: aew built OK
    mean | MR=0.2 | seed=0 | MAE=7.0461e-02 | t=0.0020s
    nearest | MR=0.2 | seed=0 | MAE=6.6301e-02 | t=0.0041s
    tikhonov | MR=0.2 | seed=0 | MAE=1.4152e-01 | t=0.0066s
    tv | MR=0.2 | seed=0 | MAE=7.0298e-02 | t=0.1498s
    trss | MR=0.2 | seed=0 | MAE=5.2901e-02 | t=0.0210s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.5006e-01 | t=0.0080s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=4.4687e-01 | t=2.7165s
    mean | MR=0.2 | seed=1 | MAE=6.9165e-02 | t=0.0041s
    nearest | MR=0.2 | seed=1 | MAE=6.3510e-02 | t=0.0047s
    tikhonov | MR=0.2 | seed=1 | MAE=1.3956e-01 | t=0.0057s
    tv | MR=0.2 | seed=1 | MAE=6.8993e-02 | t=0.1545s
    trss | MR=0.2 | seed=1 | MAE=5.2632e-02 | t=0.0204s

Completed: 2026-04-16T09:11:56.936087+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.