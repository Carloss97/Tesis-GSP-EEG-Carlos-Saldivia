# Integration Log: scr_00619
Started: 2026-04-16T14:45:53.182161+00:00
Description: Screening scr_00619 ds=iris_graph_signal graph=knng miss=[0.3] mode=base

## Dataset: iris_graph_signal | rows=14
  Graph: knng built OK
    mean | MR=0.3 | seed=0 | MAE=2.7644e-01 | t=0.0014s
    nearest | MR=0.3 | seed=0 | MAE=3.5475e-01 | t=0.0021s
    tikhonov | MR=0.3 | seed=0 | MAE=3.0955e-01 | t=0.0035s
    tv | MR=0.3 | seed=0 | MAE=2.7279e-01 | t=0.1751s
    trss | MR=0.3 | seed=0 | MAE=2.3350e-01 | t=0.0037s
    graph_time_tikhonov | MR=0.3 | seed=0 | MAE=3.9060e-01 | t=0.0039s
    temporal_laplacian | MR=0.3 | seed=0 | MAE=5.8216e-01 | t=19.7046s
    mean | MR=0.3 | seed=1 | MAE=2.5974e-01 | t=0.0015s
    nearest | MR=0.3 | seed=1 | MAE=3.7471e-01 | t=0.0025s
    tikhonov | MR=0.3 | seed=1 | MAE=3.0554e-01 | t=0.0223s
    tv | MR=0.3 | seed=1 | MAE=2.6089e-01 | t=0.2666s
    trss | MR=0.3 | seed=1 | MAE=2.2330e-01 | t=0.0036s

Completed: 2026-04-16T14:45:53.183069+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.