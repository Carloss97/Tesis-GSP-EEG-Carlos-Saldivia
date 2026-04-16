# Integration Log: scr_01001
Started: 2026-04-16T12:50:18.391166+00:00
Description: Screening scr_01001 ds=bci_iv2a_real_s3 graph=knn miss=3ch mode=lambda

## Dataset: bci_iv2a_real_s3 | rows=24
  Graph: knn__k7 built OK
    tv | MR=0.2 | seed=0 | MAE=7.3147e-07 | t=0.1624s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.8640e-06 | t=0.0079s
    trss | MR=0.2 | seed=0 | MAE=3.4930e-07 | t=0.0200s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=3.4121e-06 | t=4.7526s
    tv | MR=0.2 | seed=1 | MAE=7.3468e-07 | t=0.3738s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=1.8568e-06 | t=0.0131s
    trss | MR=0.2 | seed=1 | MAE=3.5867e-07 | t=0.0736s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=3.4241e-06 | t=4.7593s
    tv | MR=0.2 | seed=0 | MAE=7.3141e-07 | t=0.3824s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.2199e-06 | t=0.0239s
    trss | MR=0.2 | seed=0 | MAE=3.8288e-07 | t=0.1435s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=4.3080e-06 | t=2.0320s

Completed: 2026-04-16T12:50:18.392029+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.