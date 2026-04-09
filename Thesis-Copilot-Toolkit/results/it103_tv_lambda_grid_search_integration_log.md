# Integration Log: it103_tv_lambda_grid_search
Started: 2026-04-09T17:47:52.531063+00:00
Description: Lambda grid search for TV family methods

## Dataset: physionet_eegmmidb_real | rows=80
  Graph: knn__k3 built OK
    tv | MR=0.2 | seed=0 | MAE=3.8677e-06 | t=0.1424s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=6.6581e-06 | t=0.0079s
    trss | MR=0.2 | seed=0 | MAE=1.4248e-06 | t=0.0174s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.3704e-05 | t=1.3020s
    tv | MR=0.2 | seed=1 | MAE=3.8094e-06 | t=0.1459s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=6.5917e-06 | t=0.0079s
    trss | MR=0.2 | seed=1 | MAE=1.3915e-06 | t=0.0172s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.3716e-05 | t=1.3405s
    tv | MR=0.2 | seed=2 | MAE=3.8070e-06 | t=0.1428s
    graph_time_tikhonov | MR=0.2 | seed=2 | MAE=6.5863e-06 | t=0.0079s
    trss | MR=0.2 | seed=2 | MAE=1.3252e-06 | t=0.0163s
    temporal_laplacian | MR=0.2 | seed=2 | MAE=1.3672e-05 | t=1.4227s

Completed: 2026-04-09T17:47:52.531965+00:00
Total rows: 80
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.