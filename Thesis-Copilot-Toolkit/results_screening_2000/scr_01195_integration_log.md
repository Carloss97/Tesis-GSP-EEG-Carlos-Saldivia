# Integration Log: scr_01195
Started: 2026-04-16T15:33:25.172338+00:00
Description: Screening scr_01195 ds=iris_graph_signal graph=knn miss=[0.2] mode=lambda

## Dataset: iris_graph_signal | rows=24
  Graph: knn__k3 built OK
    tv | MR=0.2 | seed=0 | MAE=1.2457e-01 | t=0.0935s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.3662e-01 | t=0.0043s
    trss | MR=0.2 | seed=0 | MAE=8.1681e-02 | t=0.0046s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=3.8836e-01 | t=1.7036s
    tv | MR=0.2 | seed=1 | MAE=1.3875e-01 | t=0.1291s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=2.4081e-01 | t=0.0044s
    trss | MR=0.2 | seed=1 | MAE=8.7147e-02 | t=0.0050s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=3.8955e-01 | t=7.6641s
    tv | MR=0.2 | seed=0 | MAE=1.2600e-01 | t=0.2731s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.8011e-01 | t=0.0055s
    trss | MR=0.2 | seed=0 | MAE=8.3264e-02 | t=0.0050s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=4.3334e-01 | t=13.0091s

Completed: 2026-04-16T15:33:25.173297+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.