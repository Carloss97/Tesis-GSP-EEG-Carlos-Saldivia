# Integration Log: scr_00691
Started: 2026-04-16T15:25:05.449300+00:00
Description: Screening scr_00691 ds=iris_graph_signal graph=gaussian miss=[0.4] mode=base

## Dataset: iris_graph_signal | rows=14
  Graph: gaussian__sigma1.0 built OK
    mean | MR=0.4 | seed=0 | MAE=2.7644e-01 | t=0.0017s
    nearest | MR=0.4 | seed=0 | MAE=3.5475e-01 | t=0.0020s
    tikhonov | MR=0.4 | seed=0 | MAE=3.0955e-01 | t=0.0116s
    tv | MR=0.4 | seed=0 | MAE=2.7279e-01 | t=0.2006s
    trss | MR=0.4 | seed=0 | MAE=2.3350e-01 | t=0.0039s
    graph_time_tikhonov | MR=0.4 | seed=0 | MAE=3.9060e-01 | t=0.0051s
    temporal_laplacian | MR=0.4 | seed=0 | MAE=5.8216e-01 | t=17.3626s
    mean | MR=0.4 | seed=1 | MAE=2.5974e-01 | t=0.0014s
    nearest | MR=0.4 | seed=1 | MAE=3.7471e-01 | t=0.0023s
    tikhonov | MR=0.4 | seed=1 | MAE=3.0554e-01 | t=0.0044s
    tv | MR=0.4 | seed=1 | MAE=2.6089e-01 | t=0.3516s
    trss | MR=0.4 | seed=1 | MAE=2.2330e-01 | t=0.0037s

Completed: 2026-04-16T15:25:05.450196+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.