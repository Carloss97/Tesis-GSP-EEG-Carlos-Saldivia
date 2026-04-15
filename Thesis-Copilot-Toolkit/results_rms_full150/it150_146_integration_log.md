# Integration Log: it150_146
Started: 2026-04-15T00:58:01.939313+00:00
Description: Bulk normalized run it150_146 dataset=physionet_real graph=kalofolias miss=[0.2] mode=base

## Dataset: physionet_eegmmidb_real | rows=14
  Graph: kalofolias built OK
    mean | MR=0.2 | seed=0 | MAE=7.8019e-02 | t=0.0026s
    nearest | MR=0.2 | seed=0 | MAE=8.9975e-02 | t=0.0044s
    tikhonov | MR=0.2 | seed=0 | MAE=2.3187e-01 | t=0.0071s
    tv | MR=0.2 | seed=0 | MAE=7.8019e-02 | t=0.2369s
    trss | MR=0.2 | seed=0 | MAE=5.8008e-02 | t=0.0199s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=3.7030e-01 | t=0.0113s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=6.5672e-01 | t=1.8478s
    mean | MR=0.2 | seed=1 | MAE=7.7313e-02 | t=0.0028s
    nearest | MR=0.2 | seed=1 | MAE=8.7931e-02 | t=0.0055s
    tikhonov | MR=0.2 | seed=1 | MAE=2.3198e-01 | t=0.0068s
    tv | MR=0.2 | seed=1 | MAE=7.7313e-02 | t=0.2318s
    trss | MR=0.2 | seed=1 | MAE=5.7380e-02 | t=0.0200s

Completed: 2026-04-15T00:58:01.940323+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.