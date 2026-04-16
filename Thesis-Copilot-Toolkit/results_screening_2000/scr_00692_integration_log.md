# Integration Log: scr_00692
Started: 2026-04-16T15:25:57.070284+00:00
Description: Screening scr_00692 ds=movielens_graph_signal graph=gaussian miss=[0.4] mode=base

## Dataset: movielens_graph_signal | rows=14
  Graph: gaussian__sigma1.0 built OK
    mean | MR=0.4 | seed=0 | MAE=9.1473e-02 | t=0.0031s
    nearest | MR=0.4 | seed=0 | MAE=1.0507e-01 | t=0.0537s
    tikhonov | MR=0.4 | seed=0 | MAE=1.4052e-01 | t=0.0104s
    tv | MR=0.4 | seed=0 | MAE=9.1477e-02 | t=0.8209s
    trss | MR=0.4 | seed=0 | MAE=1.0897e-01 | t=0.5565s
    graph_time_tikhonov | MR=0.4 | seed=0 | MAE=1.7221e-01 | t=0.0398s
    temporal_laplacian | MR=0.4 | seed=0 | MAE=1.5854e-01 | t=24.4550s
    mean | MR=0.4 | seed=1 | MAE=8.7528e-02 | t=0.0066s
    nearest | MR=0.4 | seed=1 | MAE=9.3427e-02 | t=0.0423s
    tikhonov | MR=0.4 | seed=1 | MAE=1.4801e-01 | t=0.0208s
    tv | MR=0.4 | seed=1 | MAE=8.7527e-02 | t=0.4916s
    trss | MR=0.4 | seed=1 | MAE=1.0461e-01 | t=0.0860s

Completed: 2026-04-16T15:25:57.071260+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.