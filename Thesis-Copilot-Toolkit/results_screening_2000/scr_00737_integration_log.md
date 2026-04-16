# Integration Log: scr_00737
Started: 2026-04-16T11:51:40.671949+00:00
Description: Screening scr_00737 ds=bci_iv2a_real_s3 graph=vknng miss=[0.4] mode=base

## Dataset: bci_iv2a_real_s3 | rows=14
  Graph: vknng built OK
    mean | MR=0.4 | seed=0 | MAE=1.4549e-06 | t=0.0021s
    nearest | MR=0.4 | seed=0 | MAE=1.3679e-06 | t=0.0086s
    tikhonov | MR=0.4 | seed=0 | MAE=1.9276e-06 | t=0.0064s
    tv | MR=0.4 | seed=0 | MAE=1.4549e-06 | t=0.1463s
    trss | MR=0.4 | seed=0 | MAE=1.4348e-06 | t=0.0201s
    graph_time_tikhonov | MR=0.4 | seed=0 | MAE=2.6223e-06 | t=0.0079s
    temporal_laplacian | MR=0.4 | seed=0 | MAE=5.0406e-06 | t=1.2811s
    mean | MR=0.4 | seed=1 | MAE=1.4638e-06 | t=0.0020s
    nearest | MR=0.4 | seed=1 | MAE=1.3378e-06 | t=0.0085s
    tikhonov | MR=0.4 | seed=1 | MAE=1.9393e-06 | t=0.0058s
    tv | MR=0.4 | seed=1 | MAE=1.4638e-06 | t=0.1449s
    trss | MR=0.4 | seed=1 | MAE=1.4380e-06 | t=0.0201s

Completed: 2026-04-16T11:51:40.672647+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.