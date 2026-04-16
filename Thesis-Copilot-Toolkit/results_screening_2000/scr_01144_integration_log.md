# Integration Log: scr_01144
Started: 2026-04-16T14:24:01.612991+00:00
Description: Screening scr_01144 ds=bci_iv2a_real_s2 graph=kalofolias miss=[0.1] mode=lambda

## Dataset: bci_iv2a_real_s2 | rows=24
  Graph: kalofolias built OK
    tv | MR=0.2 | seed=0 | MAE=8.7638e-07 | t=0.6306s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=4.0684e-06 | t=0.2087s
    trss | MR=0.2 | seed=0 | MAE=3.7113e-07 | t=0.5017s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=6.9934e-06 | t=24.0207s
    tv | MR=0.2 | seed=1 | MAE=9.0508e-07 | t=0.1905s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=4.1155e-06 | t=0.0081s
    trss | MR=0.2 | seed=1 | MAE=3.8645e-07 | t=0.0200s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=7.0194e-06 | t=22.1401s
    tv | MR=0.2 | seed=0 | MAE=8.7638e-07 | t=0.8674s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=4.3035e-06 | t=0.0266s
    trss | MR=0.2 | seed=0 | MAE=4.0887e-07 | t=0.4514s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=9.6423e-06 | t=18.8319s

Completed: 2026-04-16T14:24:01.613879+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.