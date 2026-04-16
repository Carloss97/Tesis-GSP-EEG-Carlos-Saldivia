# Integration Log: scr_01087
Started: 2026-04-16T13:34:32.958750+00:00
Description: Screening scr_01087 ds=iris_graph_signal graph=knn miss=[0.1] mode=lambda

## Dataset: iris_graph_signal | rows=24
  Graph: knn__k3 built OK
    tv | MR=0.2 | seed=0 | MAE=1.2457e-01 | t=0.2110s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.3662e-01 | t=0.0041s
    trss | MR=0.2 | seed=0 | MAE=8.1681e-02 | t=0.0195s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=3.8836e-01 | t=12.7278s
    tv | MR=0.2 | seed=1 | MAE=1.3875e-01 | t=0.0663s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=2.4081e-01 | t=0.0036s
    trss | MR=0.2 | seed=1 | MAE=8.7147e-02 | t=0.0027s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=3.8955e-01 | t=0.8805s
    tv | MR=0.2 | seed=0 | MAE=1.2600e-01 | t=0.0546s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.8011e-01 | t=0.0026s
    trss | MR=0.2 | seed=0 | MAE=8.3264e-02 | t=0.0026s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=4.3334e-01 | t=0.7372s

Completed: 2026-04-16T13:34:32.959631+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.