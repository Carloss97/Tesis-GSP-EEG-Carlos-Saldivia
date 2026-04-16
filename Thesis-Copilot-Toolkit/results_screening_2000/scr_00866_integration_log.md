# Integration Log: scr_00866
Started: 2026-04-16T12:06:48.742768+00:00
Description: Screening scr_00866 ds=physionet_real graph=knn miss=2ch mode=lambda

## Dataset: physionet_eegmmidb_real | rows=24
  Graph: knn__k3 built OK
    tv | MR=0.2 | seed=0 | MAE=4.8108e-06 | t=0.1579s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=5.7316e-06 | t=0.0085s
    trss | MR=0.2 | seed=0 | MAE=1.8541e-06 | t=0.0190s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.5037e-05 | t=2.5394s
    tv | MR=0.2 | seed=1 | MAE=4.8199e-06 | t=0.1475s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=5.6202e-06 | t=0.0078s
    trss | MR=0.2 | seed=1 | MAE=1.9364e-06 | t=0.0193s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.5141e-05 | t=2.5611s
    tv | MR=0.2 | seed=0 | MAE=4.9816e-06 | t=0.1469s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=6.7590e-06 | t=0.0078s
    trss | MR=0.2 | seed=0 | MAE=1.9097e-06 | t=0.0186s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.8316e-05 | t=2.3845s

Completed: 2026-04-16T12:06:48.743729+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.