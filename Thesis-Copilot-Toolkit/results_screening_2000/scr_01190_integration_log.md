# Integration Log: scr_01190
Started: 2026-04-16T15:22:14.298592+00:00
Description: Screening scr_01190 ds=physionet_real graph=knn miss=[0.2] mode=lambda

## Dataset: physionet_eegmmidb_real | rows=24
  Graph: knn__k3 built OK
    tv | MR=0.2 | seed=0 | MAE=4.8108e-06 | t=0.7039s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=5.7316e-06 | t=0.0127s
    trss | MR=0.2 | seed=0 | MAE=1.8541e-06 | t=0.2020s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.5037e-05 | t=27.1567s
    tv | MR=0.2 | seed=1 | MAE=4.8199e-06 | t=0.7485s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=5.6202e-06 | t=0.0125s
    trss | MR=0.2 | seed=1 | MAE=1.9364e-06 | t=0.2516s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.5141e-05 | t=23.4888s
    tv | MR=0.2 | seed=0 | MAE=4.9816e-06 | t=0.6782s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=6.7590e-06 | t=0.0279s
    trss | MR=0.2 | seed=0 | MAE=1.9097e-06 | t=0.6189s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.8316e-05 | t=26.8103s

Completed: 2026-04-16T15:22:14.299374+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.