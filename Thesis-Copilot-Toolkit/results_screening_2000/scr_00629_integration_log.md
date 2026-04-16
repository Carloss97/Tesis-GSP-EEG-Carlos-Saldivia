# Integration Log: scr_00629
Started: 2026-04-16T14:50:19.324432+00:00
Description: Screening scr_00629 ds=bci_iv2a_real_s3 graph=vknng miss=[0.3] mode=base

## Dataset: bci_iv2a_real_s3 | rows=14
  Graph: vknng built OK
    mean | MR=0.3 | seed=0 | MAE=1.0520e-06 | t=0.0032s
    nearest | MR=0.3 | seed=0 | MAE=9.1472e-07 | t=0.0326s
    tikhonov | MR=0.3 | seed=0 | MAE=1.5905e-06 | t=0.0539s
    tv | MR=0.3 | seed=0 | MAE=1.0521e-06 | t=0.4859s
    trss | MR=0.3 | seed=0 | MAE=9.7986e-07 | t=0.1015s
    graph_time_tikhonov | MR=0.3 | seed=0 | MAE=2.4405e-06 | t=0.0130s
    temporal_laplacian | MR=0.3 | seed=0 | MAE=4.6645e-06 | t=27.7507s
    mean | MR=0.3 | seed=1 | MAE=1.0248e-06 | t=0.0031s
    nearest | MR=0.3 | seed=1 | MAE=9.0879e-07 | t=0.0449s
    tikhonov | MR=0.3 | seed=1 | MAE=1.5882e-06 | t=0.0144s
    tv | MR=0.3 | seed=1 | MAE=1.0249e-06 | t=0.3604s
    trss | MR=0.3 | seed=1 | MAE=9.8947e-07 | t=0.1884s

Completed: 2026-04-16T14:50:19.325709+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.