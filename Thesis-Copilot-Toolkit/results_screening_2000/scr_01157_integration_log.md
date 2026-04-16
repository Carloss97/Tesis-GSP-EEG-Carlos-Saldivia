# Integration Log: scr_01157
Started: 2026-04-16T14:42:11.256093+00:00
Description: Screening scr_01157 ds=bci_iv2a_real_s3 graph=knng miss=[0.1] mode=lambda

## Dataset: bci_iv2a_real_s3 | rows=24
  Graph: knng built OK
    tv | MR=0.2 | seed=0 | MAE=7.3155e-07 | t=0.9642s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.6455e-06 | t=0.0123s
    trss | MR=0.2 | seed=0 | MAE=3.6633e-07 | t=0.3672s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.9615e-06 | t=11.6065s
    tv | MR=0.2 | seed=1 | MAE=7.3475e-07 | t=0.8545s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=1.6365e-06 | t=0.0123s
    trss | MR=0.2 | seed=1 | MAE=3.7370e-07 | t=0.7297s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=2.9702e-06 | t=18.2092s
    tv | MR=0.2 | seed=0 | MAE=7.3145e-07 | t=0.2074s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.9046e-06 | t=0.0363s
    trss | MR=0.2 | seed=0 | MAE=4.0538e-07 | t=0.2438s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=3.7146e-06 | t=29.5956s

Completed: 2026-04-16T14:42:11.257023+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.