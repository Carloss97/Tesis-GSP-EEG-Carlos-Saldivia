# Integration Log: scr_00905
Started: 2026-04-16T12:15:33.860179+00:00
Description: Screening scr_00905 ds=bci_iv2a_real_s3 graph=gaussian miss=2ch mode=lambda

## Dataset: bci_iv2a_real_s3 | rows=24
  Graph: gaussian__sigma1.0 built OK
    tv | MR=0.2 | seed=0 | MAE=7.3135e-07 | t=0.3547s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.3141e-06 | t=0.0244s
    trss | MR=0.2 | seed=0 | MAE=3.1566e-07 | t=0.0521s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=4.4873e-06 | t=2.1459s
    tv | MR=0.2 | seed=1 | MAE=7.3458e-07 | t=0.1972s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=2.3107e-06 | t=0.0083s
    trss | MR=0.2 | seed=1 | MAE=3.3033e-07 | t=0.0194s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=4.4910e-06 | t=7.9785s
    tv | MR=0.2 | seed=0 | MAE=7.3135e-07 | t=0.1905s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.7103e-06 | t=0.0079s
    trss | MR=0.2 | seed=0 | MAE=3.4559e-07 | t=0.0190s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=5.3716e-06 | t=10.3209s

Completed: 2026-04-16T12:15:33.861049+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.