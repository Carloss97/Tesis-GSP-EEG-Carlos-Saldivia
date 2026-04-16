# Integration Log: scr_01121
Started: 2026-04-16T14:02:21.602612+00:00
Description: Screening scr_01121 ds=bci_iv2a_real_s3 graph=gaussian miss=[0.1] mode=lambda

## Dataset: bci_iv2a_real_s3 | rows=24
  Graph: gaussian__sigma1.0 built OK
    tv | MR=0.2 | seed=0 | MAE=7.3135e-07 | t=0.7507s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.3141e-06 | t=0.0132s
    trss | MR=0.2 | seed=0 | MAE=3.1566e-07 | t=0.0479s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=4.4873e-06 | t=16.8350s
    tv | MR=0.2 | seed=1 | MAE=7.3458e-07 | t=0.2211s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=2.3107e-06 | t=0.0096s
    trss | MR=0.2 | seed=1 | MAE=3.3033e-07 | t=0.0202s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=4.4910e-06 | t=12.3081s
    tv | MR=0.2 | seed=0 | MAE=7.3135e-07 | t=0.4886s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.7103e-06 | t=0.0510s
    trss | MR=0.2 | seed=0 | MAE=3.4559e-07 | t=0.2826s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=5.3716e-06 | t=15.3986s

Completed: 2026-04-16T14:02:21.603757+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.