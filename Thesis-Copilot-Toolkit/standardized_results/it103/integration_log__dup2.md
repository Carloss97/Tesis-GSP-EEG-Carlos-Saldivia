# Integration Log: it103_tv_lambda_grid_search
Started: 2026-04-09T07:21:31.999124+00:00
Description: Lambda grid search for TV family methods

## Dataset: physionet_eegmmidb_real | rows=80
  Graph: knn__k3 built OK
    tv | MR=0.2 | seed=0 | MAE=3.8677e-06 | t=0.1403s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=6.6581e-06 | t=0.0078s
    trss | MR=0.2 | seed=0 | MAE=1.4248e-06 | t=0.0166s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.3704e-05 | t=7.9965s
    tv | MR=0.2 | seed=1 | MAE=3.8094e-06 | t=0.1474s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=6.5917e-06 | t=0.0148s
    trss | MR=0.2 | seed=1 | MAE=1.3915e-06 | t=0.2763s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.3716e-05 | t=5.8338s
    tv | MR=0.2 | seed=2 | MAE=3.8070e-06 | t=0.1421s
    graph_time_tikhonov | MR=0.2 | seed=2 | MAE=6.5863e-06 | t=0.0077s
    trss | MR=0.2 | seed=2 | MAE=1.3252e-06 | t=0.0162s
    temporal_laplacian | MR=0.2 | seed=2 | MAE=1.3672e-05 | t=2.0564s

Completed: 2026-04-09T07:21:31.999887+00:00
Total rows: 80
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.