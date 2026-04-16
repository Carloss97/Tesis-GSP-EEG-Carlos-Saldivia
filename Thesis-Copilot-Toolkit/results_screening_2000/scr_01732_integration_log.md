# Integration Log: scr_01732
Started: 2026-04-16T09:29:05.383772+00:00
Description: Screening scr_01732 ds=bci_iv2a_real_s2 graph=knn miss=3ch mode=noise

## Dataset: bci_iv2a_real_s2 | rows=42
  Graph: knn__k3 built OK
    mean | MR=0.2 | seed=0 | MAE=3.0783e-02 | t=0.0020s
    nearest | MR=0.2 | seed=0 | MAE=3.0054e-02 | t=0.0045s
    tikhonov | MR=0.2 | seed=0 | MAE=7.1945e-02 | t=0.0063s
    tv | MR=0.2 | seed=0 | MAE=3.0784e-02 | t=0.1445s
    trss | MR=0.2 | seed=0 | MAE=2.7045e-02 | t=0.0192s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.9699e-01 | t=0.0083s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=5.4652e-01 | t=1.4299s
    mean | MR=0.2 | seed=1 | MAE=3.0057e-02 | t=0.0029s
    nearest | MR=0.2 | seed=1 | MAE=3.0917e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=1 | MAE=7.1334e-02 | t=0.0057s
    tv | MR=0.2 | seed=1 | MAE=3.0057e-02 | t=0.1455s
    trss | MR=0.2 | seed=1 | MAE=2.6431e-02 | t=0.0200s

Completed: 2026-04-16T09:29:05.384542+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.