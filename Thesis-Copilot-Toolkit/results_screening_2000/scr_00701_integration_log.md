# Integration Log: scr_00701
Started: 2026-04-16T15:30:11.579438+00:00
Description: Screening scr_00701 ds=bci_iv2a_real_s3 graph=gaussian miss=[0.4] mode=base

## Dataset: bci_iv2a_real_s3 | rows=14
  Graph: gaussian__sigma0.6 built OK
    mean | MR=0.4 | seed=0 | MAE=1.4549e-06 | t=0.0036s
    nearest | MR=0.4 | seed=0 | MAE=1.3679e-06 | t=0.0145s
    tikhonov | MR=0.4 | seed=0 | MAE=2.8394e-06 | t=0.0419s
    tv | MR=0.4 | seed=0 | MAE=1.4549e-06 | t=1.3299s
    trss | MR=0.4 | seed=0 | MAE=1.1908e-06 | t=0.1876s
    graph_time_tikhonov | MR=0.4 | seed=0 | MAE=3.3264e-06 | t=0.0925s
    temporal_laplacian | MR=0.4 | seed=0 | MAE=6.6659e-06 | t=31.7234s
    mean | MR=0.4 | seed=1 | MAE=1.4638e-06 | t=0.0060s
    nearest | MR=0.4 | seed=1 | MAE=1.3378e-06 | t=0.1538s
    tikhonov | MR=0.4 | seed=1 | MAE=2.8380e-06 | t=0.0156s
    tv | MR=0.4 | seed=1 | MAE=1.4638e-06 | t=2.6837s
    trss | MR=0.4 | seed=1 | MAE=1.1893e-06 | t=0.2515s

Completed: 2026-04-16T15:30:11.580534+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.