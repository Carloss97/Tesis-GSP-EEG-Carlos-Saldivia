# Integration Log: scr_01156
Started: 2026-04-16T14:39:41.891101+00:00
Description: Screening scr_01156 ds=bci_iv2a_real_s2 graph=knng miss=[0.1] mode=lambda

## Dataset: bci_iv2a_real_s2 | rows=24
  Graph: knng built OK
    tv | MR=0.2 | seed=0 | MAE=8.7658e-07 | t=0.4698s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=4.0229e-06 | t=0.0127s
    trss | MR=0.2 | seed=0 | MAE=4.4441e-07 | t=0.3043s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=6.3364e-06 | t=15.1306s
    tv | MR=0.2 | seed=1 | MAE=9.0520e-07 | t=0.8670s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=4.0643e-06 | t=0.0123s
    trss | MR=0.2 | seed=1 | MAE=4.4891e-07 | t=1.0130s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=6.3695e-06 | t=25.1327s
    tv | MR=0.2 | seed=0 | MAE=8.7648e-07 | t=0.6268s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=4.1860e-06 | t=0.0128s
    trss | MR=0.2 | seed=0 | MAE=4.7787e-07 | t=0.3749s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=8.5990e-06 | t=12.5004s

Completed: 2026-04-16T14:39:41.892603+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.