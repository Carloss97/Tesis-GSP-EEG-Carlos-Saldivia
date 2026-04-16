# Integration Log: scr_00893
Started: 2026-04-16T12:10:57.459994+00:00
Description: Screening scr_00893 ds=bci_iv2a_real_s3 graph=knn miss=2ch mode=lambda

## Dataset: bci_iv2a_real_s3 | rows=24
  Graph: knn__k7 built OK
    tv | MR=0.2 | seed=0 | MAE=7.3147e-07 | t=0.3799s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.8640e-06 | t=0.0323s
    trss | MR=0.2 | seed=0 | MAE=3.4930e-07 | t=0.0790s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=3.4121e-06 | t=4.1564s
    tv | MR=0.2 | seed=1 | MAE=7.3468e-07 | t=0.1922s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=1.8568e-06 | t=0.0079s
    trss | MR=0.2 | seed=1 | MAE=3.5867e-07 | t=0.0188s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=3.4241e-06 | t=2.4572s
    tv | MR=0.2 | seed=0 | MAE=7.3141e-07 | t=0.2678s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.2199e-06 | t=0.0130s
    trss | MR=0.2 | seed=0 | MAE=3.8288e-07 | t=0.0556s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=4.3080e-06 | t=2.6142s

Completed: 2026-04-16T12:10:57.460718+00:00
Total rows: 24
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.