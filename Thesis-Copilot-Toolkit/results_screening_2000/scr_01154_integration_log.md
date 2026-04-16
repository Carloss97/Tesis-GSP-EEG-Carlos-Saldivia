# Integration Log: scr_01154
Started: 2026-04-16T14:35:10.634836+00:00
Description: Screening scr_01154 ds=physionet_real graph=knng miss=[0.1] mode=lambda

## Dataset: physionet_eegmmidb_real | rows=24
  Graph: knng built OK
    tv | MR=0.2 | seed=0 | MAE=5.0492e-06 | t=0.2644s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=6.3236e-06 | t=0.0154s
    trss | MR=0.2 | seed=0 | MAE=1.8066e-06 | t=0.2457s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.6182e-05 | t=27.1265s
    tv | MR=0.2 | seed=1 | MAE=5.0593e-06 | t=0.5625s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=6.2448e-06 | t=0.0131s
    trss | MR=0.2 | seed=1 | MAE=1.8476e-06 | t=0.1791s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.6313e-05 | t=21.4688s
    tv | MR=0.2 | seed=0 | MAE=5.1244e-06 | t=0.4596s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=7.7191e-06 | t=0.0122s
    trss | MR=0.2 | seed=0 | MAE=1.8935e-06 | t=0.2795s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.0082e-05 | t=20.7524s

Completed: 2026-04-16T14:35:10.635699+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.