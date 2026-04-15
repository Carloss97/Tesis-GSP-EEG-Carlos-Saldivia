# Integration Log: it150_081
Started: 2026-04-15T00:52:05.469122+00:00
Description: Bulk normalized run it150_081 dataset=synthetic_alpha graph=vknng miss=[0.1] mode=base

## Dataset: synthetic_alpha | rows=14
  Graph: vknng built OK
    mean | MR=0.1 | seed=0 | MAE=4.3607e-02 | t=0.0036s
    nearest | MR=0.1 | seed=0 | MAE=5.6541e-02 | t=0.0048s
    tikhonov | MR=0.1 | seed=0 | MAE=2.3456e-01 | t=0.0076s
    tv | MR=0.1 | seed=0 | MAE=4.5028e-02 | t=0.1891s
    trss | MR=0.1 | seed=0 | MAE=3.3477e-02 | t=0.0174s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=4.5125e-01 | t=0.0082s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=6.7957e-01 | t=2.4975s
    mean | MR=0.1 | seed=1 | MAE=4.3636e-02 | t=0.0162s
    nearest | MR=0.1 | seed=1 | MAE=5.7009e-02 | t=0.0051s
    tikhonov | MR=0.1 | seed=1 | MAE=2.3349e-01 | t=0.0275s
    tv | MR=0.1 | seed=1 | MAE=4.4669e-02 | t=0.3467s
    trss | MR=0.1 | seed=1 | MAE=3.2515e-02 | t=0.0411s

Completed: 2026-04-15T00:52:05.470118+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.