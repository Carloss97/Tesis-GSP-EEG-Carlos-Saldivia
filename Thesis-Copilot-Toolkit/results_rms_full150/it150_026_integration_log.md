# Integration Log: it150_026
Started: 2026-04-15T00:26:11.646878+00:00
Description: Bulk normalized run it150_026 dataset=physionet_real graph=gaussian miss=[0.1] mode=base

## Dataset: physionet_eegmmidb_real | rows=42
  Graph: gaussian__sigma1.0 built OK
    mean | MR=0.1 | seed=0 | MAE=3.9669e-02 | t=0.0040s
    nearest | MR=0.1 | seed=0 | MAE=4.4949e-02 | t=0.0029s
    tikhonov | MR=0.1 | seed=0 | MAE=3.2689e-01 | t=0.0087s
    tv | MR=0.1 | seed=0 | MAE=3.9669e-02 | t=0.7651s
    trss | MR=0.1 | seed=0 | MAE=2.8849e-02 | t=0.1184s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=4.1761e-01 | t=0.0148s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=7.4262e-01 | t=3.0370s
    mean | MR=0.1 | seed=1 | MAE=3.8639e-02 | t=0.0034s
    nearest | MR=0.1 | seed=1 | MAE=4.3518e-02 | t=0.0041s
    tikhonov | MR=0.1 | seed=1 | MAE=3.2731e-01 | t=0.0070s
    tv | MR=0.1 | seed=1 | MAE=3.8639e-02 | t=0.2387s
    trss | MR=0.1 | seed=1 | MAE=2.8185e-02 | t=0.0188s

Completed: 2026-04-15T00:26:11.647639+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.