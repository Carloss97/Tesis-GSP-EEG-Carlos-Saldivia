# Integration Log: scr_01012
Started: 2026-04-16T12:54:02.834734+00:00
Description: Screening scr_01012 ds=bci_iv2a_real_s2 graph=gaussian miss=3ch mode=lambda

## Dataset: bci_iv2a_real_s2 | rows=24
  Graph: gaussian__sigma1.0 built OK
    tv | MR=0.2 | seed=0 | MAE=8.7638e-07 | t=0.1925s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=4.5387e-06 | t=0.0079s
    trss | MR=0.2 | seed=0 | MAE=3.6928e-07 | t=0.0195s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.1729e-05 | t=7.0523s
    tv | MR=0.2 | seed=1 | MAE=9.0508e-07 | t=0.2162s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=4.5777e-06 | t=0.0078s
    trss | MR=0.2 | seed=1 | MAE=3.8400e-07 | t=0.0303s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=1.1742e-05 | t=12.0285s
    tv | MR=0.2 | seed=0 | MAE=8.7638e-07 | t=0.2668s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=4.8591e-06 | t=0.0079s
    trss | MR=0.2 | seed=0 | MAE=4.0866e-07 | t=0.0198s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.4146e-05 | t=3.5488s

Completed: 2026-04-16T12:54:02.835574+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.