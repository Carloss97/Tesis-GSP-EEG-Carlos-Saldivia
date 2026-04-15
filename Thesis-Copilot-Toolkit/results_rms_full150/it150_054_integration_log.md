# Integration Log: it150_054
Started: 2026-04-15T00:32:05.830355+00:00
Description: Bulk normalized run it150_054 dataset=iv100hz_mat graph=kalofolias miss=[0.1] mode=base

## Dataset: iv100hz_mat | rows=42
  Graph: kalofolias built OK
    mean | MR=0.1 | seed=0 | MAE=8.1185e-03 | t=0.0035s
    nearest | MR=0.1 | seed=0 | MAE=1.2947e-02 | t=0.0040s
    tikhonov | MR=0.1 | seed=0 | MAE=6.1914e-02 | t=0.0088s
    tv | MR=0.1 | seed=0 | MAE=7.9676e-03 | t=0.2290s
    trss | MR=0.1 | seed=0 | MAE=3.0374e-03 | t=0.0194s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=6.2693e-02 | t=0.0107s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=1.1520e-01 | t=1.9247s
    mean | MR=0.1 | seed=1 | MAE=8.3274e-03 | t=0.0020s
    nearest | MR=0.1 | seed=1 | MAE=1.3348e-02 | t=0.0036s
    tikhonov | MR=0.1 | seed=1 | MAE=6.2402e-02 | t=0.0097s
    tv | MR=0.1 | seed=1 | MAE=8.3126e-03 | t=0.2332s
    trss | MR=0.1 | seed=1 | MAE=3.1515e-03 | t=0.0196s

Completed: 2026-04-15T00:32:05.831463+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.