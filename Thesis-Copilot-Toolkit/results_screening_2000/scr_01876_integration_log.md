# Integration Log: scr_01876
Started: 2026-04-16T09:49:28.342888+00:00
Description: Screening scr_01876 ds=bci_iv2a_real_s2 graph=gaussian miss=[0.1] mode=noise

## Dataset: bci_iv2a_real_s2 | rows=42
  Graph: gaussian__sigma1.0 built OK
    mean | MR=0.2 | seed=0 | MAE=3.0783e-02 | t=0.0020s
    nearest | MR=0.2 | seed=0 | MAE=3.0054e-02 | t=0.0041s
    tikhonov | MR=0.2 | seed=0 | MAE=1.3053e-01 | t=0.0057s
    tv | MR=0.2 | seed=0 | MAE=3.0783e-02 | t=0.1888s
    trss | MR=0.2 | seed=0 | MAE=2.3194e-02 | t=0.0202s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.2471e-01 | t=0.0080s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=7.2714e-01 | t=1.2403s
    mean | MR=0.2 | seed=1 | MAE=3.0057e-02 | t=0.0020s
    nearest | MR=0.2 | seed=1 | MAE=3.0917e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=1 | MAE=1.3065e-01 | t=0.0057s
    tv | MR=0.2 | seed=1 | MAE=3.0057e-02 | t=0.1958s
    trss | MR=0.2 | seed=1 | MAE=2.3001e-02 | t=0.0204s

Completed: 2026-04-16T09:49:28.343752+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.