# Integration Log: scr_00583
Started: 2026-04-16T14:27:31.482387+00:00
Description: Screening scr_00583 ds=iris_graph_signal graph=gaussian miss=[0.3] mode=base

## Dataset: iris_graph_signal | rows=14
  Graph: gaussian__sigma1.0 built OK
    mean | MR=0.3 | seed=0 | MAE=2.7644e-01 | t=0.0016s
    nearest | MR=0.3 | seed=0 | MAE=3.5475e-01 | t=0.0020s
    tikhonov | MR=0.3 | seed=0 | MAE=3.0955e-01 | t=0.0044s
    tv | MR=0.3 | seed=0 | MAE=2.7279e-01 | t=0.1408s
    trss | MR=0.3 | seed=0 | MAE=2.3350e-01 | t=0.0038s
    graph_time_tikhonov | MR=0.3 | seed=0 | MAE=3.9060e-01 | t=0.0039s
    temporal_laplacian | MR=0.3 | seed=0 | MAE=5.8216e-01 | t=1.9678s
    mean | MR=0.3 | seed=1 | MAE=2.5974e-01 | t=0.0010s
    nearest | MR=0.3 | seed=1 | MAE=3.7471e-01 | t=0.0013s
    tikhonov | MR=0.3 | seed=1 | MAE=3.0554e-01 | t=0.0071s
    tv | MR=0.3 | seed=1 | MAE=2.6089e-01 | t=0.0560s
    trss | MR=0.3 | seed=1 | MAE=2.2330e-01 | t=0.0027s

Completed: 2026-04-16T14:27:31.483280+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.