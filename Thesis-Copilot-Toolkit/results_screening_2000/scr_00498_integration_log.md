# Integration Log: scr_00498
Started: 2026-04-16T13:51:36.360287+00:00
Description: Screening scr_00498 ds=iv100hz_mat graph=kalofolias miss=[0.2] mode=base

## Dataset: iv100hz_mat | rows=14
  Graph: kalofolias built OK
    mean | MR=0.2 | seed=0 | MAE=5.2754e+01 | t=0.0031s
    nearest | MR=0.2 | seed=0 | MAE=8.0647e+01 | t=0.0084s
    tikhonov | MR=0.2 | seed=0 | MAE=1.4075e+02 | t=0.0488s
    tv | MR=0.2 | seed=0 | MAE=5.1746e+01 | t=0.6504s
    trss | MR=0.2 | seed=0 | MAE=2.0904e+01 | t=0.4072s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=1.4301e+02 | t=0.0209s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=2.9098e+02 | t=11.1460s
    mean | MR=0.2 | seed=1 | MAE=5.2652e+01 | t=0.0032s
    nearest | MR=0.2 | seed=1 | MAE=8.0770e+01 | t=0.0078s
    tikhonov | MR=0.2 | seed=1 | MAE=1.4129e+02 | t=0.0349s
    tv | MR=0.2 | seed=1 | MAE=5.1845e+01 | t=0.3482s
    trss | MR=0.2 | seed=1 | MAE=2.0602e+01 | t=0.0208s

Completed: 2026-04-16T13:51:36.361334+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.