# Integration Log: scr_00579
Started: 2026-04-16T14:24:28.434428+00:00
Description: Screening scr_00579 ds=bci_iv2a_real_s1 graph=gaussian miss=[0.3] mode=base

## Dataset: bci_iv2a_real_s1 | rows=14
  Graph: gaussian__sigma1.0 built OK
    mean | MR=0.3 | seed=0 | MAE=4.4732e-06 | t=0.0031s
    nearest | MR=0.3 | seed=0 | MAE=4.7753e-06 | t=0.0219s
    tikhonov | MR=0.3 | seed=0 | MAE=1.1555e-05 | t=0.0087s
    tv | MR=0.3 | seed=0 | MAE=4.4732e-06 | t=0.4983s
    trss | MR=0.3 | seed=0 | MAE=3.3338e-06 | t=0.6858s
    graph_time_tikhonov | MR=0.3 | seed=0 | MAE=1.3684e-05 | t=0.0452s
    temporal_laplacian | MR=0.3 | seed=0 | MAE=1.9411e-05 | t=6.6105s
    mean | MR=0.3 | seed=1 | MAE=4.4548e-06 | t=0.0024s
    nearest | MR=0.3 | seed=1 | MAE=4.6851e-06 | t=0.0121s
    tikhonov | MR=0.3 | seed=1 | MAE=1.1473e-05 | t=0.0087s
    tv | MR=0.3 | seed=1 | MAE=4.4548e-06 | t=0.5140s
    trss | MR=0.3 | seed=1 | MAE=3.3023e-06 | t=0.0815s

Completed: 2026-04-16T14:24:28.435173+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.