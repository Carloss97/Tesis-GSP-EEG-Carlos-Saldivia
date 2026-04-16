# Integration Log: scr_01923
Started: 2026-04-16T09:56:00.034112+00:00
Description: Screening scr_01923 ds=bci_iv2a_real_s1 graph=vknng miss=[0.1] mode=noise

## Dataset: bci_iv2a_real_s1 | rows=42
  Graph: vknng built OK
    mean | MR=0.2 | seed=0 | MAE=7.0461e-02 | t=0.0022s
    nearest | MR=0.2 | seed=0 | MAE=6.6301e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=0 | MAE=1.3943e-01 | t=0.0058s
    tv | MR=0.2 | seed=0 | MAE=7.0454e-02 | t=0.1429s
    trss | MR=0.2 | seed=0 | MAE=5.5601e-02 | t=0.0201s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.5521e-01 | t=0.0081s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=4.1331e-01 | t=1.2418s
    mean | MR=0.2 | seed=1 | MAE=6.9165e-02 | t=0.0020s
    nearest | MR=0.2 | seed=1 | MAE=6.3510e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=1 | MAE=1.3710e-01 | t=0.0057s
    tv | MR=0.2 | seed=1 | MAE=6.9158e-02 | t=0.1419s
    trss | MR=0.2 | seed=1 | MAE=5.6157e-02 | t=0.0196s

Completed: 2026-04-16T09:56:00.034821+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.