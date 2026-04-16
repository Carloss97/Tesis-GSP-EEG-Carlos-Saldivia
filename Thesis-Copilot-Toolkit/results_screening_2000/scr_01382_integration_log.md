# Integration Log: scr_01382
Started: 2026-04-16T08:41:33.456743+00:00
Description: Screening scr_01382 ds=physionet_real graph=vknng miss=[0.3] mode=lambda

## Dataset: physionet_eegmmidb_real | rows=24
  Graph: vknng built OK
    tv | MR=0.2 | seed=0 | MAE=7.5305e-02 | t=0.1482s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.1101e-01 | t=0.0081s
    trss | MR=0.2 | seed=0 | MAE=2.9797e-02 | t=0.0198s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.9476e-01 | t=1.2676s
    tv | MR=0.2 | seed=1 | MAE=7.4589e-02 | t=0.1437s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=1.1058e-01 | t=0.0080s
    trss | MR=0.2 | seed=1 | MAE=2.8827e-02 | t=0.0205s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=2.9559e-01 | t=1.2637s
    tv | MR=0.2 | seed=0 | MAE=7.6592e-02 | t=0.1426s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.3766e-01 | t=0.0080s
    trss | MR=0.2 | seed=0 | MAE=3.0508e-02 | t=0.0200s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=3.6800e-01 | t=2.1824s

Completed: 2026-04-16T08:41:33.457698+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.