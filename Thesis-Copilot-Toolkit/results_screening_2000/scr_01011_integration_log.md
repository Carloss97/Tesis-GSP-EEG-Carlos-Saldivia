# Integration Log: scr_01011
Started: 2026-04-16T12:53:17.312894+00:00
Description: Screening scr_01011 ds=bci_iv2a_real_s1 graph=gaussian miss=3ch mode=lambda

## Dataset: bci_iv2a_real_s1 | rows=24
  Graph: gaussian__sigma1.0 built OK
    tv | MR=0.2 | seed=0 | MAE=3.0357e-06 | t=0.1938s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=9.3255e-06 | t=0.0079s
    trss | MR=0.2 | seed=0 | MAE=7.0652e-07 | t=0.0193s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.3921e-05 | t=2.1351s
    tv | MR=0.2 | seed=1 | MAE=3.3734e-06 | t=0.2074s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=9.3856e-06 | t=0.0122s
    trss | MR=0.2 | seed=1 | MAE=8.2877e-07 | t=0.1362s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.3940e-05 | t=9.0082s
    tv | MR=0.2 | seed=0 | MAE=3.0357e-06 | t=0.2036s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.1082e-05 | t=0.0097s
    trss | MR=0.2 | seed=0 | MAE=9.6702e-07 | t=0.0202s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.6084e-05 | t=10.4228s

Completed: 2026-04-16T12:53:17.314201+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.