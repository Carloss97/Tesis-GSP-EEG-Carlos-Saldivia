# Integration Log: scr_01948
Started: 2026-04-16T09:59:42.083899+00:00
Description: Screening scr_01948 ds=bci_iv2a_real_s2 graph=knn miss=[0.2] mode=noise

## Dataset: bci_iv2a_real_s2 | rows=42
  Graph: knn__k3 built OK
    mean | MR=0.2 | seed=0 | MAE=3.0783e-02 | t=0.0020s
    nearest | MR=0.2 | seed=0 | MAE=3.0054e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=0 | MAE=7.1945e-02 | t=0.0056s
    tv | MR=0.2 | seed=0 | MAE=3.0784e-02 | t=0.1494s
    trss | MR=0.2 | seed=0 | MAE=2.7045e-02 | t=0.0213s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.9699e-01 | t=0.0082s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=5.4652e-01 | t=1.2444s
    mean | MR=0.2 | seed=1 | MAE=3.0057e-02 | t=0.0020s
    nearest | MR=0.2 | seed=1 | MAE=3.0917e-02 | t=0.0043s
    tikhonov | MR=0.2 | seed=1 | MAE=7.1334e-02 | t=0.0056s
    tv | MR=0.2 | seed=1 | MAE=3.0057e-02 | t=0.1469s
    trss | MR=0.2 | seed=1 | MAE=2.6431e-02 | t=0.0203s

Completed: 2026-04-16T09:59:42.084614+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.