# Integration Log: scr_00723
Started: 2026-04-16T15:41:20.754858+00:00
Description: Screening scr_00723 ds=bci_iv2a_real_s1 graph=knng miss=[0.4] mode=base

## Dataset: bci_iv2a_real_s1 | rows=14
  Graph: knng built OK
    mean | MR=0.4 | seed=0 | MAE=6.3033e-06 | t=0.0039s
    nearest | MR=0.4 | seed=0 | MAE=6.5281e-06 | t=0.0320s
    tikhonov | MR=0.4 | seed=0 | MAE=8.8934e-06 | t=0.0103s
    tv | MR=0.4 | seed=0 | MAE=6.3028e-06 | t=0.7266s
    trss | MR=0.4 | seed=0 | MAE=4.8655e-06 | t=0.3662s
    graph_time_tikhonov | MR=0.4 | seed=0 | MAE=1.2139e-05 | t=0.0134s
    temporal_laplacian | MR=0.4 | seed=0 | MAE=1.7100e-05 | t=38.1563s
    mean | MR=0.4 | seed=1 | MAE=6.2507e-06 | t=0.0041s
    nearest | MR=0.4 | seed=1 | MAE=6.8607e-06 | t=0.0177s
    tikhonov | MR=0.4 | seed=1 | MAE=8.8452e-06 | t=0.0187s
    tv | MR=0.4 | seed=1 | MAE=6.2502e-06 | t=0.4485s
    trss | MR=0.4 | seed=1 | MAE=4.8770e-06 | t=0.1781s

Completed: 2026-04-16T15:41:20.755757+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.