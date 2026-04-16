# Integration Log: scr_01023
Started: 2026-04-16T12:57:23.994255+00:00
Description: Screening scr_01023 ds=bci_iv2a_real_s1 graph=gaussian miss=3ch mode=lambda

## Dataset: bci_iv2a_real_s1 | rows=24
  Graph: gaussian__sigma0.6 built OK
    tv | MR=0.2 | seed=0 | MAE=3.0357e-06 | t=0.4073s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=9.3255e-06 | t=0.0186s
    trss | MR=0.2 | seed=0 | MAE=7.0652e-07 | t=0.2217s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.3921e-05 | t=9.7283s
    tv | MR=0.2 | seed=1 | MAE=3.3734e-06 | t=0.4693s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=9.3856e-06 | t=0.0574s
    trss | MR=0.2 | seed=1 | MAE=8.2877e-07 | t=0.2325s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.3940e-05 | t=3.4902s
    tv | MR=0.2 | seed=0 | MAE=3.0357e-06 | t=0.1912s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.1082e-05 | t=0.0080s
    trss | MR=0.2 | seed=0 | MAE=9.6702e-07 | t=0.0210s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.6084e-05 | t=9.2273s

Completed: 2026-04-16T12:57:23.995143+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.