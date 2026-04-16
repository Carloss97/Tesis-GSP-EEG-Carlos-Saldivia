# Integration Log: scr_00389
Started: 2026-04-16T13:14:37.610290+00:00
Description: Screening scr_00389 ds=bci_iv2a_real_s3 graph=kalofolias miss=[0.1] mode=base

## Dataset: bci_iv2a_real_s3 | rows=14
  Graph: kalofolias built OK
    mean | MR=0.1 | seed=0 | MAE=3.0419e-07 | t=0.0020s
    nearest | MR=0.1 | seed=0 | MAE=2.4876e-07 | t=0.0083s
    tikhonov | MR=0.1 | seed=0 | MAE=1.5765e-06 | t=0.0058s
    tv | MR=0.1 | seed=0 | MAE=3.0419e-07 | t=0.2804s
    trss | MR=0.1 | seed=0 | MAE=2.1652e-07 | t=0.2352s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=2.7983e-06 | t=0.0454s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=5.5764e-06 | t=10.7252s
    mean | MR=0.1 | seed=1 | MAE=2.8472e-07 | t=0.0020s
    nearest | MR=0.1 | seed=1 | MAE=2.5230e-07 | t=0.0028s
    tikhonov | MR=0.1 | seed=1 | MAE=1.5661e-06 | t=0.0085s
    tv | MR=0.1 | seed=1 | MAE=2.8472e-07 | t=0.4238s
    trss | MR=0.1 | seed=1 | MAE=2.0313e-07 | t=0.0463s

Completed: 2026-04-16T13:14:37.611216+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.