# Integration Log: scr_00340
Started: 2026-04-16T13:05:06.619595+00:00
Description: Screening scr_00340 ds=bci_iv2a_real_s2 graph=knn miss=[0.1] mode=base

## Dataset: bci_iv2a_real_s2 | rows=14
  Graph: knn__k5 built OK
    mean | MR=0.1 | seed=0 | MAE=3.3429e-07 | t=0.0031s
    nearest | MR=0.1 | seed=0 | MAE=3.2237e-07 | t=0.0043s
    tikhonov | MR=0.1 | seed=0 | MAE=1.8042e-06 | t=0.0058s
    tv | MR=0.1 | seed=0 | MAE=3.3430e-07 | t=0.1586s
    trss | MR=0.1 | seed=0 | MAE=2.6884e-07 | t=0.0167s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=4.8386e-06 | t=0.0080s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=1.4370e-05 | t=13.7049s
    mean | MR=0.1 | seed=1 | MAE=3.4821e-07 | t=0.0020s
    nearest | MR=0.1 | seed=1 | MAE=3.1417e-07 | t=0.0028s
    tikhonov | MR=0.1 | seed=1 | MAE=1.8118e-06 | t=0.0057s
    tv | MR=0.1 | seed=1 | MAE=3.4821e-07 | t=0.1575s
    trss | MR=0.1 | seed=1 | MAE=2.7431e-07 | t=0.0166s

Completed: 2026-04-16T13:05:06.620516+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.