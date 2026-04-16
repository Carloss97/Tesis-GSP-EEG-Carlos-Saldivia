# Integration Log: scr_00772
Started: 2026-04-16T11:54:52.140296+00:00
Description: Screening scr_00772 ds=bci_iv2a_real_s2 graph=knn miss=1ch mode=lambda

## Dataset: bci_iv2a_real_s2 | rows=24
  Graph: knn__k5 built OK
    tv | MR=0.2 | seed=0 | MAE=8.7659e-07 | t=0.1545s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=4.0635e-06 | t=0.0079s
    trss | MR=0.2 | seed=0 | MAE=4.2026e-07 | t=0.0188s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=7.0377e-06 | t=1.3846s
    tv | MR=0.2 | seed=1 | MAE=9.0517e-07 | t=0.1548s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=4.1013e-06 | t=0.0079s
    trss | MR=0.2 | seed=1 | MAE=4.2224e-07 | t=0.0186s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=7.0696e-06 | t=1.2908s
    tv | MR=0.2 | seed=0 | MAE=8.7649e-07 | t=0.1589s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=4.2613e-06 | t=0.0079s
    trss | MR=0.2 | seed=0 | MAE=4.5962e-07 | t=0.0185s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=9.4732e-06 | t=1.3854s

Completed: 2026-04-16T11:54:52.140990+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.