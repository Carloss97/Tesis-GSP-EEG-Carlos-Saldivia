# Integration Log: scr_00735
Started: 2026-04-16T11:51:29.380118+00:00
Description: Screening scr_00735 ds=bci_iv2a_real_s1 graph=vknng miss=[0.4] mode=base

## Dataset: bci_iv2a_real_s1 | rows=14
  Graph: vknng built OK
    mean | MR=0.4 | seed=0 | MAE=6.3033e-06 | t=0.0020s
    nearest | MR=0.4 | seed=0 | MAE=6.5281e-06 | t=0.0085s
    tikhonov | MR=0.4 | seed=0 | MAE=7.8074e-06 | t=0.0057s
    tv | MR=0.4 | seed=0 | MAE=6.3026e-06 | t=0.1437s
    trss | MR=0.4 | seed=0 | MAE=4.9993e-06 | t=0.0196s
    graph_time_tikhonov | MR=0.4 | seed=0 | MAE=1.0740e-05 | t=0.0079s
    temporal_laplacian | MR=0.4 | seed=0 | MAE=1.5254e-05 | t=1.2638s
    mean | MR=0.4 | seed=1 | MAE=6.2507e-06 | t=0.0021s
    nearest | MR=0.4 | seed=1 | MAE=6.8607e-06 | t=0.0088s
    tikhonov | MR=0.4 | seed=1 | MAE=7.7736e-06 | t=0.0057s
    tv | MR=0.4 | seed=1 | MAE=6.2501e-06 | t=0.1419s
    trss | MR=0.4 | seed=1 | MAE=5.0182e-06 | t=0.0209s

Completed: 2026-04-16T11:51:29.380985+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.