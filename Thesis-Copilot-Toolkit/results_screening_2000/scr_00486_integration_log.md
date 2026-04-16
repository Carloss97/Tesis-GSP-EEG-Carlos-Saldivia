# Integration Log: scr_00486
Started: 2026-04-16T13:47:32.859217+00:00
Description: Screening scr_00486 ds=iv100hz_mat graph=gaussian miss=[0.2] mode=base

## Dataset: iv100hz_mat | rows=14
  Graph: gaussian__sigma0.6 built OK
    mean | MR=0.2 | seed=0 | MAE=5.2754e+01 | t=0.0035s
    nearest | MR=0.2 | seed=0 | MAE=8.0647e+01 | t=0.0132s
    tikhonov | MR=0.2 | seed=0 | MAE=1.2320e+02 | t=0.0085s
    tv | MR=0.2 | seed=0 | MAE=3.2942e+01 | t=0.2815s
    trss | MR=0.2 | seed=0 | MAE=4.0264e+01 | t=0.3307s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.9059e+02 | t=0.0261s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.3568e+02 | t=14.2624s
    mean | MR=0.2 | seed=1 | MAE=5.2652e+01 | t=0.0020s
    nearest | MR=0.2 | seed=1 | MAE=8.0770e+01 | t=0.0049s
    tikhonov | MR=0.2 | seed=1 | MAE=1.2334e+02 | t=0.0057s
    tv | MR=0.2 | seed=1 | MAE=3.5327e+01 | t=0.2039s
    trss | MR=0.2 | seed=1 | MAE=4.0830e+01 | t=0.1691s

Completed: 2026-04-16T13:47:32.860075+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.