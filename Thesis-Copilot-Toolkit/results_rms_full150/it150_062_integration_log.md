# Integration Log: it150_062
Started: 2026-04-15T00:32:55.318232+00:00
Description: Bulk normalized run it150_062 dataset=physionet_real graph=knng miss=[0.1] mode=base

## Dataset: physionet_eegmmidb_real | rows=42
  Graph: knng built OK
    mean | MR=0.1 | seed=0 | MAE=3.9669e-02 | t=0.0044s
    nearest | MR=0.1 | seed=0 | MAE=4.4949e-02 | t=0.0043s
    tikhonov | MR=0.1 | seed=0 | MAE=1.0743e-01 | t=0.0082s
    tv | MR=0.1 | seed=0 | MAE=3.9280e-02 | t=0.2750s
    trss | MR=0.1 | seed=0 | MAE=1.9547e-02 | t=0.0258s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=2.2959e-01 | t=0.0116s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=5.7864e-01 | t=4.2107s
    mean | MR=0.1 | seed=1 | MAE=3.8639e-02 | t=0.0027s
    nearest | MR=0.1 | seed=1 | MAE=4.3518e-02 | t=0.0048s
    tikhonov | MR=0.1 | seed=1 | MAE=1.0686e-01 | t=0.0100s
    tv | MR=0.1 | seed=1 | MAE=3.8265e-02 | t=0.2552s
    trss | MR=0.1 | seed=1 | MAE=1.8882e-02 | t=0.0209s

Completed: 2026-04-15T00:32:55.319212+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.