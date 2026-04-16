# Integration Log: scr_00713
Started: 2026-04-16T15:36:11.721186+00:00
Description: Screening scr_00713 ds=bci_iv2a_real_s3 graph=kalofolias miss=[0.4] mode=base

## Dataset: bci_iv2a_real_s3 | rows=14
  Graph: kalofolias built OK
    mean | MR=0.4 | seed=0 | MAE=1.4549e-06 | t=0.0058s
    nearest | MR=0.4 | seed=0 | MAE=1.3679e-06 | t=0.1703s
    tikhonov | MR=0.4 | seed=0 | MAE=2.2681e-06 | t=0.0897s
    tv | MR=0.4 | seed=0 | MAE=1.4549e-06 | t=1.1737s
    trss | MR=0.4 | seed=0 | MAE=1.1908e-06 | t=0.1175s
    graph_time_tikhonov | MR=0.4 | seed=0 | MAE=3.0594e-06 | t=0.0140s
    temporal_laplacian | MR=0.4 | seed=0 | MAE=6.0918e-06 | t=22.8244s
    mean | MR=0.4 | seed=1 | MAE=1.4638e-06 | t=0.0031s
    nearest | MR=0.4 | seed=1 | MAE=1.3378e-06 | t=0.0143s
    tikhonov | MR=0.4 | seed=1 | MAE=2.2710e-06 | t=0.0117s
    tv | MR=0.4 | seed=1 | MAE=1.4638e-06 | t=0.5985s
    trss | MR=0.4 | seed=1 | MAE=1.1893e-06 | t=0.1802s

Completed: 2026-04-16T15:36:11.722079+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.