# Integration Log: scr_00630
Started: 2026-04-16T14:51:28.762609+00:00
Description: Screening scr_00630 ds=iv100hz_mat graph=vknng miss=[0.3] mode=base

## Dataset: iv100hz_mat | rows=14
  Graph: vknng built OK
    mean | MR=0.3 | seed=0 | MAE=7.3919e+01 | t=0.0021s
    nearest | MR=0.3 | seed=0 | MAE=1.1253e+02 | t=0.0064s
    tikhonov | MR=0.3 | seed=0 | MAE=1.2724e+02 | t=0.0115s
    tv | MR=0.3 | seed=0 | MAE=6.3971e+01 | t=0.2551s
    trss | MR=0.3 | seed=0 | MAE=6.0939e+01 | t=0.1459s
    graph_time_tikhonov | MR=0.3 | seed=0 | MAE=1.8368e+02 | t=0.0151s
    temporal_laplacian | MR=0.3 | seed=0 | MAE=2.1884e+02 | t=32.6431s
    mean | MR=0.3 | seed=1 | MAE=7.2756e+01 | t=0.0033s
    nearest | MR=0.3 | seed=1 | MAE=1.1224e+02 | t=0.0137s
    tikhonov | MR=0.3 | seed=1 | MAE=1.2737e+02 | t=0.0401s
    tv | MR=0.3 | seed=1 | MAE=6.2952e+01 | t=0.2981s
    trss | MR=0.3 | seed=1 | MAE=5.9999e+01 | t=0.1594s

Completed: 2026-04-16T14:51:28.763766+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.