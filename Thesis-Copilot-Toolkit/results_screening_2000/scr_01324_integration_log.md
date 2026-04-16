# Integration Log: scr_01324
Started: 2026-04-16T08:34:32.380343+00:00
Description: Screening scr_01324 ds=bci_iv2a_real_s2 graph=knn miss=[0.3] mode=lambda

## Dataset: bci_iv2a_real_s2 | rows=24
  Graph: knn__k7 built OK
    tv | MR=0.2 | seed=0 | MAE=2.9533e-02 | t=0.1912s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.7123e-01 | t=0.0080s
    trss | MR=0.2 | seed=0 | MAE=1.2513e-02 | t=0.0194s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=3.3801e-01 | t=2.5760s
    tv | MR=0.2 | seed=1 | MAE=2.8800e-02 | t=0.1872s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=1.7034e-01 | t=0.0081s
    trss | MR=0.2 | seed=1 | MAE=1.2536e-02 | t=0.0204s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=3.3905e-01 | t=2.4048s
    tv | MR=0.2 | seed=0 | MAE=2.9530e-02 | t=0.1600s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.8168e-01 | t=0.0079s
    trss | MR=0.2 | seed=0 | MAE=1.3895e-02 | t=0.0188s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=4.4850e-01 | t=1.2429s

Completed: 2026-04-16T08:34:32.381232+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.