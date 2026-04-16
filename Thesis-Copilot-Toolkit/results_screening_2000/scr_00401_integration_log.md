# Integration Log: scr_00401
Started: 2026-04-16T13:18:24.119123+00:00
Description: Screening scr_00401 ds=bci_iv2a_real_s3 graph=knng miss=[0.1] mode=base

## Dataset: bci_iv2a_real_s3 | rows=14
  Graph: knng built OK
    mean | MR=0.1 | seed=0 | MAE=3.0419e-07 | t=0.0030s
    nearest | MR=0.1 | seed=0 | MAE=2.4876e-07 | t=0.0060s
    tikhonov | MR=0.1 | seed=0 | MAE=1.4321e-06 | t=0.0131s
    tv | MR=0.1 | seed=0 | MAE=3.0422e-07 | t=0.1971s
    trss | MR=0.1 | seed=0 | MAE=2.7018e-07 | t=0.2906s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=2.6054e-06 | t=0.0140s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=5.3351e-06 | t=15.5349s
    mean | MR=0.1 | seed=1 | MAE=2.8472e-07 | t=0.0098s
    nearest | MR=0.1 | seed=1 | MAE=2.5230e-07 | t=0.0078s
    tikhonov | MR=0.1 | seed=1 | MAE=1.4129e-06 | t=0.0114s
    tv | MR=0.1 | seed=1 | MAE=2.8474e-07 | t=0.1578s
    trss | MR=0.1 | seed=1 | MAE=2.5676e-07 | t=0.0169s

Completed: 2026-04-16T13:18:24.119982+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.