# Integration Log: it150_143
Started: 2026-04-15T00:57:41.749433+00:00
Description: Bulk normalized run it150_143 dataset=synthetic_broad graph=gaussian miss=[0.2] mode=base

## Dataset: synthetic_broad | rows=14
  Graph: gaussian__sigma0.6 built OK
    mean | MR=0.2 | seed=0 | MAE=1.0968e-01 | t=0.0021s
    nearest | MR=0.2 | seed=0 | MAE=1.4989e-01 | t=0.0053s
    tikhonov | MR=0.2 | seed=0 | MAE=2.9728e-01 | t=0.0066s
    tv | MR=0.2 | seed=0 | MAE=1.0995e-01 | t=0.2461s
    trss | MR=0.2 | seed=0 | MAE=8.2900e-02 | t=0.0210s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=4.8519e-01 | t=0.0125s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=7.1186e-01 | t=1.7299s
    mean | MR=0.2 | seed=1 | MAE=1.1027e-01 | t=0.0022s
    nearest | MR=0.2 | seed=1 | MAE=1.5218e-01 | t=0.0049s
    tikhonov | MR=0.2 | seed=1 | MAE=2.9678e-01 | t=0.0068s
    tv | MR=0.2 | seed=1 | MAE=1.1057e-01 | t=0.2405s
    trss | MR=0.2 | seed=1 | MAE=8.2940e-02 | t=0.0197s

Completed: 2026-04-15T00:57:41.750505+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.