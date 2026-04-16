# Integration Log: scr_00988
Started: 2026-04-16T12:45:13.748394+00:00
Description: Screening scr_00988 ds=bci_iv2a_real_s2 graph=knn miss=3ch mode=lambda

## Dataset: bci_iv2a_real_s2 | rows=24
  Graph: knn__k5 built OK
    tv | MR=0.2 | seed=0 | MAE=8.7659e-07 | t=0.1548s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=4.0635e-06 | t=0.0080s
    trss | MR=0.2 | seed=0 | MAE=4.2026e-07 | t=0.0196s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=7.0377e-06 | t=2.9412s
    tv | MR=0.2 | seed=1 | MAE=9.0517e-07 | t=0.1753s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=4.1013e-06 | t=0.0090s
    trss | MR=0.2 | seed=1 | MAE=4.2224e-07 | t=0.0202s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=7.0696e-06 | t=9.3826s
    tv | MR=0.2 | seed=0 | MAE=8.7649e-07 | t=0.3450s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=4.2613e-06 | t=0.0125s
    trss | MR=0.2 | seed=0 | MAE=4.5962e-07 | t=0.3559s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=9.4732e-06 | t=8.3647s

Completed: 2026-04-16T12:45:13.749257+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.