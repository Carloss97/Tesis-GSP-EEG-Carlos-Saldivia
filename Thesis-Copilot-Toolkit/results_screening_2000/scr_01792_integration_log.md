# Integration Log: scr_01792
Started: 2026-04-16T09:37:37.747793+00:00
Description: Screening scr_01792 ds=bci_iv2a_real_s2 graph=kalofolias miss=3ch mode=noise

## Dataset: bci_iv2a_real_s2 | rows=42
  Graph: kalofolias built OK
    mean | MR=0.2 | seed=0 | MAE=3.0783e-02 | t=0.0020s
    nearest | MR=0.2 | seed=0 | MAE=3.0054e-02 | t=0.0053s
    tikhonov | MR=0.2 | seed=0 | MAE=8.9370e-02 | t=0.0056s
    tv | MR=0.2 | seed=0 | MAE=3.0783e-02 | t=0.1869s
    trss | MR=0.2 | seed=0 | MAE=2.3194e-02 | t=0.0197s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.1061e-01 | t=0.0081s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=6.3515e-01 | t=1.2489s
    mean | MR=0.2 | seed=1 | MAE=3.0057e-02 | t=0.0020s
    nearest | MR=0.2 | seed=1 | MAE=3.0917e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=1 | MAE=8.9144e-02 | t=0.0057s
    tv | MR=0.2 | seed=1 | MAE=3.0057e-02 | t=0.1883s
    trss | MR=0.2 | seed=1 | MAE=2.3001e-02 | t=0.0205s

Completed: 2026-04-16T09:37:37.748669+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.