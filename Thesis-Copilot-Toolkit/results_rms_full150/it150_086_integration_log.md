# Integration Log: it150_086
Started: 2026-04-15T00:37:19.562004+00:00
Description: Bulk normalized run it150_086 dataset=physionet_real graph=aew miss=[0.1] mode=base

## Dataset: physionet_eegmmidb_real | rows=42
  Graph: aew built OK
    mean | MR=0.1 | seed=0 | MAE=3.9669e-02 | t=0.0028s
    nearest | MR=0.1 | seed=0 | MAE=4.4949e-02 | t=0.0033s
    tikhonov | MR=0.1 | seed=0 | MAE=9.1862e-02 | t=0.0071s
    tv | MR=0.1 | seed=0 | MAE=3.9170e-02 | t=0.2017s
    trss | MR=0.1 | seed=0 | MAE=1.9213e-02 | t=0.0192s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=2.0752e-01 | t=0.0097s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=5.3956e-01 | t=1.8812s
    mean | MR=0.1 | seed=1 | MAE=3.8639e-02 | t=0.0020s
    nearest | MR=0.1 | seed=1 | MAE=4.3518e-02 | t=0.0029s
    tikhonov | MR=0.1 | seed=1 | MAE=9.1153e-02 | t=0.0077s
    tv | MR=0.1 | seed=1 | MAE=3.8165e-02 | t=0.1870s
    trss | MR=0.1 | seed=1 | MAE=1.8435e-02 | t=0.0193s

Completed: 2026-04-15T00:37:19.562953+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.