# Integration Log: scr_01048
Started: 2026-04-16T13:07:07.565223+00:00
Description: Screening scr_01048 ds=bci_iv2a_real_s2 graph=knng miss=3ch mode=lambda

## Dataset: bci_iv2a_real_s2 | rows=24
  Graph: knng built OK
    tv | MR=0.2 | seed=0 | MAE=8.7658e-07 | t=0.3469s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=4.0229e-06 | t=0.0151s
    trss | MR=0.2 | seed=0 | MAE=4.4441e-07 | t=0.3270s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=6.3364e-06 | t=9.1123s
    tv | MR=0.2 | seed=1 | MAE=9.0520e-07 | t=0.4237s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=4.0643e-06 | t=0.0378s
    trss | MR=0.2 | seed=1 | MAE=4.4891e-07 | t=0.2638s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=6.3695e-06 | t=2.9592s
    tv | MR=0.2 | seed=0 | MAE=8.7648e-07 | t=0.1559s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=4.1860e-06 | t=0.0081s
    trss | MR=0.2 | seed=0 | MAE=4.7787e-07 | t=0.0196s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=8.5990e-06 | t=8.8142s

Completed: 2026-04-16T13:07:07.566168+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.