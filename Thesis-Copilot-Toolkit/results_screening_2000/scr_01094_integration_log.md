# Integration Log: scr_01094
Started: 2026-04-16T13:37:18.794786+00:00
Description: Screening scr_01094 ds=physionet_real graph=knn miss=[0.1] mode=lambda

## Dataset: physionet_eegmmidb_real | rows=24
  Graph: knn__k5 built OK
    tv | MR=0.2 | seed=0 | MAE=5.1032e-06 | t=0.2077s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=6.6501e-06 | t=0.0080s
    trss | MR=0.2 | seed=0 | MAE=1.7786e-06 | t=0.0200s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.7023e-05 | t=16.6781s
    tv | MR=0.2 | seed=1 | MAE=5.1120e-06 | t=0.1807s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=6.5763e-06 | t=0.0087s
    trss | MR=0.2 | seed=1 | MAE=1.8204e-06 | t=0.0200s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.7171e-05 | t=8.2560s
    tv | MR=0.2 | seed=0 | MAE=5.1533e-06 | t=0.5340s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=8.2347e-06 | t=0.0442s
    trss | MR=0.2 | seed=0 | MAE=1.8814e-06 | t=0.4986s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.1365e-05 | t=6.9981s

Completed: 2026-04-16T13:37:18.795694+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.