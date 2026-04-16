# Integration Log: scr_01097
Started: 2026-04-16T13:42:02.587193+00:00
Description: Screening scr_01097 ds=bci_iv2a_real_s3 graph=knn miss=[0.1] mode=lambda

## Dataset: bci_iv2a_real_s3 | rows=24
  Graph: knn__k5 built OK
    tv | MR=0.2 | seed=0 | MAE=7.3155e-07 | t=0.2951s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.7328e-06 | t=0.0372s
    trss | MR=0.2 | seed=0 | MAE=3.6240e-07 | t=0.0402s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.9958e-06 | t=12.5255s
    tv | MR=0.2 | seed=1 | MAE=7.3474e-07 | t=0.1635s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=1.7246e-06 | t=0.0084s
    trss | MR=0.2 | seed=1 | MAE=3.7337e-07 | t=0.0197s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=3.0066e-06 | t=24.8071s
    tv | MR=0.2 | seed=0 | MAE=7.3145e-07 | t=0.1552s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.0343e-06 | t=0.0080s
    trss | MR=0.2 | seed=0 | MAE=4.0262e-07 | t=0.0208s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=3.8232e-06 | t=14.0796s

Completed: 2026-04-16T13:42:02.587933+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.