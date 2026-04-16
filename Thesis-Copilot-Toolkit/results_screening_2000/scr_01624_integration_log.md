# Integration Log: scr_01624
Started: 2026-04-16T09:13:57.443462+00:00
Description: Screening scr_01624 ds=bci_iv2a_real_s2 graph=knn miss=2ch mode=noise

## Dataset: bci_iv2a_real_s2 | rows=42
  Graph: knn__k3 built OK
    mean | MR=0.2 | seed=0 | MAE=3.0783e-02 | t=0.0021s
    nearest | MR=0.2 | seed=0 | MAE=3.0054e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=0 | MAE=7.1945e-02 | t=0.0058s
    tv | MR=0.2 | seed=0 | MAE=3.0784e-02 | t=0.1478s
    trss | MR=0.2 | seed=0 | MAE=2.7045e-02 | t=0.0207s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.9699e-01 | t=0.0085s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=5.4652e-01 | t=1.2892s
    mean | MR=0.2 | seed=1 | MAE=3.0057e-02 | t=0.0022s
    nearest | MR=0.2 | seed=1 | MAE=3.0917e-02 | t=0.0045s
    tikhonov | MR=0.2 | seed=1 | MAE=7.1334e-02 | t=0.0057s
    tv | MR=0.2 | seed=1 | MAE=3.0057e-02 | t=0.1464s
    trss | MR=0.2 | seed=1 | MAE=2.6431e-02 | t=0.0202s

Completed: 2026-04-16T09:13:57.444167+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.