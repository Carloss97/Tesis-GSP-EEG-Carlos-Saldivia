# Integration Log: it150_131
Started: 2026-04-15T00:56:19.389999+00:00
Description: Bulk normalized run it150_131 dataset=synthetic_broad graph=gaussian miss=[0.2] mode=base

## Dataset: synthetic_broad | rows=14
  Graph: gaussian__sigma1.0 built OK
    mean | MR=0.2 | seed=0 | MAE=1.0968e-01 | t=0.0025s
    nearest | MR=0.2 | seed=0 | MAE=1.4989e-01 | t=0.0048s
    tikhonov | MR=0.2 | seed=0 | MAE=3.7764e-01 | t=0.0072s
    tv | MR=0.2 | seed=0 | MAE=1.0940e-01 | t=0.2292s
    trss | MR=0.2 | seed=0 | MAE=7.9647e-02 | t=0.0195s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=5.4212e-01 | t=0.0099s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=7.8355e-01 | t=2.8721s
    mean | MR=0.2 | seed=1 | MAE=1.1027e-01 | t=0.0020s
    nearest | MR=0.2 | seed=1 | MAE=1.5218e-01 | t=0.0056s
    tikhonov | MR=0.2 | seed=1 | MAE=3.7709e-01 | t=0.0081s
    tv | MR=0.2 | seed=1 | MAE=1.1000e-01 | t=0.2427s
    trss | MR=0.2 | seed=1 | MAE=7.9910e-02 | t=0.0204s

Completed: 2026-04-15T00:56:19.391051+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.