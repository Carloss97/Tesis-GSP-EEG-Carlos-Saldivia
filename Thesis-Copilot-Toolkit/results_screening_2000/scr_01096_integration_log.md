# Integration Log: scr_01096
Started: 2026-04-16T13:40:23.942198+00:00
Description: Screening scr_01096 ds=bci_iv2a_real_s2 graph=knn miss=[0.1] mode=lambda

## Dataset: bci_iv2a_real_s2 | rows=24
  Graph: knn__k5 built OK
    tv | MR=0.2 | seed=0 | MAE=8.7659e-07 | t=0.1801s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=4.0635e-06 | t=0.0079s
    trss | MR=0.2 | seed=0 | MAE=4.2026e-07 | t=0.2353s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=7.0377e-06 | t=13.6843s
    tv | MR=0.2 | seed=1 | MAE=9.0517e-07 | t=0.7544s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=4.1013e-06 | t=0.0448s
    trss | MR=0.2 | seed=1 | MAE=4.2224e-07 | t=0.6414s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=7.0696e-06 | t=18.4166s
    tv | MR=0.2 | seed=0 | MAE=8.7649e-07 | t=0.4403s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=4.2613e-06 | t=0.0085s
    trss | MR=0.2 | seed=0 | MAE=4.5962e-07 | t=0.0207s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=9.4732e-06 | t=7.3140s

Completed: 2026-04-16T13:40:23.943040+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.