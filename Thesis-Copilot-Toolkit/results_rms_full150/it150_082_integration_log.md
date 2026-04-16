# Integration Log: it150_082
Started: 2026-04-15T00:52:12.711704+00:00
Description: Bulk normalized run it150_082 dataset=synthetic_beta graph=vknng miss=[0.1] mode=base

## Dataset: synthetic_beta | rows=14
  Graph: vknng built OK
    mean | MR=0.1 | seed=0 | MAE=4.3607e-02 | t=0.0020s
    nearest | MR=0.1 | seed=0 | MAE=5.6541e-02 | t=0.0025s
    tikhonov | MR=0.1 | seed=0 | MAE=2.3456e-01 | t=0.0075s
    tv | MR=0.1 | seed=0 | MAE=4.5028e-02 | t=0.1970s
    trss | MR=0.1 | seed=0 | MAE=3.3477e-02 | t=0.0182s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=4.5125e-01 | t=0.0117s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=6.7957e-01 | t=1.2878s
    mean | MR=0.1 | seed=1 | MAE=4.3636e-02 | t=0.0028s
    nearest | MR=0.1 | seed=1 | MAE=5.7009e-02 | t=0.0030s
    tikhonov | MR=0.1 | seed=1 | MAE=2.3349e-01 | t=0.0086s
    tv | MR=0.1 | seed=1 | MAE=4.4669e-02 | t=0.1917s
    trss | MR=0.1 | seed=1 | MAE=3.2515e-02 | t=0.0163s

Completed: 2026-04-15T00:52:12.713165+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.