# Integration Log: scr_00566
Started: 2026-04-16T14:17:38.358700+00:00
Description: Screening scr_00566 ds=physionet_real graph=knn miss=[0.3] mode=base

## Dataset: physionet_eegmmidb_real | rows=14
  Graph: knn__k7 built OK
    mean | MR=0.3 | seed=0 | MAE=7.1409e-06 | t=0.0029s
    nearest | MR=0.3 | seed=0 | MAE=8.1341e-06 | t=0.0104s
    tikhonov | MR=0.3 | seed=0 | MAE=1.0682e-05 | t=0.0381s
    tv | MR=0.3 | seed=0 | MAE=7.1259e-06 | t=0.3979s
    trss | MR=0.3 | seed=0 | MAE=3.9815e-06 | t=0.2994s
    graph_time_tikhonov | MR=0.3 | seed=0 | MAE=1.7348e-05 | t=0.0081s
    temporal_laplacian | MR=0.3 | seed=0 | MAE=3.5839e-05 | t=22.9477s
    mean | MR=0.3 | seed=1 | MAE=7.3000e-06 | t=0.0424s
    nearest | MR=0.3 | seed=1 | MAE=8.0659e-06 | t=0.0100s
    tikhonov | MR=0.3 | seed=1 | MAE=1.0744e-05 | t=0.0106s
    tv | MR=0.3 | seed=1 | MAE=7.2848e-06 | t=0.7645s
    trss | MR=0.3 | seed=1 | MAE=4.0444e-06 | t=0.2954s

Completed: 2026-04-16T14:17:38.359730+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.