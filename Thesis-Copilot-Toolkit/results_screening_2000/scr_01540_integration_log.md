# Integration Log: scr_01540
Started: 2026-04-16T09:02:00.531782+00:00
Description: Screening scr_01540 ds=bci_iv2a_real_s2 graph=knn miss=1ch mode=noise

## Dataset: bci_iv2a_real_s2 | rows=42
  Graph: knn__k7 built OK
    mean | MR=0.2 | seed=0 | MAE=3.0783e-02 | t=0.0020s
    nearest | MR=0.2 | seed=0 | MAE=3.0054e-02 | t=0.0041s
    tikhonov | MR=0.2 | seed=0 | MAE=1.0074e-01 | t=0.0057s
    tv | MR=0.2 | seed=0 | MAE=3.0784e-02 | t=0.1597s
    trss | MR=0.2 | seed=0 | MAE=2.5339e-02 | t=0.0206s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.1356e-01 | t=0.0083s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=6.6208e-01 | t=1.3410s
    mean | MR=0.2 | seed=1 | MAE=3.0057e-02 | t=0.0020s
    nearest | MR=0.2 | seed=1 | MAE=3.0917e-02 | t=0.0041s
    tikhonov | MR=0.2 | seed=1 | MAE=1.0018e-01 | t=0.0057s
    tv | MR=0.2 | seed=1 | MAE=3.0058e-02 | t=0.1624s
    trss | MR=0.2 | seed=1 | MAE=2.4873e-02 | t=0.0199s

Completed: 2026-04-16T09:02:00.532637+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.