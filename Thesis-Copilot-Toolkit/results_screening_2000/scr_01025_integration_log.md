# Integration Log: scr_01025
Started: 2026-04-16T12:58:49.761773+00:00
Description: Screening scr_01025 ds=bci_iv2a_real_s3 graph=gaussian miss=3ch mode=lambda

## Dataset: bci_iv2a_real_s3 | rows=24
  Graph: gaussian__sigma0.6 built OK
    tv | MR=0.2 | seed=0 | MAE=7.3135e-07 | t=0.3479s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.3141e-06 | t=0.0157s
    trss | MR=0.2 | seed=0 | MAE=3.1566e-07 | t=0.1991s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=4.4873e-06 | t=2.1329s
    tv | MR=0.2 | seed=1 | MAE=7.3458e-07 | t=0.2034s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=2.3107e-06 | t=0.0084s
    trss | MR=0.2 | seed=1 | MAE=3.3033e-07 | t=0.0200s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=4.4910e-06 | t=4.6571s
    tv | MR=0.2 | seed=0 | MAE=7.3135e-07 | t=0.5652s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.7103e-06 | t=0.0127s
    trss | MR=0.2 | seed=0 | MAE=3.4559e-07 | t=0.0206s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=5.3716e-06 | t=6.5288s

Completed: 2026-04-16T12:58:49.762643+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.