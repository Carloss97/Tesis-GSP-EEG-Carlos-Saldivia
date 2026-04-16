# Integration Log: scr_01516
Started: 2026-04-16T08:58:35.453677+00:00
Description: Screening scr_01516 ds=bci_iv2a_real_s2 graph=knn miss=1ch mode=noise

## Dataset: bci_iv2a_real_s2 | rows=42
  Graph: knn__k3 built OK
    mean | MR=0.2 | seed=0 | MAE=3.0783e-02 | t=0.0020s
    nearest | MR=0.2 | seed=0 | MAE=3.0054e-02 | t=0.0041s
    tikhonov | MR=0.2 | seed=0 | MAE=7.1945e-02 | t=0.0056s
    tv | MR=0.2 | seed=0 | MAE=3.0784e-02 | t=0.1488s
    trss | MR=0.2 | seed=0 | MAE=2.7045e-02 | t=0.0194s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.9699e-01 | t=0.0080s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=5.4652e-01 | t=1.2786s
    mean | MR=0.2 | seed=1 | MAE=3.0057e-02 | t=0.0020s
    nearest | MR=0.2 | seed=1 | MAE=3.0917e-02 | t=0.0041s
    tikhonov | MR=0.2 | seed=1 | MAE=7.1334e-02 | t=0.0057s
    tv | MR=0.2 | seed=1 | MAE=3.0057e-02 | t=0.1452s
    trss | MR=0.2 | seed=1 | MAE=2.6431e-02 | t=0.0192s

Completed: 2026-04-16T08:58:35.454525+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.