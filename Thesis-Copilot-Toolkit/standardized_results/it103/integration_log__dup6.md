# Integration Log: it103_tv_lambda_grid_search
Started: 2026-04-09T15:30:04.316014+00:00
Description: Lambda grid search for TV family methods

## Dataset: physionet_eegmmidb_real | rows=80
  Graph: knn__k3 built OK
    tv | MR=0.2 | seed=0 | MAE=3.8677e-06 | t=0.4250s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=6.6581e-06 | t=0.0169s
    trss | MR=0.2 | seed=0 | MAE=1.4248e-06 | t=0.0978s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.3704e-05 | t=6.2986s
    tv | MR=0.2 | seed=1 | MAE=3.8094e-06 | t=0.3425s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=6.5917e-06 | t=0.0132s
    trss | MR=0.2 | seed=1 | MAE=1.3915e-06 | t=0.0192s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.3716e-05 | t=6.5134s
    tv | MR=0.2 | seed=2 | MAE=3.8070e-06 | t=0.3311s
    graph_time_tikhonov | MR=0.2 | seed=2 | MAE=6.5863e-06 | t=0.0089s
    trss | MR=0.2 | seed=2 | MAE=1.3252e-06 | t=0.0163s
    temporal_laplacian | MR=0.2 | seed=2 | MAE=1.3672e-05 | t=7.9282s

Completed: 2026-04-09T15:30:04.317276+00:00
Total rows: 80
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.