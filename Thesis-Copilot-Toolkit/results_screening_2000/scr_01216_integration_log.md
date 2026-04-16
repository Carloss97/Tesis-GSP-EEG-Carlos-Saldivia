# Integration Log: scr_01216
Started: 2026-04-16T08:21:05.828476+00:00
Description: Screening scr_01216 ds=bci_iv2a_real_s2 graph=knn miss=[0.2] mode=lambda

## Dataset: bci_iv2a_real_s2 | rows=24
  Graph: knn__k7 built OK
    tv | MR=0.2 | seed=0 | MAE=2.9533e-02 | t=0.1619s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.7123e-01 | t=0.0082s
    trss | MR=0.2 | seed=0 | MAE=1.2513e-02 | t=0.0195s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=3.3801e-01 | t=1.3581s
    tv | MR=0.2 | seed=1 | MAE=2.8800e-02 | t=0.1595s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=1.7034e-01 | t=0.0082s
    trss | MR=0.2 | seed=1 | MAE=1.2536e-02 | t=0.0190s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=3.3905e-01 | t=1.2432s
    tv | MR=0.2 | seed=0 | MAE=2.9530e-02 | t=0.1583s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.8168e-01 | t=0.0081s
    trss | MR=0.2 | seed=0 | MAE=1.3895e-02 | t=0.0188s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=4.4850e-01 | t=1.2974s

Completed: 2026-04-16T08:21:05.829420+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.