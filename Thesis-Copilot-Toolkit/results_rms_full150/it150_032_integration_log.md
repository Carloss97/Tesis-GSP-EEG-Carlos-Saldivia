# Integration Log: it150_032
Started: 2026-04-15T00:28:12.879913+00:00
Description: Bulk normalized run it150_032 dataset=movielens_graph_signal graph=gaussian miss=[0.1] mode=base

## Dataset: movielens_graph_signal | rows=42
  Graph: gaussian__sigma1.0 built OK
    mean | MR=0.1 | seed=0 | MAE=1.7323e-02 | t=0.0027s
    nearest | MR=0.1 | seed=0 | MAE=1.5567e-02 | t=0.0040s
    tikhonov | MR=0.1 | seed=0 | MAE=1.2274e-01 | t=0.0086s
    tv | MR=0.1 | seed=0 | MAE=1.7323e-02 | t=0.2245s
    trss | MR=0.1 | seed=0 | MAE=2.2423e-02 | t=0.0188s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=1.9089e-01 | t=0.0101s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=1.6143e-01 | t=2.4963s
    mean | MR=0.1 | seed=1 | MAE=2.1103e-02 | t=0.0031s
    nearest | MR=0.1 | seed=1 | MAE=2.3466e-02 | t=0.0047s
    tikhonov | MR=0.1 | seed=1 | MAE=1.2185e-01 | t=0.0084s
    tv | MR=0.1 | seed=1 | MAE=2.1104e-02 | t=0.2690s
    trss | MR=0.1 | seed=1 | MAE=2.6753e-02 | t=0.0176s

Completed: 2026-04-15T00:28:12.880659+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.