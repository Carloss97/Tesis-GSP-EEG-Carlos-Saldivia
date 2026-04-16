# Integration Log: scr_00903
Started: 2026-04-16T12:13:58.333329+00:00
Description: Screening scr_00903 ds=bci_iv2a_real_s1 graph=gaussian miss=2ch mode=lambda

## Dataset: bci_iv2a_real_s1 | rows=24
  Graph: gaussian__sigma1.0 built OK
    tv | MR=0.2 | seed=0 | MAE=3.0357e-06 | t=0.1866s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=9.3255e-06 | t=0.0082s
    trss | MR=0.2 | seed=0 | MAE=7.0652e-07 | t=0.0187s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.3921e-05 | t=4.9106s
    tv | MR=0.2 | seed=1 | MAE=3.3734e-06 | t=0.3686s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=9.3856e-06 | t=0.0085s
    trss | MR=0.2 | seed=1 | MAE=8.2877e-07 | t=0.0188s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.3940e-05 | t=2.1786s
    tv | MR=0.2 | seed=0 | MAE=3.0357e-06 | t=0.1896s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.1082e-05 | t=0.0081s
    trss | MR=0.2 | seed=0 | MAE=9.6702e-07 | t=0.0194s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.6084e-05 | t=11.9680s

Completed: 2026-04-16T12:13:58.334047+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.