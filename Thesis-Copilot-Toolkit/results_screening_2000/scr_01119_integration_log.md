# Integration Log: scr_01119
Started: 2026-04-16T13:59:05.442883+00:00
Description: Screening scr_01119 ds=bci_iv2a_real_s1 graph=gaussian miss=[0.1] mode=lambda

## Dataset: bci_iv2a_real_s1 | rows=24
  Graph: gaussian__sigma1.0 built OK
    tv | MR=0.2 | seed=0 | MAE=3.0357e-06 | t=0.7859s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=9.3255e-06 | t=0.0126s
    trss | MR=0.2 | seed=0 | MAE=7.0652e-07 | t=0.3869s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.3921e-05 | t=11.6634s
    tv | MR=0.2 | seed=1 | MAE=3.3734e-06 | t=0.1938s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=9.3856e-06 | t=0.0093s
    trss | MR=0.2 | seed=1 | MAE=8.2877e-07 | t=0.0216s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.3940e-05 | t=3.1936s
    tv | MR=0.2 | seed=0 | MAE=3.0357e-06 | t=0.5086s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.1082e-05 | t=0.0130s
    trss | MR=0.2 | seed=0 | MAE=9.6702e-07 | t=0.0881s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.6084e-05 | t=20.7713s

Completed: 2026-04-16T13:59:05.443608+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.