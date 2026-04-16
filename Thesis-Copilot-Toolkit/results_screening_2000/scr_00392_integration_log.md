# Integration Log: scr_00392
Started: 2026-04-16T13:16:01.079310+00:00
Description: Screening scr_00392 ds=movielens_graph_signal graph=kalofolias miss=[0.1] mode=base

## Dataset: movielens_graph_signal | rows=14
  Graph: kalofolias built OK
    mean | MR=0.1 | seed=0 | MAE=1.4577e-02 | t=0.0041s
    nearest | MR=0.1 | seed=0 | MAE=1.3191e-02 | t=0.0299s
    tikhonov | MR=0.1 | seed=0 | MAE=2.0577e-01 | t=0.0094s
    tv | MR=0.1 | seed=0 | MAE=1.4577e-02 | t=0.6160s
    trss | MR=0.1 | seed=0 | MAE=2.6235e-02 | t=0.1289s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=2.0246e-01 | t=0.0128s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=1.7799e-01 | t=12.0000s
    mean | MR=0.1 | seed=1 | MAE=1.9048e-02 | t=0.0021s
    nearest | MR=0.1 | seed=1 | MAE=2.1272e-02 | t=0.0027s
    tikhonov | MR=0.1 | seed=1 | MAE=2.0094e-01 | t=0.0058s
    tv | MR=0.1 | seed=1 | MAE=1.9048e-02 | t=0.3082s
    trss | MR=0.1 | seed=1 | MAE=3.2565e-02 | t=0.0852s

Completed: 2026-04-16T13:16:01.080289+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.