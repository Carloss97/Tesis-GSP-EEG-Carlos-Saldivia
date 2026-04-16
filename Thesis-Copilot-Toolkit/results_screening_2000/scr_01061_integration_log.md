# Integration Log: scr_01061
Started: 2026-04-16T13:13:18.247122+00:00
Description: Screening scr_01061 ds=bci_iv2a_real_s3 graph=vknng miss=3ch mode=lambda

## Dataset: bci_iv2a_real_s3 | rows=24
  Graph: vknng built OK
    tv | MR=0.2 | seed=0 | MAE=7.3152e-07 | t=0.1505s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.4681e-06 | t=0.0123s
    trss | MR=0.2 | seed=0 | MAE=4.6083e-07 | t=0.1997s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.0451e-06 | t=17.9008s
    tv | MR=0.2 | seed=1 | MAE=7.3472e-07 | t=0.5424s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=1.4620e-06 | t=0.0560s
    trss | MR=0.2 | seed=1 | MAE=4.6733e-07 | t=0.6243s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=2.0631e-06 | t=9.5696s
    tv | MR=0.2 | seed=0 | MAE=7.3144e-07 | t=0.3023s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.6018e-06 | t=0.0124s
    trss | MR=0.2 | seed=0 | MAE=4.7805e-07 | t=0.0745s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.5318e-06 | t=6.7945s

Completed: 2026-04-16T13:13:18.248281+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.