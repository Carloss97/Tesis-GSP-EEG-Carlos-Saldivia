# Integration Log: it150_050
Started: 2026-04-15T00:30:34.015058+00:00
Description: Bulk normalized run it150_050 dataset=physionet_real graph=kalofolias miss=[0.1] mode=base

## Dataset: physionet_eegmmidb_real | rows=42
  Graph: kalofolias built OK
    mean | MR=0.1 | seed=0 | MAE=3.9669e-02 | t=0.0031s
    nearest | MR=0.1 | seed=0 | MAE=4.4949e-02 | t=0.0034s
    tikhonov | MR=0.1 | seed=0 | MAE=2.0892e-01 | t=0.0073s
    tv | MR=0.1 | seed=0 | MAE=3.9669e-02 | t=0.2307s
    trss | MR=0.1 | seed=0 | MAE=2.8904e-02 | t=0.0190s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=3.6118e-01 | t=0.0092s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=6.4291e-01 | t=1.8725s
    mean | MR=0.1 | seed=1 | MAE=3.8639e-02 | t=0.0020s
    nearest | MR=0.1 | seed=1 | MAE=4.3518e-02 | t=0.0041s
    tikhonov | MR=0.1 | seed=1 | MAE=2.0874e-01 | t=0.0087s
    tv | MR=0.1 | seed=1 | MAE=3.8639e-02 | t=0.2177s
    trss | MR=0.1 | seed=1 | MAE=2.8239e-02 | t=0.0174s

Completed: 2026-04-15T00:30:34.015913+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.