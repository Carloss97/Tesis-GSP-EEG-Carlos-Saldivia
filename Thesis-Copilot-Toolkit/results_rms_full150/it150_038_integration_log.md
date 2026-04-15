# Integration Log: it150_038
Started: 2026-04-15T00:28:34.616908+00:00
Description: Bulk normalized run it150_038 dataset=physionet_real graph=gaussian miss=[0.1] mode=base

## Dataset: physionet_eegmmidb_real | rows=42
  Graph: gaussian__sigma0.6 built OK
    mean | MR=0.1 | seed=0 | MAE=3.9669e-02 | t=0.0021s
    nearest | MR=0.1 | seed=0 | MAE=4.4949e-02 | t=0.0031s
    tikhonov | MR=0.1 | seed=0 | MAE=3.2523e-01 | t=0.0060s
    tv | MR=0.1 | seed=0 | MAE=3.9669e-02 | t=0.2102s
    trss | MR=0.1 | seed=0 | MAE=2.8750e-02 | t=0.0167s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=4.1706e-01 | t=0.0080s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=7.4184e-01 | t=3.0650s
    mean | MR=0.1 | seed=1 | MAE=3.8639e-02 | t=0.0026s
    nearest | MR=0.1 | seed=1 | MAE=4.3518e-02 | t=0.0032s
    tikhonov | MR=0.1 | seed=1 | MAE=3.2564e-01 | t=0.0067s
    tv | MR=0.1 | seed=1 | MAE=3.8639e-02 | t=0.2402s
    trss | MR=0.1 | seed=1 | MAE=2.8089e-02 | t=0.0178s

Completed: 2026-04-15T00:28:34.617752+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.