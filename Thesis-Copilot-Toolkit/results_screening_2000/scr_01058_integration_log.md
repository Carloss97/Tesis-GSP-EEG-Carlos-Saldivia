# Integration Log: scr_01058
Started: 2026-04-16T13:10:16.595039+00:00
Description: Screening scr_01058 ds=physionet_real graph=vknng miss=3ch mode=lambda

## Dataset: physionet_eegmmidb_real | rows=24
  Graph: vknng built OK
    tv | MR=0.2 | seed=0 | MAE=5.0288e-06 | t=0.1508s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=6.3213e-06 | t=0.0123s
    trss | MR=0.2 | seed=0 | MAE=1.8586e-06 | t=0.4256s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.6126e-05 | t=8.8657s
    tv | MR=0.2 | seed=1 | MAE=5.0386e-06 | t=0.1436s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=6.2312e-06 | t=0.0119s
    trss | MR=0.2 | seed=1 | MAE=1.9118e-06 | t=0.0203s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.6255e-05 | t=7.4649s
    tv | MR=0.2 | seed=0 | MAE=5.1131e-06 | t=0.3416s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=7.6899e-06 | t=0.0124s
    trss | MR=0.2 | seed=0 | MAE=1.9460e-06 | t=0.1153s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.9923e-05 | t=3.9932s

Completed: 2026-04-16T13:10:16.596293+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.