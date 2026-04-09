# Integration Log: it113_movielens_graph_lambda_grid
Started: 2026-04-06T19:40:36.455379+00:00
Description: MovieLens graph-signal lambda grid

## Dataset: movielens_graph_signal | rows=160
  Graph: knn__k3 built OK
    tv | MR=0.2 | seed=0 | MAE=3.2195e-02 | t=0.2841s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=7.9212e-02 | t=0.0164s
    trss | MR=0.2 | seed=0 | MAE=5.7441e-02 | t=0.0354s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.1361e-01 | t=7.8363s
    tv | MR=0.2 | seed=1 | MAE=3.6501e-02 | t=0.2838s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=8.5982e-02 | t=0.0160s
    trss | MR=0.2 | seed=1 | MAE=6.3899e-02 | t=0.0346s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.1366e-01 | t=7.4081s
    tv | MR=0.2 | seed=2 | MAE=3.3204e-02 | t=0.2809s
    graph_time_tikhonov | MR=0.2 | seed=2 | MAE=7.9565e-02 | t=0.0159s
    trss | MR=0.2 | seed=2 | MAE=6.3886e-02 | t=0.0339s
    temporal_laplacian | MR=0.2 | seed=2 | MAE=1.1275e-01 | t=7.3718s

Completed: 2026-04-06T19:40:36.456850+00:00
Total rows: 160
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.