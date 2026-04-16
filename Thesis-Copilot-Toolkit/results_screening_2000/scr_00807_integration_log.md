# Integration Log: scr_00807
Started: 2026-04-16T11:59:17.261230+00:00
Description: Screening scr_00807 ds=bci_iv2a_real_s1 graph=gaussian miss=1ch mode=lambda

## Dataset: bci_iv2a_real_s1 | rows=24
  Graph: gaussian__sigma0.6 built OK
    tv | MR=0.2 | seed=0 | MAE=3.0357e-06 | t=0.2141s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=9.3255e-06 | t=0.0114s
    trss | MR=0.2 | seed=0 | MAE=7.0652e-07 | t=0.0191s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.3921e-05 | t=1.3636s
    tv | MR=0.2 | seed=1 | MAE=3.3734e-06 | t=0.1867s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=9.3856e-06 | t=0.0078s
    trss | MR=0.2 | seed=1 | MAE=8.2877e-07 | t=0.0192s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.3940e-05 | t=1.2558s
    tv | MR=0.2 | seed=0 | MAE=3.0357e-06 | t=0.1874s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.1082e-05 | t=0.0078s
    trss | MR=0.2 | seed=0 | MAE=9.6702e-07 | t=0.0186s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.6084e-05 | t=1.4597s

Completed: 2026-04-16T11:59:17.262077+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.