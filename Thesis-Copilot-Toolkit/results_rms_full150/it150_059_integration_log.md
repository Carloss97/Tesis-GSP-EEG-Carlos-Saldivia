# Integration Log: it150_059
Started: 2026-04-15T00:50:22.115655+00:00
Description: Bulk normalized run it150_059 dataset=synthetic_broad graph=kalofolias miss=[0.1] mode=base

## Dataset: synthetic_broad | rows=14
  Graph: kalofolias built OK
    mean | MR=0.1 | seed=0 | MAE=5.4881e-02 | t=0.0035s
    nearest | MR=0.1 | seed=0 | MAE=7.5105e-02 | t=0.0054s
    tikhonov | MR=0.1 | seed=0 | MAE=6.1805e-01 | t=0.0091s
    tv | MR=0.1 | seed=0 | MAE=5.4881e-02 | t=0.2084s
    trss | MR=0.1 | seed=0 | MAE=4.9552e-02 | t=0.0182s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=6.1974e-01 | t=0.0109s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=8.8760e-01 | t=5.8347s
    mean | MR=0.1 | seed=1 | MAE=5.4906e-02 | t=0.0042s
    nearest | MR=0.1 | seed=1 | MAE=7.4297e-02 | t=0.0075s
    tikhonov | MR=0.1 | seed=1 | MAE=6.1886e-01 | t=0.0085s
    tv | MR=0.1 | seed=1 | MAE=5.4906e-02 | t=0.2033s
    trss | MR=0.1 | seed=1 | MAE=4.7873e-02 | t=0.0193s

Completed: 2026-04-15T00:50:22.117438+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.