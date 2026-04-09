# Integration Log: it103_tv_lambda_grid_search
Started: 2026-04-09T07:08:17.004423+00:00
Description: Lambda grid search for TV family methods

## Dataset: physionet_eegmmidb_real | rows=80
  Graph: knn__k3 built OK
    tv | MR=0.2 | seed=0 | MAE=3.8677e-06 | t=0.3210s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=6.6581e-06 | t=0.0120s
    trss | MR=0.2 | seed=0 | MAE=1.4248e-06 | t=0.1639s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.3704e-05 | t=12.3257s
    tv | MR=0.2 | seed=1 | MAE=3.8094e-06 | t=0.4439s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=6.5917e-06 | t=0.0321s
    trss | MR=0.2 | seed=1 | MAE=1.3915e-06 | t=0.4634s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.3716e-05 | t=17.9757s
    tv | MR=0.2 | seed=2 | MAE=3.8070e-06 | t=0.5177s
    graph_time_tikhonov | MR=0.2 | seed=2 | MAE=6.5863e-06 | t=0.0120s
    trss | MR=0.2 | seed=2 | MAE=1.3252e-06 | t=0.4481s
    temporal_laplacian | MR=0.2 | seed=2 | MAE=1.3672e-05 | t=18.9829s

Completed: 2026-04-09T07:08:17.005729+00:00
Total rows: 80
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.