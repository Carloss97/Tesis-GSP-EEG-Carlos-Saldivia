# Integration Log: scr_01312
Started: 2026-04-16T08:33:02.966099+00:00
Description: Screening scr_01312 ds=bci_iv2a_real_s2 graph=knn miss=[0.3] mode=lambda

## Dataset: bci_iv2a_real_s2 | rows=24
  Graph: knn__k5 built OK
    tv | MR=0.2 | seed=0 | MAE=2.9533e-02 | t=0.1583s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.6743e-01 | t=0.0118s
    trss | MR=0.2 | seed=0 | MAE=1.2914e-02 | t=0.0195s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.8139e-01 | t=2.8117s
    tv | MR=0.2 | seed=1 | MAE=2.8800e-02 | t=0.1953s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=1.6657e-01 | t=0.0079s
    trss | MR=0.2 | seed=1 | MAE=1.2965e-02 | t=0.0189s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=2.8253e-01 | t=2.5911s
    tv | MR=0.2 | seed=0 | MAE=2.9530e-02 | t=0.1591s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.7568e-01 | t=0.0083s
    trss | MR=0.2 | seed=0 | MAE=1.4213e-02 | t=0.0191s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=3.8431e-01 | t=3.1840s

Completed: 2026-04-16T08:33:02.966794+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.