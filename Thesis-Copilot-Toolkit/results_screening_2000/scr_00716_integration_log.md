# Integration Log: scr_00716
Started: 2026-04-16T15:38:42.624746+00:00
Description: Screening scr_00716 ds=movielens_graph_signal graph=kalofolias miss=[0.4] mode=base

## Dataset: movielens_graph_signal | rows=14
  Graph: kalofolias built OK
    mean | MR=0.4 | seed=0 | MAE=9.1473e-02 | t=0.0031s
    nearest | MR=0.4 | seed=0 | MAE=1.0507e-01 | t=0.0188s
    tikhonov | MR=0.4 | seed=0 | MAE=1.8612e-01 | t=0.0396s
    tv | MR=0.4 | seed=0 | MAE=9.1473e-02 | t=0.4724s
    trss | MR=0.4 | seed=0 | MAE=1.1389e-01 | t=0.0794s
    graph_time_tikhonov | MR=0.4 | seed=0 | MAE=1.8463e-01 | t=0.0363s
    temporal_laplacian | MR=0.4 | seed=0 | MAE=1.7168e-01 | t=19.3675s
    mean | MR=0.4 | seed=1 | MAE=8.7528e-02 | t=0.0031s
    nearest | MR=0.4 | seed=1 | MAE=9.3427e-02 | t=0.0424s
    tikhonov | MR=0.4 | seed=1 | MAE=2.0682e-01 | t=0.0110s
    tv | MR=0.4 | seed=1 | MAE=8.7528e-02 | t=0.5940s
    trss | MR=0.4 | seed=1 | MAE=1.2425e-01 | t=0.1230s

Completed: 2026-04-16T15:38:42.626051+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.