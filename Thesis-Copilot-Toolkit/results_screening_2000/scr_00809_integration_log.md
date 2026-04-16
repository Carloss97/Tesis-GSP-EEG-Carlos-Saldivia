# Integration Log: scr_00809
Started: 2026-04-16T11:59:49.222503+00:00
Description: Screening scr_00809 ds=bci_iv2a_real_s3 graph=gaussian miss=1ch mode=lambda

## Dataset: bci_iv2a_real_s3 | rows=24
  Graph: gaussian__sigma0.6 built OK
    tv | MR=0.2 | seed=0 | MAE=7.3135e-07 | t=0.1917s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.3141e-06 | t=0.0086s
    trss | MR=0.2 | seed=0 | MAE=3.1566e-07 | t=0.0187s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=4.4873e-06 | t=2.5836s
    tv | MR=0.2 | seed=1 | MAE=7.3458e-07 | t=0.1861s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=2.3107e-06 | t=0.0089s
    trss | MR=0.2 | seed=1 | MAE=3.3033e-07 | t=0.0195s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=4.4910e-06 | t=2.6260s
    tv | MR=0.2 | seed=0 | MAE=7.3135e-07 | t=0.1998s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.7103e-06 | t=0.0081s
    trss | MR=0.2 | seed=0 | MAE=3.4559e-07 | t=0.0194s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=5.3716e-06 | t=2.5194s

Completed: 2026-04-16T11:59:49.223203+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.