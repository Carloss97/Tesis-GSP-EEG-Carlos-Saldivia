# Integration Log: scr_01166
Started: 2026-04-16T14:49:59.515282+00:00
Description: Screening scr_01166 ds=physionet_real graph=vknng miss=[0.1] mode=lambda

## Dataset: physionet_eegmmidb_real | rows=24
  Graph: vknng built OK
    tv | MR=0.2 | seed=0 | MAE=5.0288e-06 | t=0.4779s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=6.3213e-06 | t=0.0381s
    trss | MR=0.2 | seed=0 | MAE=1.8586e-06 | t=0.5888s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.6126e-05 | t=25.4119s
    tv | MR=0.2 | seed=1 | MAE=5.0386e-06 | t=0.7851s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=6.2312e-06 | t=0.0125s
    trss | MR=0.2 | seed=1 | MAE=1.9118e-06 | t=0.4841s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.6255e-05 | t=10.2929s
    tv | MR=0.2 | seed=0 | MAE=5.1131e-06 | t=0.4333s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=7.6899e-06 | t=0.0243s
    trss | MR=0.2 | seed=0 | MAE=1.9460e-06 | t=0.3307s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.9923e-05 | t=25.2456s

Completed: 2026-04-16T14:49:59.516206+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.