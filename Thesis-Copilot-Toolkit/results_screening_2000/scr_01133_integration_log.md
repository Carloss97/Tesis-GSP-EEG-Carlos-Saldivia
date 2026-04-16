# Integration Log: scr_01133
Started: 2026-04-16T14:11:54.348344+00:00
Description: Screening scr_01133 ds=bci_iv2a_real_s3 graph=gaussian miss=[0.1] mode=lambda

## Dataset: bci_iv2a_real_s3 | rows=24
  Graph: gaussian__sigma0.6 built OK
    tv | MR=0.2 | seed=0 | MAE=7.3135e-07 | t=0.4316s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.3141e-06 | t=0.0080s
    trss | MR=0.2 | seed=0 | MAE=3.1566e-07 | t=0.0192s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=4.4873e-06 | t=24.0754s
    tv | MR=0.2 | seed=1 | MAE=7.3458e-07 | t=0.7524s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=2.3107e-06 | t=0.0139s
    trss | MR=0.2 | seed=1 | MAE=3.3033e-07 | t=0.0220s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=4.4910e-06 | t=2.8778s
    tv | MR=0.2 | seed=0 | MAE=7.3135e-07 | t=0.1912s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.7103e-06 | t=0.0081s
    trss | MR=0.2 | seed=0 | MAE=3.4559e-07 | t=0.0197s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=5.3716e-06 | t=16.1267s

Completed: 2026-04-16T14:11:54.349056+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.