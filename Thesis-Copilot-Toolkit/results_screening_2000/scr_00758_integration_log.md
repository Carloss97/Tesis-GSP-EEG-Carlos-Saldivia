# Integration Log: scr_00758
Started: 2026-04-16T11:52:54.709019+00:00
Description: Screening scr_00758 ds=physionet_real graph=knn miss=1ch mode=lambda

## Dataset: physionet_eegmmidb_real | rows=24
  Graph: knn__k3 built OK
    tv | MR=0.2 | seed=0 | MAE=4.8108e-06 | t=0.1500s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=5.7316e-06 | t=0.0114s
    trss | MR=0.2 | seed=0 | MAE=1.8541e-06 | t=0.0190s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.5037e-05 | t=2.7429s
    tv | MR=0.2 | seed=1 | MAE=4.8199e-06 | t=0.1501s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=5.6202e-06 | t=0.0083s
    trss | MR=0.2 | seed=1 | MAE=1.9364e-06 | t=0.0199s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.5141e-05 | t=2.6020s
    tv | MR=0.2 | seed=0 | MAE=4.9816e-06 | t=0.1428s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=6.7590e-06 | t=0.0085s
    trss | MR=0.2 | seed=0 | MAE=1.9097e-06 | t=0.0190s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.8316e-05 | t=2.7368s

Completed: 2026-04-16T11:52:54.709848+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.