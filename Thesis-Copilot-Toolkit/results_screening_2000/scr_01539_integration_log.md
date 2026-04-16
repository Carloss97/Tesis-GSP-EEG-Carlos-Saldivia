# Integration Log: scr_01539
Started: 2026-04-16T09:01:46.111476+00:00
Description: Screening scr_01539 ds=bci_iv2a_real_s1 graph=knn miss=1ch mode=noise

## Dataset: bci_iv2a_real_s1 | rows=42
  Graph: knn__k7 built OK
    mean | MR=0.2 | seed=0 | MAE=7.0461e-02 | t=0.0031s
    nearest | MR=0.2 | seed=0 | MAE=6.6301e-02 | t=0.0044s
    tikhonov | MR=0.2 | seed=0 | MAE=2.2640e-01 | t=0.0064s
    tv | MR=0.2 | seed=0 | MAE=7.0454e-02 | t=0.1617s
    trss | MR=0.2 | seed=0 | MAE=4.6421e-02 | t=0.0194s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=3.4390e-01 | t=0.0089s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=5.5263e-01 | t=1.2457s
    mean | MR=0.2 | seed=1 | MAE=6.9165e-02 | t=0.0020s
    nearest | MR=0.2 | seed=1 | MAE=6.3510e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=1 | MAE=2.2211e-01 | t=0.0057s
    tv | MR=0.2 | seed=1 | MAE=6.9158e-02 | t=0.1628s
    trss | MR=0.2 | seed=1 | MAE=4.7272e-02 | t=0.0192s

Completed: 2026-04-16T09:01:46.112185+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.