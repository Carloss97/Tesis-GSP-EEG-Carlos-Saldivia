# Integration Log: scr_00726
Started: 2026-04-16T11:51:04.880342+00:00
Description: Screening scr_00726 ds=iv100hz_mat graph=knng miss=[0.4] mode=base

## Dataset: iv100hz_mat | rows=14
  Graph: knng built OK
    mean | MR=0.4 | seed=0 | MAE=1.0557e+02 | t=0.0021s
    nearest | MR=0.4 | seed=0 | MAE=1.5725e+02 | t=0.0085s
    tikhonov | MR=0.4 | seed=0 | MAE=1.5195e+02 | t=0.0057s
    tv | MR=0.4 | seed=0 | MAE=1.1971e+02 | t=0.1421s
    trss | MR=0.4 | seed=0 | MAE=9.4610e+01 | t=0.0194s
    graph_time_tikhonov | MR=0.4 | seed=0 | MAE=1.9439e+02 | t=0.0083s
    temporal_laplacian | MR=0.4 | seed=0 | MAE=2.2668e+02 | t=1.2981s
    mean | MR=0.4 | seed=1 | MAE=1.0515e+02 | t=0.0020s
    nearest | MR=0.4 | seed=1 | MAE=1.5788e+02 | t=0.0085s
    tikhonov | MR=0.4 | seed=1 | MAE=1.5334e+02 | t=0.0058s
    tv | MR=0.4 | seed=1 | MAE=1.2367e+02 | t=0.1437s
    trss | MR=0.4 | seed=1 | MAE=9.4609e+01 | t=0.0208s

Completed: 2026-04-16T11:51:04.881040+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.