# Integration Log: scr_01082
Started: 2026-04-16T13:28:04.590558+00:00
Description: Screening scr_01082 ds=physionet_real graph=knn miss=[0.1] mode=lambda

## Dataset: physionet_eegmmidb_real | rows=24
  Graph: knn__k3 built OK
    tv | MR=0.2 | seed=0 | MAE=4.8108e-06 | t=0.1489s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=5.7316e-06 | t=0.0121s
    trss | MR=0.2 | seed=0 | MAE=1.8541e-06 | t=0.2590s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.5037e-05 | t=14.9474s
    tv | MR=0.2 | seed=1 | MAE=4.8199e-06 | t=0.3385s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=5.6202e-06 | t=0.0128s
    trss | MR=0.2 | seed=1 | MAE=1.9364e-06 | t=0.0190s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.5141e-05 | t=13.2690s
    tv | MR=0.2 | seed=0 | MAE=4.9816e-06 | t=0.7089s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=6.7590e-06 | t=0.0123s
    trss | MR=0.2 | seed=0 | MAE=1.9097e-06 | t=0.5266s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.8316e-05 | t=14.7753s

Completed: 2026-04-16T13:28:04.591293+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.