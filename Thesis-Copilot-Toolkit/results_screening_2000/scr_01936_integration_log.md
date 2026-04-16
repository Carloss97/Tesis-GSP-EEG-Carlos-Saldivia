# Integration Log: scr_01936
Started: 2026-04-16T09:58:02.710521+00:00
Description: Screening scr_01936 ds=bci_iv2a_real_s2 graph=aew miss=[0.1] mode=noise

## Dataset: bci_iv2a_real_s2 | rows=42
  Graph: aew built OK
    mean | MR=0.2 | seed=0 | MAE=3.0783e-02 | t=0.0020s
    nearest | MR=0.2 | seed=0 | MAE=3.0054e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=0 | MAE=7.6077e-02 | t=0.0057s
    tv | MR=0.2 | seed=0 | MAE=3.0783e-02 | t=0.1530s
    trss | MR=0.2 | seed=0 | MAE=2.6708e-02 | t=0.0203s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.9851e-01 | t=0.0086s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=5.7593e-01 | t=1.5527s
    mean | MR=0.2 | seed=1 | MAE=3.0057e-02 | t=0.0020s
    nearest | MR=0.2 | seed=1 | MAE=3.0917e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=1 | MAE=7.5221e-02 | t=0.0057s
    tv | MR=0.2 | seed=1 | MAE=3.0056e-02 | t=0.1487s
    trss | MR=0.2 | seed=1 | MAE=2.6108e-02 | t=0.0198s

Completed: 2026-04-16T09:58:02.711381+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.