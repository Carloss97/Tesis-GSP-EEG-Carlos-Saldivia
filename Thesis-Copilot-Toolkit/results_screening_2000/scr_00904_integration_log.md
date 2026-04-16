# Integration Log: scr_00904
Started: 2026-04-16T12:14:45.334786+00:00
Description: Screening scr_00904 ds=bci_iv2a_real_s2 graph=gaussian miss=2ch mode=lambda

## Dataset: bci_iv2a_real_s2 | rows=24
  Graph: gaussian__sigma1.0 built OK
    tv | MR=0.2 | seed=0 | MAE=8.7638e-07 | t=0.3704s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=4.5387e-06 | t=0.0134s
    trss | MR=0.2 | seed=0 | MAE=3.6928e-07 | t=0.0189s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.1729e-05 | t=5.3382s
    tv | MR=0.2 | seed=1 | MAE=9.0508e-07 | t=0.3454s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=4.5777e-06 | t=0.0141s
    trss | MR=0.2 | seed=1 | MAE=3.8400e-07 | t=0.1060s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.1742e-05 | t=2.8827s
    tv | MR=0.2 | seed=0 | MAE=8.7638e-07 | t=0.2145s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=4.8591e-06 | t=0.0092s
    trss | MR=0.2 | seed=0 | MAE=4.0866e-07 | t=0.0189s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.4146e-05 | t=13.1593s

Completed: 2026-04-16T12:14:45.335634+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.