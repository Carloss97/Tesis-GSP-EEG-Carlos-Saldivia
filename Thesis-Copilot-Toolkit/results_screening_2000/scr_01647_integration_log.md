# Integration Log: scr_01647
Started: 2026-04-16T09:17:03.432348+00:00
Description: Screening scr_01647 ds=bci_iv2a_real_s1 graph=knn miss=2ch mode=noise

## Dataset: bci_iv2a_real_s1 | rows=42
  Graph: knn__k7 built OK
    mean | MR=0.2 | seed=0 | MAE=7.0461e-02 | t=0.0020s
    nearest | MR=0.2 | seed=0 | MAE=6.6301e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=0 | MAE=2.2640e-01 | t=0.0057s
    tv | MR=0.2 | seed=0 | MAE=7.0454e-02 | t=0.1701s
    trss | MR=0.2 | seed=0 | MAE=4.6421e-02 | t=0.0199s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=3.4390e-01 | t=0.0082s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=5.5263e-01 | t=2.6074s
    mean | MR=0.2 | seed=1 | MAE=6.9165e-02 | t=0.0020s
    nearest | MR=0.2 | seed=1 | MAE=6.3510e-02 | t=0.0042s
    tikhonov | MR=0.2 | seed=1 | MAE=2.2211e-01 | t=0.0057s
    tv | MR=0.2 | seed=1 | MAE=6.9158e-02 | t=0.1604s
    trss | MR=0.2 | seed=1 | MAE=4.7272e-02 | t=0.0200s

Completed: 2026-04-16T09:17:03.433055+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.