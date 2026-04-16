# Integration Log: scr_00115
Started: 2026-04-16T15:10:02.576255+00:00
Description: Screening scr_00115 ds=iris_graph_signal graph=knn miss=2ch mode=base

## Dataset: iris_graph_signal | rows=14
  Graph: knn__k3 built OK
    mean | MR=2ch | seed=0 | MAE=2.7644e-01 | t=0.0011s
    nearest | MR=2ch | seed=0 | MAE=3.5475e-01 | t=0.0013s
    tikhonov | MR=2ch | seed=0 | MAE=3.7033e-01 | t=0.0028s
    tv | MR=2ch | seed=0 | MAE=2.7751e-01 | t=0.0968s
    trss | MR=2ch | seed=0 | MAE=2.5786e-01 | t=0.0028s
    graph_time_tikhonov | MR=2ch | seed=0 | MAE=4.5695e-01 | t=0.0026s
    temporal_laplacian | MR=2ch | seed=0 | MAE=6.6315e-01 | t=1.7122s
    mean | MR=2ch | seed=1 | MAE=2.5974e-01 | t=0.0017s
    nearest | MR=2ch | seed=1 | MAE=3.7471e-01 | t=0.0039s
    tikhonov | MR=2ch | seed=1 | MAE=3.7736e-01 | t=0.0048s
    tv | MR=2ch | seed=1 | MAE=2.6133e-01 | t=0.1090s
    trss | MR=2ch | seed=1 | MAE=2.4933e-01 | t=0.0036s

Completed: 2026-04-16T15:10:02.577141+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.