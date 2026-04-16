# Integration Log: scr_00438
Started: 2026-04-16T13:31:32.379631+00:00
Description: Screening scr_00438 ds=iv100hz_mat graph=knn miss=[0.2] mode=base

## Dataset: iv100hz_mat | rows=14
  Graph: knn__k3 built OK
    mean | MR=0.2 | seed=0 | MAE=5.2754e+01 | t=0.0033s
    nearest | MR=0.2 | seed=0 | MAE=8.0647e+01 | t=0.0078s
    tikhonov | MR=0.2 | seed=0 | MAE=1.0881e+02 | t=0.0722s
    tv | MR=0.2 | seed=0 | MAE=5.1681e+01 | t=0.5463s
    trss | MR=0.2 | seed=0 | MAE=4.3043e+01 | t=0.1762s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.7075e+02 | t=0.0148s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.0559e+02 | t=10.7976s
    mean | MR=0.2 | seed=1 | MAE=5.2652e+01 | t=0.0020s
    nearest | MR=0.2 | seed=1 | MAE=8.0770e+01 | t=0.0049s
    tikhonov | MR=0.2 | seed=1 | MAE=1.0985e+02 | t=0.0057s
    tv | MR=0.2 | seed=1 | MAE=5.0168e+01 | t=0.1452s
    trss | MR=0.2 | seed=1 | MAE=4.4617e+01 | t=0.0180s

Completed: 2026-04-16T13:31:32.401724+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.