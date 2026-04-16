# Integration Log: it150_102
Started: 2026-04-15T00:40:39.628651+00:00
Description: Bulk normalized run it150_102 dataset=iv100hz_mat graph=knn miss=[0.2] mode=base

## Dataset: iv100hz_mat | rows=42
  Graph: knn__k3 built OK
    mean | MR=0.2 | seed=0 | MAE=1.6829e-02 | t=0.0027s
    nearest | MR=0.2 | seed=0 | MAE=2.5741e-02 | t=0.0055s
    tikhonov | MR=0.2 | seed=0 | MAE=4.0855e-02 | t=0.0087s
    tv | MR=0.2 | seed=0 | MAE=1.6688e-02 | t=0.2097s
    trss | MR=0.2 | seed=0 | MAE=1.3597e-02 | t=0.0210s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=6.7939e-02 | t=0.0107s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=8.1404e-02 | t=2.8222s
    mean | MR=0.2 | seed=1 | MAE=1.6767e-02 | t=0.0025s
    nearest | MR=0.2 | seed=1 | MAE=2.5796e-02 | t=0.0052s
    tikhonov | MR=0.2 | seed=1 | MAE=4.0964e-02 | t=0.0098s
    tv | MR=0.2 | seed=1 | MAE=1.6351e-02 | t=0.2179s
    trss | MR=0.2 | seed=1 | MAE=1.3699e-02 | t=0.0207s

Completed: 2026-04-15T00:40:39.629437+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.