# Integration Log: scr_00915
Started: 2026-04-16T12:18:26.907819+00:00
Description: Screening scr_00915 ds=bci_iv2a_real_s1 graph=gaussian miss=2ch mode=lambda

## Dataset: bci_iv2a_real_s1 | rows=24
  Graph: gaussian__sigma0.6 built OK
    tv | MR=0.2 | seed=0 | MAE=3.0357e-06 | t=0.2041s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=9.3255e-06 | t=0.0078s
    trss | MR=0.2 | seed=0 | MAE=7.0652e-07 | t=0.0189s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.3921e-05 | t=4.7787s
    tv | MR=0.2 | seed=1 | MAE=3.3734e-06 | t=0.3070s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=9.3856e-06 | t=0.0103s
    trss | MR=0.2 | seed=1 | MAE=8.2877e-07 | t=0.0185s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.3940e-05 | t=2.9608s
    tv | MR=0.2 | seed=0 | MAE=3.0357e-06 | t=0.3435s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.1082e-05 | t=0.0132s
    trss | MR=0.2 | seed=0 | MAE=9.6702e-07 | t=0.0995s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.6084e-05 | t=2.5242s

Completed: 2026-04-16T12:18:26.908819+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.