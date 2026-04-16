# Integration Log: scr_00749
Started: 2026-04-16T11:52:22.482907+00:00
Description: Screening scr_00749 ds=bci_iv2a_real_s3 graph=aew miss=[0.4] mode=base

## Dataset: bci_iv2a_real_s3 | rows=14
  Graph: aew built OK
    mean | MR=0.4 | seed=0 | MAE=1.4549e-06 | t=0.0021s
    nearest | MR=0.4 | seed=0 | MAE=1.3679e-06 | t=0.0115s
    tikhonov | MR=0.4 | seed=0 | MAE=1.9987e-06 | t=0.0060s
    tv | MR=0.4 | seed=0 | MAE=1.4547e-06 | t=0.1538s
    trss | MR=0.4 | seed=0 | MAE=1.3448e-06 | t=0.0202s
    graph_time_tikhonov | MR=0.4 | seed=0 | MAE=2.7116e-06 | t=0.0081s
    temporal_laplacian | MR=0.4 | seed=0 | MAE=5.5306e-06 | t=1.2873s
    mean | MR=0.4 | seed=1 | MAE=1.4638e-06 | t=0.0020s
    nearest | MR=0.4 | seed=1 | MAE=1.3378e-06 | t=0.0086s
    tikhonov | MR=0.4 | seed=1 | MAE=2.0136e-06 | t=0.0058s
    tv | MR=0.4 | seed=1 | MAE=1.4637e-06 | t=0.1515s
    trss | MR=0.4 | seed=1 | MAE=1.3444e-06 | t=0.0208s

Completed: 2026-04-16T11:52:22.483762+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.