# Integration Log: scr_00137
Started: 2026-04-16T15:22:08.958370+00:00
Description: Screening scr_00137 ds=bci_iv2a_real_s3 graph=knn miss=2ch mode=base

## Dataset: bci_iv2a_real_s3 | rows=14
  Graph: knn__k7 built OK
    mean | MR=2ch | seed=0 | MAE=3.0419e-07 | t=0.0037s
    nearest | MR=2ch | seed=0 | MAE=2.4876e-07 | t=0.0078s
    tikhonov | MR=2ch | seed=0 | MAE=1.8502e-06 | t=0.0450s
    tv | MR=2ch | seed=0 | MAE=3.0421e-07 | t=0.6754s
    trss | MR=2ch | seed=0 | MAE=2.4794e-07 | t=0.5110s
    graph_time_tikhonov | MR=2ch | seed=0 | MAE=2.9183e-06 | t=0.0355s
    temporal_laplacian | MR=2ch | seed=0 | MAE=5.8797e-06 | t=35.1848s
    mean | MR=2ch | seed=1 | MAE=2.8472e-07 | t=0.0049s
    nearest | MR=2ch | seed=1 | MAE=2.5230e-07 | t=0.0053s
    tikhonov | MR=2ch | seed=1 | MAE=1.8374e-06 | t=0.0103s
    tv | MR=2ch | seed=1 | MAE=2.8474e-07 | t=0.7898s
    trss | MR=2ch | seed=1 | MAE=2.3291e-07 | t=0.2505s

Completed: 2026-04-16T15:22:08.959459+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.